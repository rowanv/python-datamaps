import unittest
from datamaps import BasicMap

class BasicMapTest(unittest.TestCase):

    def test_basic_map_builds(self):
        basic_map = BasicMap()
        basic_map.build_html()

    def test_basic_map_returns_correct_html(self):
        basic_map = BasicMap()
        basic_map.build_html()
        assert "var map = new Datamap({" \
            in basic_map.html_content

    def test_can_change_default_fill(self):
        basic_map = BasicMap(default_fill='rgb(23,48,101)')
        basic_map.build_html()
        assert 'rgb(23,48,101)' in basic_map.html_content

    def test_can_change_default_map_container_element(self):
        basic_map = BasicMap()
        basic_map.build_html()
        assert "document.getElementById('container')" in \
            basic_map.html_content
        basic_map = BasicMap(element_id='map_container')
        basic_map.build_html()
        assert "document.getElementById('map_container')" \
            in basic_map.html_content


if __name__ == '__main__':
    unittest.main()