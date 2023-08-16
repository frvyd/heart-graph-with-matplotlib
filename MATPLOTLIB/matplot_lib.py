import matplotlib.pyplot as plt
import numpy as np

# x = [5,9,1] 
# y = [1,6,7] 
# plt.plot(x,y)
# plt.show()

# plt.plot ([1,7,5,6])
# plt.show()

# plt.plot ([1,2,3,4] , [1,7,5,6] , "g")
# plt.ylabel("Y Etiketi")
# plt.xlabel("X Etiketi")
# plt.show()

# t= np.arange (0,5,0.2)
# plt.plot (t,t,"b--",t,t**2,"r*")
# plt.show()

# groups= ["A","B","C"]
# datas= [15,45,30]
# plt.figure(figsize=(9,3))
# plt.subplot(131)
# plt.bar(groups, datas)      #plt.barh(groups, datas) 
# plt.subplot(132)
# plt.scatter(groups,datas)
# plt.subplot(133)
# plt.plot(groups,datas)
# plt.suptitle("Categories")
# plt.show()

 #KALBİMİN KODU 
t= np.arange (0, 2*np.pi , 0.1)
x= np.sin(t)**3
y= 19*np.cos(t) - 8*np.cos(2*t) - 5*np.cos(3*t) - 2*np.cos(4*t)
plt.plot(x,y,"r")
plt.show()