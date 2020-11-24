import pandas as pd
import matplotlib.pyplot as mp

df = pd.read_csv('/Users/Javier/Downloads/archive 2/2019.csv')

print(df.head())

print(df.describe())

x = df["GDP per capita"]
y = df["Score"]
mp.scatter(x,y)

x2 = df["Social support"]

mp.scatter(x2,y)

x3 = df["Healthy life expectancy"]
mp.scatter(x3,y)

x4 = df["Freedom to make life choices"]
mp.scatter(x4,y)

x5 = df["Generosity"]
mp.scatter(x5,y)

x6 = df["Perceptions of corruption"]
mp.scatter(x6,y)