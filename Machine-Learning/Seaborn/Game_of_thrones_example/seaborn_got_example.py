import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('battles.csv')
df.dtypes

sns.set_style("whitegrid")
example=sns.barplot(x="year",y="major_death",data=df)