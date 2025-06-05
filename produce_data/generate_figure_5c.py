# add the parent directory to the system path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.Discovery import Discovery
from src.FileLoader import FileLoader
from src.utils import load_hyperparameters_from_csv
import os

DATASETS_DIR = "./logs/"
OUTPUT_DIR = "./data/figure_5c/"
NUM_RUNS = 1
BEST_PARAMS = "./best_parameters.csv"
MAX_GENERATIONS = 300

def generate_monitors(method: callable):
    datasets = os.listdir(DATASETS_DIR)

    for dataset in datasets:
        print(f'Processing {dataset}')
        eventlog = FileLoader.load_eventlog(f"{DATASETS_DIR}/{dataset}")
        for i in range(NUM_RUNS):
            method(eventlog)   # Each run will export monitor object to specified export path
        

if __name__ == "__main__":
    hyper_parameters = load_hyperparameters_from_csv(BEST_PARAMS)

    # Define model
    genetic_miner = lambda log: Discovery.genetic_algorithm(
        log,
        method_name="Genetic_miner",
        export_monitor_path=OUTPUT_DIR,
        max_generations=MAX_GENERATIONS,
        **hyper_parameters,
    )
    
    generate_monitors(genetic_miner)