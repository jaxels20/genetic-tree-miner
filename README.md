# Reborn and Refined: An Enhanced Genetic Algorithm for Process Discovery

This repository contains the code and data for the paper **_Reborn and Refined: An Enhanced Genetic Algorithm for Process Discovery_**. It implements a novel process discovery algorithm using a genetic approach and provides tools to reproduce the results and figures from the paper.

## 📂 Project Structure

   ```
├── requirements.txt          # Python dependencies required to run the project
├── GTM.py                    # The entrypoint for discovery
│
├── data/                     # Intermediate and processed data
│   ├── table_1/
│   └── ...
│
├── figures/                  # Final figures and tables for publication
│   ├── table_1.tex
│   └── ...
│   
├── logs/       # Real-world event logs in XES format
│   ├── 2013-cp.xes
│   └── ...
│
├── produce_data/             # Scripts to generate raw data for experiments
│   ├── generate_figure_5a.py
│   └── ...
│  
└── produce_figures/          # Scripts to create figures and tables from data
       ├── generate_table_1.py
       └── ...
   ```


## 📖 Description

This repository accompanies our research on process discovery, introducing an enhanced genetic algorithm to generate accurate and interpretable process models from event logs. The approach is benchmarked on multiple real-life datasets and compared to existing methods.

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jaxels20/genetic-tree-miner.git
   cd genetic-tree-miner
   ```
2. Install Dependencies
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. Build FastTokenBasedReplay (make sure cmake, pybind11, and gtest are installed)
   ```bash
   cd src/FastTokenBasedReplay/
   mkdir build && cd build
   cmake -DCMAKE_BUILD_TYPE=Release ..
   make
   cd ../../..
   ```
   
## ▶️ Usage
  ```bash
    python3 GTM.py --log_path logs/2013-cp.xes --output_path output.pdf --max_generations 5
  ```

## 📊 Datasets
The repository includes several real-life event logs from the 4TU Centre for Research Data. These are located in the `logs/` folder and are in .xes format. However, please note that due to size limitations, only a subset of the event logs are included here, but they can all be downloaded [HERE](https://www.tf-pm.org/resources/logs) and put into the log folder.

## 🧪 Reproducibility
Each script in `produce_figures/` and `produce_data/` generates specific results from the paper. The resulting data and figures are stored in the `data/` and `figures/` folders, respectively.

You can choose to generate both data and figures, or only the figures. The `data/` folder is pre-populated for convenience, but you can regenerate it by running the scripts in `produce_data/`. Please note that regenerating the data can be time-consuming — the estimated runtimes (assuming it is run on all event logs featured in the paper) are provided in the relevant commands.

Important: Some experiments are not fully independent, so we strongly recommend running the data-generation scripts in the order specified below to ensure consistency.

Running the data-generation scripts is optional — all required data is already included. Below you’ll find the commands to generate each figure or table.

### Table I
```bash
# Produce Table I
python3 produce_figures/generate_table_1.py       # TIME ESTIMATE: ~10 minutes
```
### Table II
```bash
# Produce data for Table II
python3 produce_data/generate_table_2.py          # TIME ESTIMATE: ~6 hours
# Produce Table II
python3 produce_figures/generate_table_2.py
```
### Figure 5a
```bash
# Produce data for Figure 5a
python3 produce_data/generate_figure_5a.py        # TIME ESTIMATE: ~18 hours
# Produce Figure 5a
python3 produce_figures/generate_figure_5a.py
```
### Figure 5b
```bash
# Produce data for Figure 5b
python3 produce_data/generate_figure_5b.py         # TIME ESTIMATE: ~5 seconds

# Produce Figure 5b
python3 produce_figures/generate_figure_5b.py
```
### Figure 5c
```bash
# Produce data for Figure 5c
python3 produce_data/generate_figure_5c.py          # TIME ESTIMATE: ~8 hours

# Produce Figure 5c
python3 produce_figures/generate_figure_5c.py
```
### Figure 5d
```bash
# Produce data for Figure 5d
python3 produce_data/generate_figure_5d.py           # TIME ESTIMATE: ~16 hours

# Produce Figure 5b
python3 produce_figures/generate_figure_5d.py
```


## 📜 License
This project is licensed under the terms of the MIT License. See LICENSE for more information.
## 📚 Citation
  ```
    @misc{

    }
  ```
