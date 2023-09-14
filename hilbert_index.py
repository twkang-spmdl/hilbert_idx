import numpy as np
import math
import itertools
from hilbertcurve.hilbertcurve import HilbertCurve

def generate_lattice(m, d):
    # The side length of the lattice along each dimension
    side_length = 2 ** m
    
    # Number of points in the lattice
    num_points = side_length ** d
    
    # Initialize output array
    output = np.zeros((num_points, d))
    
    # Generate coordinates for the lattice points
    index = 0
    for point in itertools.product(range(side_length), repeat=d):
        output[index] = point
        index += 1
    
    return output

# Lattice size is 2^m
m = 3
# Dimension of the system
d = 2
points = generate_lattice(m,d)
# the number of iterations to construc Hilbert curves
p = round(math.pow(points.shape[0], 1/d))
# Considering the n-dimensional hypercube of side length 2^p
num_points = (2**m)**d
hilbert_curve = HilbertCurve(p, d)
scan_idx = hilbert_curve.distances_from_points(points, match_type=False)
# print(scan_idx)

# print(type(scan_idx))

# Scan idx for MATLAB
mat_scan_idx = [i+1 for i in scan_idx]
mat_scan_idx = np.array(mat_scan_idx)
print(mat_scan_idx.reshape(d**m, d**m))

from scipy.io import savemat
savemat('indMat.mat', {'indMat': mat_scan_idx})

test_array = np.zeros((5, 5))
savemat('zeromat.mat', {'zeromat': test_array})

# Sort original position using hilbert indices(distances)
sort_idx = np.argsort(scan_idx)
position_sorted = points[sort_idx]
# print(position_sorted)
