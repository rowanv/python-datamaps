from flask import Flask
from flask.ext.testing import LiveServerTestCase
from datamaps import BasicMap
from selenium import webdriver
from urllib.request import urlopen

from test_app import app

class BaseMapRenders(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8824
        return app

    def setUp(self):
        # Open File for test
        output_file = open('test_all_map_elems.html', 'w')

        html_open = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <script src="//cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script>
            <script src="//cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js"></script>
            <script src="http://datamaps.github.io/scripts/datamaps.world.min.js?v=1"></script>
        </head>
        """
        output_file.write(html_open)

        basic_map = BasicMap()
        basic_map.build_html()
        output_file.write(basic_map.html_content)

        html_close = """</body></html>"""
        output_file.write(html_close)

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.close()

    def test_index_returns_200_code(self):
        response = urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)





