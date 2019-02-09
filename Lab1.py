"""
Course CS2301 MW 1:30-2:50pm
Instructor:Fuentes, Olac
Tovar, Brianna
Date of last modification: 2/8/2019
1st Lab
This lab is over the drawing of figures using
recursion and simple math.
"""
"""
Created on Wed Feb  3 09:16:22 2019

@author: ItsBri
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#creating circle/basis for lab
def circle(center, rad):
    n = int(4 * rad * math.pi) #circle math
    t = np.linspace(0, 6.3, n)
    x = center[0] + rad * np.sin(t)
    y = center[1] + rad * np.cos(t)
    return x, y

#creating circles overlapping
def draw_circles(ax, n, center, radius, w):
    if n > 0:
        x, y = circle(center, radius)
        ax.plot(x + radius, y, color='k')
        draw_circles(ax, n-1, center, radius * w, w)

#Figure A for circles      
plt.close("all")
fig, ax = plt.subplots()
draw_circles(ax, 50, [100, 0],100, .7)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
#figure B for circles
plt.close("all")
fig, ax = plt.subplots()
draw_circles(ax, 50, [100, 0],100, .8)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
#figure Cfor circles 
plt.close("all")
fig, ax = plt.subplots()
draw_circles(ax, 50, [100, 0],100, .9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()



#exercise for squares
def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1] #points
        q = p*w + p[i1]*(1-w) #square math
        ax.plot(p[:,0],p[:,1],color='k') #plotting onto grid
        draw_squares(ax,n-1,q,w)

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,15,p,.8)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

  #another square exercise      
def draw_squares_loops(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=1, color='k') #loop for creating another square
        q=np.zeros((1,2))
        for i in range(1):
            for j in range(2):
                q[i,j]=w*p[i,j]+(1-w)*p[(i+1)%4,j]
        draw_squares_loops(ax,n-1,q,w)

#error after changing numbers, idk why
plt.close("all")
orig_size=1000
p=np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
#This is the perimeteres of the graph we are using for the figures
fig, ax=plt.subplots()
draw_squares_loops(ax,5,p,.5)
#using the numbers in class for each figure having a different decimal
ax.set_aspect(1.0)
plt.show()
fig.savefig('squares2.png')