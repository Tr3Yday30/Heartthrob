import csv
import pandas as pd
df = pd.read_csv("C:/Users/prakb/OneDrive/desktop/Heartthrob/data/NCHS_-_Leading_Causes_of_Death__United_States.csv")
#print(df)
dfint = df['Year'] = df['Year'].astype(str)
df2012 = dfint.loc[df['Year'].str.contains("2012", case=False)]
print(df2012)
df2013 = dfint.loc[df['Year'].str.contains("2013", case=False)]
print(df2013)