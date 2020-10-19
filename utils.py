import numpy as np

def generate_perpendicular(p1, p2):
    '''
    Generates two points, with the same x-values as p1 and p2
    but which generates a line perpendicular to that bewteen
    p1 an p2 and which also crosses the midpoint (p1 + p1)/2 
    between them.
    
    Arguments:
    ----------
    p1, p2: array_like
        Lists, or one-dimensional arrays, of the coordinates
        of the two points.
    
    Returns:
    --------
    perp: array
        An 2 by 2 array where the first row is the x-values
        and the second the y-values of the two point. This
        array may then be plotted as a line bewteen the two
        points with plt.plot(*perp)
    '''
    # slope of perpendicular line
    m = -(p2[0] - p1[0]) / (p2[1] - p1[1])
    
    # intercept
    y_0 = (p1[0]**2 - p2[0]**2 + p1[1]**2 - p2[1]**2) / (2*(p1[1] - p2[1]))
    
    x_vals = np.array([p1[0], p2[0]])
    y_vals = np.array([m*p1[0], m*p2[0]]) + y_0
    
    
    return np.array([x_vals, y_vals])