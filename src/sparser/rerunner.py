# reruns with different parameters
import requests 
import json 
from pathlib import Path

def send_simulation_request(config, server_url = "http://127.0.0.1:5000/simulation/"):
    '''
        Sends a simulation request to Flask server on app.py in Simulation repo. 
        Args:
            config (dict): Configuration dictionary containing simulation parameters (generated in scenario_selector.py).
            server_url (str): URL of the Flask server endpoint.

        Returns:
            dict: Response from the server, typically containing simulation results.
    '''
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(server_url, headers = headers, json = config)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e: 
        print(f"Error sending request: {e}")
        return None
    
def save_log(run_id, output_data, base_dir = "../../../data/raw"): 
    '''
    Saves the output data from a simulation run to a JSON file in a designated directory.
    Args:
        run_id (int): Unique identifier for the simulation run.
        output_data (dict): Data to be saved, typically the response from the simulation server.
        base_dir (str): Base directory where the run logs will be stored. Defaults to "../../../data/raw".

    Returns:
        None
    '''
    run_folder = Path(base_dir) / f"run_{run_id:03}"
    run_folder.mkdir(parents = True, exist_ok = True)

    with open(run_folder / "log.json", "w") as f: 
        json.dump(output_data, f, indent = 2)

def batch_run_simulations(config_list): 
    for i, config in enumerate(config_list, start = 1): 
        print(f"[+] sending run_{i:03}")
        result = send_simulation_request(config)
        if result: 
            save_log(i, result)
        else: 
            print(f"[!] Run {i:03} failed. No data saved.")
    
if __name__ == "__main__": 
    from scenario_selector import load_parameter_space, latin_hypercube_scaled
    param_space = load_parameter_space('params.json')
    samples = latin_hypercube_scaled(param_space, n_samples = 50)

    formatted_samples = []
    for sample in samples: 
        config = {
            "length": 100,  # Default length
            "location": "default_location",  # Default location
        }
        config.update(sample)
        formatted_samples.append(config)

    batch_run_simulations(formatted_samples)