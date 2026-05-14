from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from funkcija_6_1 import generate_data
X = generate_data(500, 1) 

inertia = [] 
K_range = range(1, 21)  

for k in K_range:
    k_means = KMeans(n_clusters=k, n_init=10)
    k_means.fit(X)
    inertia.append(k_means.inertia_) 

plt.plot(K_range, inertia, marker='o')
plt.xlabel("Broj klastera")
plt.ylabel("Vrijednost kriterijske funkcije")
plt.title("Lakat metoda")
plt.show()
