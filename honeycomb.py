from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange( , ,r*np.sqrt(3))
y1 = np.arange( , ,r*3)
x2 = np.arange( , ,r*np.sqrt(3))
y2 = np.arange( , ,r*3)

x1x1,y1y1 = np.meshgrid(x1,y1)
x2x2,y2y2 = np.meshgrid(x2,y2)
p1 = np.c_[x1x1.ravel(),y2y2.ravel()]
p2 = np.c_[x2x2.ravel(),y2y2.ravel()]
p = np.vstack((p1,p2))
vor = Voronoi(p)
dol_p = np.vstack((p,vor.vertices))
tri = Delaunay(dol_p)

sim = dol_p[tri.simplices[Delaunay.find_simplex(tri,'''np.array''')]]




