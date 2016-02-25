import unittest
from datamaps import BasicMap

class BasicMapTest(unittest.TestCase):

    def test_basic_map_builds(self):
        basic_map = BasicMap()
        basic_map.build_html()

    def test_basic_map_returns_correct_html(self):
        basic_map = BasicMap()
        basic_map.build_html()
        assert "var map = new Datamap(" \
            "{element: document.getElementById('container')});"\
            in basic_map.html_content

    def test_can_change_default_fill(self):
        basic_map = BasicMap(default_fill='rgb(23,48,101)')
        basic_map.build_html()
        assert 'rgb(23,48,101)' in basic_map.html_content


if __name__ == '__main__':
    unittest.main()