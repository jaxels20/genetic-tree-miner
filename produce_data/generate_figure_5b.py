import pandas as pd

INPUT_FILE = "./data/table_2/evaluation_results/results_GTM-60.csv"
OUTPUT_FILE = "./data/figure_5b/data.csv"

if __name__ == "__main__":
    # Load the data
    df = pd.read_csv(INPUT_FILE)
    
    # melt the file 
    df = df.melt(id_vars='Dataset', var_name='Metric', value_name='Score')
    df = df[df['Metric'] == 'Objective Fitness']
    df.sort_values(by=['Dataset', 'Metric'], inplace=True)
    df.to_csv(OUTPUT_FILE, index=False)
        