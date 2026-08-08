import pandas as pd


def load(path: str) -> pd.DataFrame:

    SCRIPT_DIR = __file__.rsplit("/", 1)[0] if "/" in __file__ else "."
    FILE_PATH = f"{SCRIPT_DIR}/{path}"
    try:
        df = pd.read_csv(FILE_PATH)
        row , columns = df.shape
        print(f"Loading dataset of dimensions ({row}, {columns})")
    except FileNotFoundError:
        print(f"Le fichier {FILE_PATH} n'existe pas dans ./")
    return df
