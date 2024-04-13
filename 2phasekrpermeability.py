import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#create variables
#Sw= water saturation
#Swir= the irreducible water saturation
#Snw= saturation of nonwetting phase
#Krw= relative permeability to water
#Kro= relative permeability to oil

Sw = np.linspace(0,1,100)

Swir = 0.20

Snw = (Sw - Swir)/(1-Swir)

Krw = Snw**4

Kro = ((1 - Snw)**2)*(1 - Snw**2)


plt.plot(Sw,Krw,Sw,Kro,label="Krel-Oil(Non-Wetting P.)",lw=3)
plt.plot(Sw,Krw,Sw,Kro,label="Krel-water(Wetting P.)",lw=3)
plt.title("Relative-Permeability by Corey's Model")
plt.xlabel('Sw')
plt.ylabel('Krel(o,w)')
plt.grid()
plt.legend()