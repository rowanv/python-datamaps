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


if __name__ == '__main__':
    unittest.main()