from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

# def plotdata(df : pd.DataFrame, string:str , color):
#         data = df[df['country'] == string ].loc[:, 'country':'2050']

#         series = data.drop(columns=['country']).squeeze()

#         numeric_series = series.map()
#         numeric_series.index = numeric_series.index.astype(int)

#         plt.plot(numeric_series.index, numeric_series.values, color, label=string)
#         print(numeric_series.values)


def main():
    """Start of the programme."""

    try:
        dfincome = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        dflife = load("life_expectancy_years.csv")
        dfincomel = dfincome.loc[:, ['country', '1900']]
        dflifel = dflife.loc[:, ['country', '1900']]
        merged_df = pd.merge(
            dfincomel, 
            dflifel, 
            on='country', 
            how='inner', 
            suffixes=('_income', '_life')
        )
        series_with_country = merged_df.set_index(['country', '1900_income'])['1900_life']
        # print(series_with_country)
        df_final = series_with_country.droplevel('country').reset_index()
        df_final.plot(kind='scatter', x='1900_income', y='1900_life')

        plt.xscale('log')

        plt.xlim(300, 11000)
        plt.xticks(
            [300, 1000, 10000], 
            ['300', '1k', '10k']
        )
        plt.xlabel("Gross domestic product")

        plt.ylim(18, 56)
        plt.yticks(range(20, 56, 5))
        plt.ylabel("Life Expectancy")

        plt.title("1900")
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == '__main__':
    main()