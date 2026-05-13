import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
mpg=data[ : ,0]
hp=data[ : ,3]
wt=data[ : ,5]
cyl=data[ : ,1]
plt.scatter(mpg, hp, s=wt*15, c=wt)
plt.xlabel('Hp')
plt.ylabel('Mpg')
plt.title('Ovisnost mpg, hp i wt')
plt.grid(True)
plt.show()

print('Mpg vrijednosti')
print('Min mpg:') 
print(mpg.min())
print('Max mpg:')
print(mpg.max())
print('Srednja vrijednost mpg:')
print(mpg.mean())
print('\n\n')
print('Mpg vrijednosti za mpg_cyl6')
mpg_cyl6=mpg[cyl==6]
print('Min mpg_cyl6:')
print(mpg_cyl6.min())
print('Max mpg_cyl6:')
print(mpg_cyl6.max())
print('Srednja vrijednost mpg_cyl6:')
print(mpg_cyl6.mean())
