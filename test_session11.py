import math
import os
from convex_polygon import Polygon
from polygon_sequence import PolygonSequence

def test_session11_readme_exists():
    """ 
        This test checks whether a README.md file exists in the current project
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_session11_readme_500_words():
    """ 
        This test checks whether the readme file contains atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session11_readme_file_for_more_than_10_hashes():
    """ 
        This code checks for formatting for readme file exisits. 
        It checks if there are hashes in the file which indicates
        usage of heading and comments in the readme file.There must 
        be atleast 10 hashes for function test to pass. 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

from convex_polygon import Polygon
from polygon_sequence import PolygonSequence
import math

def test_polygon_initialization():
    """Test Polygon initialization and error handling."""
    try:
        p = Polygon(2, 10)
        assert False, 'Creating a Polygon with 2 sides: Exception expected, not received'
    except ValueError:
        pass

def test_polygon_properties():
    
    abs_tol = 0.001
    rel_tol = 0.001
    
    #Test with 3 edges
    p = Polygon(3, 1)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == 3, f'actual: {p.count_vertices}, expected: 3'
    assert p.count_edges == 3, f'actual: {p.count_edges}, expected: 3'
    assert p.circumradius == 1, f'actual: {p.circumradius}, expected: 1'
    assert p.interior_angle == 60, f'actual: {p.interior_angle}, expected: 60'
    
    # Test Polygon with 4 edges
    p = Polygon(4, 1)
    assert p.interior_angle == 90, f'actual: {p.interior_angle}, expected: 90'
    assert math.isclose(p.area, 2, rel_tol=abs_tol, abs_tol=abs_tol), f'actual: {p.area}, expected: 2.0'
    assert math.isclose(p.edge_length, math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol), f'actual: {p.edge_length}, expected: {math.sqrt(2)}'
    assert math.isclose(p.perimeter, 4 * math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol), f'actual: {p.perimeter}, expected: {4 * math.sqrt(2)}'
    assert math.isclose(p.apothem, 0.707, rel_tol=rel_tol, abs_tol=abs_tol), f'actual: {p.apothem}, expected: 0.707'
    
    # Test Polygon with 6 edges
    p = Polygon(6, 2)
    assert math.isclose(p.edge_length, 2, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120, rel_tol=rel_tol, abs_tol=abs_tol)
    
    # Test Polygon with 12 edges
    p = Polygon(12, 3)
    assert math.isclose(p.edge_length, 1.55291, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150, rel_tol=rel_tol, abs_tol=abs_tol)

def test_polygon_comparisons():
    """Test comparisons between Polygon instances."""
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

def test_polygon_sequence_iteration():
    """Test iteration over PolygonSequence using a for loop."""
    polygons = PolygonSequence(10, 5)

    print("Testing for loop iteration:")
    for polygon in polygons:
        print(f"Polygon with {polygon.count_edges} edges: Area = {round(polygon.area,2)}, Perimeter = {round(polygon.perimeter,2)}")

def test_polygon_sequence_next():
    """Test next() and iter() for PolygonSequence."""
    polygons = PolygonSequence(10, 5)

    print("\nTesting next() with iter():")
    polygon_iter = iter(polygons)
    first_polygon = next(polygon_iter)
    assert first_polygon.count_edges == 3, f"Expected 3 edges, got {first_polygon.count_edges}"
    print(f"First polygon using next(): {first_polygon.count_edges} edges")

def test_polygon_sequence_exhaust_iterator():
    """Test exhausting the PolygonSequence iterator."""
    polygons = PolygonSequence(10, 5)

    print("\nExhausting the iterator:")
    polygon_iter = iter(polygons)
    try:
        while True:
            polygon = next(polygon_iter)
            print(f"Polygon with {polygon.count_edges} edges")
    except StopIteration:
        print("Iterator has been exhausted.")

def test_polygon_sequence_reset_iterator():
    """Test creating a new iterator instance for PolygonSequence."""
    polygons = PolygonSequence(10, 5)

    print("\nCreating a new iterator and iterating again:")
    new_iter = iter(polygons)
    for polygon in new_iter:
        print(f"Polygon with {polygon.count_edges} edges: Area = {round(polygon.area,2)}, Perimeter = {round(polygon.perimeter,2)}")

def test_polygon_sequence_exhausted_iterator():
    """Test using an exhausted iterator for PolygonSequence."""
    polygons = PolygonSequence(10, 5)

    print("\nTesting the exhausted iterator:")
    polygon_iter = iter(polygons)
    try:
        while True:
            next(polygon_iter)
    except StopIteration:
        print("Iterator has been exhausted.")

    try:
        next(polygon_iter)  # This should raise StopIteration immediately
    except StopIteration:
        print("Cannot iterate; the iterator is exhausted.")

def test_polygon_sequence_max_efficiency():
    """Test finding the maximum efficiency polygon in PolygonSequence."""
    polygons = PolygonSequence(10, 5)

    max_efficiency_polygon = polygons.max_efficiency_polygon
    assert isinstance(max_efficiency_polygon, Polygon), "Expected a Polygon instance"
    print(f"Max efficiency polygon has {max_efficiency_polygon.count_edges} edges.")
