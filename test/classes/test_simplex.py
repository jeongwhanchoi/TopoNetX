"""Test Cell class."""

import pytest

from toponetx.classes.simplex import Simplex


class TestSimplex:
    """Test the Simplex class."""

    def test_simplex_creation(self):
        """Test simplex creation."""
        s = Simplex((1,))
        assert len(s) == 1
        assert tuple(s) == (1,)
        assert s.construct_tree is True
        assert s.name == ""
        assert s._properties == {}

    def test_duplicate_nodes(self):
        """Test creation of simplex with duplicate nodes."""
        with pytest.raises(ValueError):
            Simplex((1, 1, 2))

    def test_contains(self):
        """Test the __contains__ method of the simplex."""
        s = Simplex((1, 2))
        assert 1 in s
        assert (1,) in s
        assert 3 not in s
        assert (1, 2) in s

    def test_boundary(self):
        """Test the boundary property of the simplex."""
        s = Simplex((1, 2, 3))
        boundary = s.boundary
        assert len(boundary) == 3

    def test_representation(self):
        """Test the string representation of the simplex."""
        s = Simplex((1, 2, 3))
        assert repr(s), "Simplex((1, 2, 3))"
        assert str(s) == "Nodes set: (1, 2, 3), attrs: {}"

    def test__contains__(self):
        """Test the __contains__ method of the simplex."""
        s = Simplex([1, 2, 3])
        assert (1, 2) in s
        assert (1, 3) in s
        assert frozenset((1, 3)) in s
        assert (1, 3, 4, 5, 6, 7) not in s
        assert not (1, 3, 4, 5, 6, 7) in s

    def test_construct_tree(self):
        """Test the construct_tree property of the simplex."""
        s = Simplex((1, 2, 3), construct_tree=True)
        assert len(s.boundary) == 3

        s = Simplex((1, 2, 3), construct_tree=False)
        assert len(s.boundary) == 3

    def test_getting_and_setting_items(self):
        """Test getting and setting items in the simplex."""
        s = Simplex((1, 2, 3), construct_tree=True)
        s["weight"] = 1
        assert s["weight"] == 1

    def test_faces(self):
        """Test getting faces from simplex."""
        s = Simplex((1, 2, 3), constuct_tree=False)
        faces = s.faces
        assert len(faces) == 7

        s = Simplex((1, 2, 3), constuct_tree=True)
        faces = s.faces
        assert len(faces) == 7

    def test_clone(self):
        """Test clone method."""
        s = Simplex((1, 2, 3))
        s1 = s.clone()

        assert 1 in s1
        assert 2 in s1
        assert 3 in s1
        assert (1, 2) in s1
        assert (2, 3) in s1
        assert (1, 3) in s1
        assert (1, 2, 3) in s1
