from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

# def testlabel():
#     # Sample data
#     x = [1, 2, 3, 4]
#     y1 = [1, 4, 9, 16]
#     y2 = [1, 2, 3, 4]

#     # Create the plots and assign labels for the graph legend
#     plt.plot(x, y1, label='Squared')
#     plt.plot(x, y2, label='Linear')

#     # Add a title to the graph
#     plt.title('My Awesome Graph')

#     # Add a label (legend) for each axis
#     plt.xlabel('X-Axis Name')
#     plt.ylabel('Y-Axis Name')

#     # Display the legend for the data lines/graphs
#     plt.legend()

#     # Show the final plot
#     plt.show()

# testlabel()

# multi = f"0, Kilo, K, 3,\n1, Million, M, 6,\n2, Milliard, B, 9,\n3, Trillion, T, 12,\n4, Quadrillion, Qa, 15,\n5, Quintillion, Qt, 18,\n6, Sextillion, Sx, 21,\n7, Septillion, Sp, 24,\n8, Octillion, Oc, 27,\n9, Nonillion, No, 30,\n10, Décillion, Dec, 33,\n11, Undécillion, Undec, 36,\n12, Duodécillion, Duodec, 39,\n13, Tredecillion, Trdec, 42,\n14, Quattuordécillion, QaDec, 45,\n15, Quindécillion, QiDec, 48,\n16, Sexdécillion, SxDec, 51,\n17, Septendécillion, SpDec, 54,\n18, Octodécillion, OcDec, 57,\n19, Novemdécillion, NvDec, 60,\n20, Vigintillion, Vg, 63,\n21, Unvigintillion, UVg, 66,\n22, Duovigintillion, DVg, 69,\n23, Trevigintillion, TVg, 72,\n24, Quattuorvigintillion, QaVg, 75,\n25, Quinvigintillion, QtVg, 78,\n26, Sexvigintillion, SxVg, 81,\n27, Septenvigintillion, SpVg, 84,\n28, Octovigintillion, OcVg, 87,\n29, Novemvigintillion, NoVg, 90,\n30, Trigintillion, Tg, 93,\n31, Untrigintillion, UTg, 96,\n32, Duotrigintillion, DTg, 99,\n33, Tretrigintillion, TTg, 102,\n34, Quattuortrigintillion, QaTg, 105,\n35, Quintrigintillion, QtTg, 108,\n36, Sextrightertillion, SxTg, 111,\n37, Septentrigintillion, SpTg, 114,\n38, Octotrigintillion, OcTg, 117,\n39, Novemtrigintillion, NoTg, 120,\n40, Quadragintillion, Qg, 123,\n41, Unquadragintillion, UQg, 126,\n42, Duoquadragintillion, DQg, 129,\n43, Trequadragintillion, TQg, 132,\n44, Quattuorquadragintillion, QaQg, 135,\n45, Quinquadragintillion, QtQg, 138,\n46, Sexquadragintillion, SxQg, 141,\n47, Septenquadragintillion, SpQg, 144,\n48, Octoquadragintillion, OcQg, 147,\n49, Novemquadragintillion, NoQg, 150,\n50, Quinquagintillion, Qq, 153,\n51, Unquinquagintillion, UQq, 156,\n52, Duoquinquagintillion, DQq, 159,\n53, Trequinquagintillion, TQq, 162,\n54, Quattuorquinquagintillion, QaQq, 165,\n55, Quinquinquagintillion, QtQq, 168,\n56, Sexquinquagintillion, SxQq, 171,\n57, Septenquinquagintillion, SpQq, 174,\n58, Octoquinquagintillion, OcQq, 177,\n59, Novemquinquagintillion, NoQq, 180,\n60, Sexagintillion, Sx, 183,\n61, Unsexagintillion, USx, 186,\n62, Duosexagintillion, DSx, 189,\n63, Tresexagintillion, TSx, 192,\n64, Quattuorsexagintillion, QaSx, 195,\n65, Quinsexagintillion, QtSx, 198,\n66, Sexsexagintillion, SxSx, 201,\n67, Septensexagintillion, SpSx, 204,\n68, Octosexagintillion, OcSx, 207,\n69, Novemsexagintillion, NoSx, 210,\n70, Septagintillion, Sp, 213,\n71, Unseptagintillion, USp, 216,\n72, Duoseptagintillion, DSp, 219,\n73, Treseptagintillion, TSp, 222,\n74, Quattuorseptagintillion, QaSp, 225,\n75, Quinseptagintillion, QtSp, 228,\n76, Sexseptagintillion, SxSp, 231,\n77, Septenseptagintillion, SpSp, 234,\n78, Octoseptagintillion, OcSp, 237,\n79, Novemseptagintillion, NoSp, 240,\n80, Octogintillion, Og, 243,\n81, Unoctogintillion, UOg, 246,\n82, Duooctogintillion, DOg, 249,\n83, Treoctogintillion, TOg, 252,\n84, Quattuoroctogintillion, QaOg, 255,\n85, Quinoctogintillion, QtOg, 258,\n86, Sexoctogintillion, SxOg, 261,\n87, Septenoctogintillion, SpOg, 264,\n88, Octooctogintillion, OcOg, 267,\n89, Novemoctogintillion, NoOg, 270,\n90, Nonagintillion, Ng, 273,\n91, Unnonagintillion, UNg, 276,\n92, Duononagintillion, DNg, 279,\n93, Trenonagintillion, TNg, 282,\n94, Quattuornonagintillion, QaNg, 285,\n95, Quinnonagintillion, QtNg, 288,\n96, Sexnonagintillion, SxNg, 291,\n97, Septennonagintillion, SpNg, 294,\n98, Octononagintillion, OcNg, 297,\n99, Novemnonagintillion, NoNg, 300,\n100, Centillion, Ce, 303,\n"
# print(multi)
# multipliers = {"K": 3,"M": 6,"B": 9,"T": 12,"Qa": 15,"Qt": 18,"Sx": 21,"Sp": 24,"Oc": 27,"No": 30,"Dec": 33,"Undec": 36,"Duodec": 39,"Trdec": 42,"QaDec": 45,"QiDec": 48,"SxDec": 51,"SpDec": 54,"OcDec": 57,"NvDec": 60,"Vg": 63,"UVg": 66,"DVg": 69,"TVg": 72,"QaVg": 75,"QtVg": 78,"SxVg": 81,"SpVg": 84,"OcVg": 87,"NoVg": 90,"Tg": 93,"UTg": 96,"DTg": 99,"TTg": 102,"QaTg": 105,"QtTg": 108,"SxTg": 111,"SpTg": 114,"OcTg": 117,"NoTg": 120,"Qg": 123,"UQg": 126,"DQg": 129,"TQg": 132,"QaQg": 135,"QtQg": 138,"SxQg": 141,"SpQg": 144,"OcQg": 147,"NoQg": 150,"Qq": 153,"UQq": 156,"DQq": 159,"TQq": 162,"QaQq": 165,"QtQq": 168,"SxQq": 171,"SpQq": 174,"OcQq": 177,"NoQq": 180,"Sx": 183,"USx": 186,"DSx": 189,"TSx": 192,"QaSx": 195,"QtSx": 198,"SxSx": 201,"SpSx": 204,"OcSx": 207,"NoSx": 210,"Sp": 213,"USp": 216,"DSp": 219,"TSp": 222,"QaSp": 225,"QtSp": 228,"SxSp": 231,"SpSp": 234,"OcSp": 237,"NoSp": 240,"Og": 243,"UOg": 246,"DOg": 249,"TOg": 252,"QaOg": 255,"QtOg": 258,"SxOg": 261,"SpOg": 264,"OcOg": 267,"NoOg": 270,"Ng": 273,"UNg": 276,"DNg": 279,"TNg": 282,"QaNg": 285,"QtNg": 288,"SxNg": 291,"SpNg": 294,"OcNg": 297,"NoNg": 300,"Ce": 303}
# print(f"1{'0'*multipliers['K']}")


def text_to_number(text_val: str) -> int:
    multipliers = {"K": 3,"M": 6,"B": 9,"T": 12,"Qa": 15,"Qt": 18,"Sx": 21,"Sp": 24,"Oc": 27,"No": 30,"Dec": 33,"Undec": 36,"Duodec": 39,"Trdec": 42,"QaDec": 45,"QiDec": 48,"SxDec": 51,"SpDec": 54,"OcDec": 57,"NvDec": 60,"Vg": 63,"UVg": 66,"DVg": 69,"TVg": 72,"QaVg": 75,"QtVg": 78,"SxVg": 81,"SpVg": 84,"OcVg": 87,"NoVg": 90,"Tg": 93,"UTg": 96,"DTg": 99,"TTg": 102,"QaTg": 105,"QtTg": 108,"SxTg": 111,"SpTg": 114,"OcTg": 117,"NoTg": 120,"Qg": 123,"UQg": 126,"DQg": 129,"TQg": 132,"QaQg": 135,"QtQg": 138,"SxQg": 141,"SpQg": 144,"OcQg": 147,"NoQg": 150,"Qq": 153,"UQq": 156,"DQq": 159,"TQq": 162,"QaQq": 165,"QtQq": 168,"SxQq": 171,"SpQq": 174,"OcQq": 177,"NoQq": 180,"Sx": 183,"USx": 186,"DSx": 189,"TSx": 192,"QaSx": 195,"QtSx": 198,"SxSx": 201,"SpSx": 204,"OcSx": 207,"NoSx": 210,"Sp": 213,"USp": 216,"DSp": 219,"TSp": 222,"QaSp": 225,"QtSp": 228,"SxSp": 231,"SpSp": 234,"OcSp": 237,"NoSp": 240,"Og": 243,"UOg": 246,"DOg": 249,"TOg": 252,"QaOg": 255,"QtOg": 258,"SxOg": 261,"SpOg": 264,"OcOg": 267,"NoOg": 270,"Ng": 273,"UNg": 276,"DNg": 279,"TNg": 282,"QaNg": 285,"QtNg": 288,"SxNg": 291,"SpNg": 294,"OcNg": 297,"NoNg": 300,"Ce": 303}

    text_val = text_val.strip()
    i = len(text_val)
    while i > 0 and not (text_val[i - 1].isdigit() or text_val[i - 1] == "."):
        i -= 1
    number_part = float(text_val[:i]) if text_val[:i] else 0.0
    suffix_part = text_val[i:]

    try:
        valsuffix = 10 ** multipliers[suffix_part]
    except Exception as e:
        print("suffix not found.")
    
    # print(number_part * valsuffix)
    return int(number_part * valsuffix)


def plotdata(df : pd.DataFrame, string:str , color):
        data = df[df['country'] == string ].loc[:, 'country':'2050']

        series = data.drop(columns=['country']).squeeze()

        numeric_series = series.map(text_to_number)
        numeric_series.index = numeric_series.index.astype(int)

        plt.plot(numeric_series.index, numeric_series.values, color, label=string)
        print(numeric_series.values)


def main():
    """Start of the programme."""

    try:
        df = load("population_total.csv")
        print(df)
        plotdata(df,'Belgium', color='blue')
        plotdata(df,'France', color='green')

        plt.grid(True)
        plt.xlim(1790, 2060)
        plt.xticks(range(1800, 2041, 40))
        plt.yticks(
            [*range(20_000_000, 60_000_001, 20_000_000)],
            ['20M', '40M', '60M']
        )

        plt.legend(loc='lower right')
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()



    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == '__main__':
    main()