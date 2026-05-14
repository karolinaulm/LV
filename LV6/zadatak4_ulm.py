import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

img = mpimg.imread('example_grayscale.png')

if len(img.shape) == 3:
    img = img.mean(axis=2)

X = img.reshape(-1, 1)

kmeans = KMeans(n_clusters=10, n_init=10)
kmeans.fit(X)

values = kmeans.cluster_centers_.squeeze()
labels = kmeans.labels_

img_compressed = values[labels]
img_compressed = img_compressed.reshape(img.shape)

plt.figure()
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.figure()
plt.imshow(img_compressed, cmap='gray')
plt.title("Kvantiziran")
plt.show()

num_pixels = img.shape[0] * img.shape[1]
original_bits = num_pixels * 8
K = 10
bits_per_pixel = np.ceil(np.log2(K))  

compressed_bits = num_pixels * bits_per_pixel
compressed_bits += K * 8 
compression_ratio = original_bits / compressed_bits

print(f"Original veličina: {original_bits}")
print(f"Kompresirana veličina: {compressed_bits}")
print(f"Kompresijski omjer: {compression_ratio:.2f}x")
