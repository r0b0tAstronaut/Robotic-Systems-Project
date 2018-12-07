from __future__ import division
import sys
import numpy as np
import scipy
import copy
import Polygon
import random
from scipy.interpolate import CubicSpline, interp1d
from scipy.optimize import minimize
from scipy import integrate
from scipy.misc import derivative
import matplotlib.pyplot as plt
from matplotlib.pyplot import Circle
from matplotlib.collections import PatchCollection

# Don't import this way in final program. Only for testing
from cubicSplinesPath import *

def main():
    # Initialize Figure
    fig, ax = plt.subplots()
    plt.gca().set_xlim([0,  1300])
    plt.gca().set_ylim([0, 1300])

    # Initialize 'given' waypoints
    wpxInit = [746.90, 1019.25, 390.52, 78.60, 204.4, 673.6]
    wpyInit = [1108.4, 1024.40, 155.47, 391.6, 612.7, 338.4]
    wpzInit = [100, 100, 100, 100, 100, 100, 100]

    # Comp Boundary converted to XY
    poly = [(609.9915651830946, 644.454456932276),
            (655.4769561099155, 1238.9138134970472),
            (899.4365305847842, 1268.1819761471047),
            (1240.810387266854, 1124.454562201312),
            (976.1887502964521, 788.4094397923109),
            (1029.310174576658, 466.5050901843899),
            (1188.824911231627, 309.8511306983688),
            (1002.0957697243854, 0.0036295812471155995),
            (421.55939798675325, 28.420887104681732),
            (0.03993415704199533, 366.0542881303085),
            (175.83977103766549, 764.1079686968526),
            (477.5319123645307, 629.0467535497892)]

    # Plot the waypoints
    plt.plot(wpxInit, wpyInit, 'x', label = 'data', color = (0,0,0,1))

    # Plot the competition boundary
    xVals = []
    yVals = []
            
    for pt in poly:
        x, y = pt

        xVals.append(x)
        yVals.append(y)
    
    x, y = poly[0]
    xVals.append(x)
    yVals.append(y)
    plt.plot(xVals, yVals)
    
    # Generate the no fly zones
    circles = makeRandomCircles(30, wpxInit, wpyInit, poly)

    # Plot the no fly zones
    ax = plt.gca()
    for circle in circles:
        circle = Circle(circle[0], circle[1], facecolor='r')
        ax.add_patch(circle)

    # Show the plot of the competition elements
    plt.show()

    # Initialize parameter spacing as constant
    t = np.arange(len(wpxInit))

    # Create initial cubic spline
    csx = CubicSpline(t, wpxInit)
    csy = CubicSpline(t, wpyInit)

    # Plot parametric cubic splines
    s = 0.01
    tSpace = np.arange(t[0], t[len(t)-1] + s, s)
    plt.plot(csx(tSpace), csy(tSpace))

    # Plot the competition elements again
    plt.plot(wpxInit, wpyInit, 'x', label = 'data', color = (0,0,0,1))
    plt.plot(xVals, yVals)

    ax = plt.gca()
    for circle in circles:
        circle = Circle(circle[0], circle[1], facecolor='r')
        ax.add_patch(circle)

    # Show the path with the first draft of the cubic spline path
    plt.show()

    # Fix the intersections with the polygon
    wpxNew, wpyNew, t = fixPolygonIntersections(wpxInit, wpyInit, t.tolist(), poly, circles)

    # Generate the path with the additional intermediate waypoints
    csx = CubicSpline(t, wpxNew)
    csy = CubicSpline(t, wpyNew)

    # Plot competition elements
    ax = plt.gca()
    for circle in circles:
        circle = Circle(circle[0], circle[1], facecolor='r')
        ax.add_patch(circle)

    # Plot the new path
    s = 0.01
    tSpace = np.arange(t[0], t[len(t)-1] + s, s)
    plt.plot(csx(tSpace), csy(tSpace))

    plt.plot(wpxNew, wpyNew, 'x', label = 'data', color = (0,0,0,1))
    plt.plot(xVals, yVals)

    plt.show()


if __name__ == "__main__":
    main()