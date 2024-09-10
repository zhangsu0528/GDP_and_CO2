import pandas as pd
import seaborn.objects as so
import matplotlib.pyplot as plt

path = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
df = pd.read_csv(path)

headdata = df.head()
df2 = df[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]


my_chart = (
    so.Plot(
        df2,
        x=df2["GDP per capita (constant 2010 US$)"],
        y=df2["Mortality rate, infant (per 1,000 live births)"],
    )
    # .add(so.Line(), so.PolyFit(order=1))
    .add(so.Dot()).label(title="GDP per capital and mortality rate")
    # .theme({**style.library["seaborn-v0_8-whitegrid"]})
)

print(my_chart)
