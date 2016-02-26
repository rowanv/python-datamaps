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

    def test_can_change_default_projection(self):
        basic_map = BasicMap()
        basic_map.build_html()
        assert 'projection' not in basic_map.html_content

        basic_map = BasicMap(projection='equirectangular')
        basic_map.build_html()
        assert "projection: 'equirectangular'" in \
            basic_map.html_content

    def test_can_change_default_height(self):
        basic_map = BasicMap(height=400)
        basic_map.build_html()
        assert 'height: 400,' in basic_map.html_content

    def test_can_change_defalt_width(self):
        basic_map = BasicMap(width=400)
        basic_map.build_html()
        assert 'width: 400' in basic_map.html_content

    def test_can_change_default_scope(self):
        basic_map = BasicMap()
        basic_map.build_html()
        assert "scope" not in basic_map.html_content

        basic_map = BasicMap(scope='world')
        basic_map.build_html()
        assert "scope: 'world'," in basic_map.html_content

    def test_can_make_responsive(self):
        basic_map = BasicMap()
        basic_map.build_html()
        assert 'responsive' not in basic_map.html_content

        basic_map = BasicMap(responsive='true')
        basic_map.build_html()
        print(basic_map.html_content)
        assert "responsive: true" in basic_map.html_content

class BasicMapBubbleTests(unittest.TestCase):

    def test_can_add_bubbles_border_width(self):
        basic_map = BasicMap()
        basic_map.build_html()
        assert 'bubblesConfig' not in basic_map.html_content

        basic_map = BasicMap(bubbles_config={'border_width': 4})
        basic_map.build_html()
        assert 'borderWidth: 4' in basic_map.html_content

    def test_can_add_bubbles_border_opacity(self):
        basic_map = BasicMap(
            bubbles_config={'border_opacity': 2})
        basic_map.build_html()
        assert 'borderOpacity: 2' in basic_map.html_content




if __name__ == '__main__':
    unittest.main()