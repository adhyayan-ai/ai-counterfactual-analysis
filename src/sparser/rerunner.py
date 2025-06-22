# reruns with slight tweaks in parameters

from pathlib import Path
import subprocess

def save_config(run_id, config, base_dir = "../data/raw"): 
    run_folder = Path(base_dir) / f"run_{run_id:03}"
    run_folder.mksir(parents = True, exist_ok = True)
    config_path = run_folder / "config.json"
    with open(config_path, 'w') as f:
        json.dump(config, f, indent = 2)

    return run_folder, config_path

def batch_run_simulation_cli(config_path, output_dir): 
    simulator_dir = Path("../../../../Simulation/simulator/simulate.py")
    subprocess.run([
        "python", "simulate.py", 
        "--config", str(config_path), 
        "--output", str(output_dir)
    ], cwd = simulator_dir)