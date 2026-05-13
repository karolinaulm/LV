import pandas as pd
import numpy as np
mtcars=pd.read_csv('mtcars.csv')

print(mtcars.describe())
print(mtcars.iloc[0:,:2])
print(mtcars.tail(5))

print("5 auta s najvećom potrošnjom:")
print(mtcars.sort_values(by="mpg").head(5))
print("\n")

mpg_cyl8=mtcars[mtcars.cyl==8]
print("3 automobila s 8 cilindara i najmnajom potrošnjom:")
print(mpg_cyl8.sort_values(by="mpg", ascending=False).head(3))
print("\n")

mpg_cyl6=mtcars[mtcars.cyl==6]
print("Srednja potrošnja automobila sa 6 cilindara:")
print(mpg_cyl6["mpg"].mean())
print("\n")

cars4=mtcars[(mtcars.cyl==4) & (mtcars.wt>=2.0) & (mtcars.wt<=2.2)]
print("Srednja potrošnja automobila izmedu 2000 i 2200 lbs:")
print(cars4["mpg"].mean())
print("\n")

print("Manuelni:")
cars_manual=mtcars[mtcars.am==1]
print(len(cars_manual))
print("\n")

print("Automatik:")
cars_automatic=mtcars[mtcars.am==0]
print(len(cars_automatic))
print("\n")

print("Automatik sa konjskom snagom većom od 100:")
automatic_hp=mtcars[(mtcars.am==0) & (mtcars.hp>100)]
print(len(automatic_hp))
print("\n")

print("Masa automobila u kg:")
mtcars["masa_kg"]= mtcars.wt*0.453592*1000
print(mtcars[["car","masa_kg"]])
print("\n")


