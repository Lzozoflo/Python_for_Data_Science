from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def main():
    """Start of the programme."""


    try:
        df = load("life_expectancy_years.csv")
        france_data = df[df['country'] == 'France']

        # 2. Exclure la colonne 'country', convertir en Series et transposer
        france_series = france_data.drop(columns=['country']).squeeze()
        print(france_series)

        # 3. Tracer le graphique
        france_series.plot()
        plt.show()
        # france_data = df[df['country'] == 'France']
        # print(france_data)
        # france_data.plot()
        # plt.show()

    except Exception as e:
        print(f"{type(e).__name__} : {e}")

if __name__ == '__main__':
    main()