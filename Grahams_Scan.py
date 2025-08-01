# Convex Hull using Graham’s Scan
""" Given a set of points in the plane, the convex hull is the “rubber band” that tightly encloses all points. 
Graham’s scan sorts the points angularly around the lowest point and then constructs the hull using a stack to prune concave turns."""

import math


def orientation(p, q, r): # type: ignore
    """Return the orientation of the triplet (p, q, r).
       0 -> collinear; >0 -> counterclockwise; <0 -> clockwise."""
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) # type: ignore


def distance_sq(p, q): # type: ignore
    """Return the squared Euclidean distance between points p and q."""
    return (p[0] - q[0])**2 + (p[1] - q[1])**2 # type: ignore


def convex_hull(points): # type: ignore

    # Find the point with the lowest y (and lowest x in case of tie)
    start = min(points, key=lambda p: (p[1], p[0])) # type: ignore

    # Sort points by polar angle with the start point
    sorted_points = sorted(points, key=lambda p: (math.atan2( # type: ignore
        p[1] - start[1], p[0] - start[0]), distance_sq(start, p))) # type: ignore

    hull = []
    for p in sorted_points: # type: ignore

        # Remove points that would cause a right (clockwise) turn.
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) <= 0: # type: ignore
            hull.pop()
        hull.append(p) # type: ignore

    return hull # type: ignore

 

# Example points

points = [(0, 3), (1, 1), (2, 2), (4, 4),
          (0, 0), (1, 2), (3, 1), (3, 3)]

hull = convex_hull(points) # type: ignore

print("Convex Hull Points (in order):", hull) # type: ignore


# Explanation:

# Preprocessing: Find the lowest point as a pivot.
# Sorting: Sort rest of the points based on the angle they make with the pivot ( and by distance if they are collinear).
# Building the Hull: Iterate through sorted points. 
# Use the orientation function to keep only those points that make a counterclockwise turn, effectively “pushing out” the convex boundary.
