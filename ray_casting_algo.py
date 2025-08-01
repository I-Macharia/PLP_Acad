# Point in Polygon (Ray Casting Algorithm)

"""The Ray Casting algorithm determines whether a point lies inside a polygon. A horizontal “ray” is cast from the test point
if it intersects the polygon edges an odd number of times, the point is inside."""


def is_point_in_polygon(point, polygon):  # type: ignore
    """Determine if a point (x, y) lies inside a polygon defined by a list of vertices."""
    x, y = point   # type: ignore
    n = len(polygon)  # type: ignore
    inside = False

    p1x, p1y = polygon[0]   # type: ignore
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]  # type: ignore

        # Check if the point is aligned with an edge
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x): # type: ignore
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / \
                    (p2y - p1y + 1e-10) + p1x
            if p1x == p2x or x <= xinters:  # type: ignore
                inside = not inside

        p1x, p1y = p2x, p2y  # type: ignore
    return inside

 # Example polygon (a square) and test points
polygon = [(1, 1), (5, 1), (5, 5), (1, 5)]
test_points = [(3, 3), (6, 3), (5, 5), (0, 0), (1, 1), (2, 2), (4, 4), (1, 3)]

for pt in test_points:
    result = is_point_in_polygon(pt, polygon)
    print(f"Point {pt} inside polygon: {result}")
