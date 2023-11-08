import pandas as pd

# Load data
def load_data():
    df = pd.read_csv("../data/nfe_produto_1000_estruturado_anotado_test.csv")
    return df

def main():
    df = load_data()
    print(df.head())