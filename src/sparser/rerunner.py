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
    
