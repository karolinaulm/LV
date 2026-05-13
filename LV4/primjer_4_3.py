import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cars_processed.csv')
print(df.info())
print("\n")
print("Automobili s najvećom kilometražom:")
print(df.loc[df["km_driven"].idxmax(),["name","km_driven"]])
print("Automobili s najmanjom kilometražom:")
print(df.loc[df["km_driven"].idxmin(), ["name", "km_driven"]])
print("\n")

sns.pairplot(df, hue='fuel')
sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

tabcorr = df.corr(numeric_only=True)
sns.heatmap(tabcorr, annot=True, linewidths=2, cmap='coolwarm')

print("\n")
print(len(df))
print("\n")

print(df.dtypes)
print("\n")

print("Najskuplji automobil:")
print(df.loc[df.selling_price.idxmax()])
print("\n")

print("Najjeftiniji automobil:")
print(df.loc[df.selling_price.idxmin()])
print("\n")

print("Broj automobila proizvedeno u 2012. godini:", len(df[df['year']==2012]))
print("\n")

print("Najčešći broj sjedala:",df['seats'].mode()[0])
print("\n")

print("Disel motori:",round(df[df["fuel"]=="Diesel"]["km_driven"].mean(),2))
print("\n")

print("Benzin motori:",round(df[df["fuel"]=="Petrol"]["km_driven"].mean(),2))
print("\n")
plt.show()
