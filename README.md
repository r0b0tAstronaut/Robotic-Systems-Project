The CubicSplinesPath file contains all the functions that implement the path
    planning as well as some currently unused function.

For a demo of the path planning, simply run the command:
       python cubicTester.py

Python 2 must be used. Additionally the following packages are required:
    numpy, scipy, Polygon, and matplotlib.pyplot

Several plot will appear during the execution of the program. Computation is paused
    when a plot is shown. To continue the computation simply close the plot window.

Additionally, the correction phase of the algorithm may take a minute or so
    depending on the computational resources available. If it takes longer than 3
    minutes please restart the program. The no fly zones may have been randomly
    distributed in such a way that make path planning especially difficult.