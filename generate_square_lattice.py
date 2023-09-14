import numpy as np
import itertools

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

# Example usage:

# 3 dimensions, m=2 (so each side has length 2^2=4)
m = 2
d = 3
lattice_points = generate_lattice(m, d)
print("Lattice Points:\n", lattice_points)

