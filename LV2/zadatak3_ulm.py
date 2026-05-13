import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()
img_a=img + 0.5
img_a=np.clip(img_a, 0, 1) 
plt.figure()
plt.imshow(img_a, cmap="gray")
plt.show()

img_b=np.rot90(img,k=-1) 
plt.figure()
plt.imshow(img_b, cmap="gray")
plt.title("Rotirano")
plt.show()

img_c=np.fliplr(img)
plt.figure()
plt.imshow(img_c, cmap="gray")
plt.title("Zrcaljenje")
plt.show()

img_d=img[::10,::10] 
plt.figure()
plt.imshow(img_d, cmap="gray")
plt.title("Smanjena rezolucija")
plt.show()

img_e=np.zeros_like(img)
sirina=img.shape[1]   
cetvrtina=sirina //4  
img_e[:, cetvrtina:cetvrtina*2] = img[:, cetvrtina:cetvrtina*2]
plt.figure()
plt.imshow(img_e, cmap="gray")
plt.title("Druga cetvrtina")
plt.show()
