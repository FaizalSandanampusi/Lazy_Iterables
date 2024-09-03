from convex_polygon import Polygon

class PolygonSequence:
    """
    A class to represent a sequence of convex polygons with a common circumradius.
    """

    def __init__(self, max_edges: int, circumradius: float) -> None:
        """
        Initializes a PolygonSequence with the maximum number of edges and a common circumradius.

        Parameters:
        max_edges : int
            The number of edges in the largest polygon in the sequence. Must be >= 3.
        circumradius : float
            The circumradius common to all polygons in the sequence.
        """
        if max_edges < 3:
            raise ValueError("A sequence must have at least 3 edges.")
        self.max_edges = max_edges
        self.circumradius = circumradius

    def __len__(self) -> int:
        """
        Returns the number of polygons in the sequence.
        """
        return self.max_edges - 2

    def __getitem__(self, s):
        """
        Returns a polygon or a list of polygons from the sequence.

        Parameters:
        s : int or slice
            The index or slice of indices to access.
        """
        if isinstance(s, int):
            s = s + 3
            if s < 3 or s > self.max_edges:
                raise IndexError("Index out of range.")
            return Polygon(s, self.circumradius)
        else:
            indices = range(*s.indices(self.max_edges - 2))
            return (Polygon(i + 3, self.circumradius) for i in indices)

    @property
    def max_efficiency_polygon(self) -> Polygon:
        """
        Returns the polygon with the highest area-to-perimeter ratio in the sequence.
        """
        return max(self, key=lambda p: p.area / p.perimeter)

    def __repr__(self) -> str:
        """
        Returns a string representation of the PolygonSequence object.
        """
        return f"PolygonSequence(max_edges={self.max_edges}, circumradius={self.circumradius})"
    
    def __iter__(self):
        """
        Returns an iterator object for the sequence.
        """
        return self.SequenceIter(self)
    
    class SequenceIter:
        """
        Iterator class for the PolygonSequence.
        """

        def __init__(self, poly_obj):
            """
            Initializes the iterator.

            Parameters:
            poly_obj : PolygonSequence
                The PolygonSequence object being iterated over.
            """
            self._poly_obj = poly_obj
            self._index = 0

        def __iter__(self):
            """
            Returns the iterator instance.
            """
            return self

        def __next__(self):
            """
            Returns the next polygon in the sequence.
            """
            if self._index >= len(self._poly_obj):
                raise StopIteration
            else:
                poly_item = Polygon(self._index + 3, self._poly_obj.circumradius)
                self._index += 1
                return poly_item
