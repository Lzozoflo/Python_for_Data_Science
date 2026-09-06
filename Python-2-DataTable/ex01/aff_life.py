from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def main():
    """Start of the programme."""

    try:
        df = load("life_expectancy_years.csv")
        france_data = df[df['country'] == 'France']

        france_series = france_data.drop(columns=['country']).squeeze()
        print(france_series)

        france_series.plot()
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__} : {e}")

if __name__ == '__main__':
    main()