import numpy as np
import matplotlib.pyplot as plt 

def sahovnica(vel_kvadrata, br_visina, br_sirina):
    bijeli=np.ones((vel_kvadrata, vel_kvadrata))*255 
    crni =np.zeros((vel_kvadrata, vel_kvadrata))     

redovi=[]
    for i in range(br_visina):  
red=[]
    for j in range(br_sirina):
          if(i+j)%2==0:
          red.append(bijeli)  
        else:
          red.append(crni)   
          redovi.append(np.hstack(red)) 
          slika=np.vstack(redovi)          
    return slika

img=sahovnica(50,4,5)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
