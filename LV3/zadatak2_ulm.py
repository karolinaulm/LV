import pandas as pd
import matplotlib.pyplot as plt
mtcars = pd.read_csv("mtcars.csv")

mtcars.groupby("cyl")["mpg"].mean().plot(kind="bar")
plt.title("Prosječna potrošnja po cilindrima")
plt.xlabel("Broj cilindra")
plt.ylabel("Mpg")
plt.show()

mtcars.boxplot(column="wt", by="cyl")
plt.title("Distribucija težine po cilindrima")
plt.xlabel("Cilindri")
plt.ylabel("Težina")
plt.show()

mtcars.boxplot(column="mpg", by="am")
plt.title("Potrošnja između manualnog i automatika")
plt.xlabel("Mjenjač")
plt.ylabel("Mpg")
plt.show()

plt.scatter(mtcars.hp, mtcars.qsec, c=mtcars.am)
plt.title("Odnos snage i ubrzanja")
plt.xlabel("Snaga")
plt.ylabel("Ubrzanje")
plt.show()
