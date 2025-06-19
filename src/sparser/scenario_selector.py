# identifies impactful parameter combinations
import json
import numpy as np 
import itertools
import random 

def load_parameter_space(json_path): 
    with open(json_path, 'r') as file:
        return json.load(file)
    
def generate_param_combinations(param_space): 
    param_values = {}
    for param, cfg in param_space.items(): 
        values = list(np.arange(cfg['min'], cfg['max'] + cfg['step'], cfg['step']))
        param_values[param] = values 

    keys = list(param_values.keys())
    product = list(itertools.product(*(param_values[key] for key in keys)))

    param_grid = [dict(zip(keys, vals)) for vals in product]
    return param_grid 

def sample_random(grid, k = 20, seed = 40): 
    random.seed(seed)
    return random.sample(grid, min(k, len(grid)))

if __name__ == "__main__":
    param_space = load_parameter_space('params.json')

    full_grid = generate_param_combinations(param_space)
    print(f"Total combinations: {len(full_grid)}")

    sampled_runs = sample_random(full_grid, k=20)

    for i, run in enumerate(sampled_runs):
        print(f"Run {i + 1}: {run}")
