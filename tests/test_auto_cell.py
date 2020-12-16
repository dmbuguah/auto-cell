import unittest

from awe_pro import auto_cell

def test_get_programming_language():
    """Test get programming language, pl exists."""
    pl = auto_cell.get_programming_language()
    assert pl in ['Python', 'Java', 'JavaScript', 'Ruby']


def test_get_programming_language_pl_does_not_exist():
    """Test get programming language, pl does not exists."""
    pl = auto_cell.get_programming_language()
    assert pl not in ['Go']
