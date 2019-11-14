from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt
import pdb
pdb.set_trace()

def houneycomb(xa,xb,ya,yb,r):
    x1 = np.arange(xa,xb+r*np.sqrt(3)/2,r*np.sqrt(3))
    y1 = np.arange(ya,yb+r*3/2,r*3)
    x2 = np.arange(xa-r*np.sqrt(3)/2,xb+r*np.sqrt(3)/2,r*np.sqrt(3))
    y2 = np.arange(ya-r*3/2,yb+r*3/2,r*3)
    x1x1,y1y1 = np.meshgrid(x1,y1)
    x2x2,y2y2 = np.meshgrid(x2,y2)
    p1 = np.c_[x1x1.ravel(),y1y1.ravel()]
    p2 = np.c_[x2x2.ravel(),y2y2.ravel()]
    p = np.vstack((p1,p2))
    vor = Voronoi(p)
    d = p[p[:,0] >= xa]
    d = p[p[:,1] >= ya]
    dol = vor.vertices
    dol = dol[dol[:,0] >= xa-r*np.sqrt(3)/2]
    dol = dol[dol[:,0] <= xb+r*np.sqrt(3)/2]
    dol = dol[dol[:,1] >= ya-r*3/2]
    dol = dol[dol[:,1] >= yb+r*3/2]
    return vor,p,d

vor,p,d = houneycomb(0,12,0,12,1)
voronoi_plot_2d(vor)

plt.xlim([0,12])
plt.ylim([0,12])

plt.show()


'''
dol_p = np.vstack((p,vor.vertices))
tri = Delaunay(dol_p)

sim = dol_p[tri.simplices[Delaunay.find_simplex(tri,np.array)]]
'''



