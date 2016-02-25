# Run from root: python3 -m datamaps.tests.qunit.create_test_map_elems

from datamaps import BasicMap


def write_map_elem_file(file_name, map_elem):
    root_app_dir = 'datamaps/tests/test_app/templates/'

    html_open = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <script src="//cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script>
                <script src="//cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js"></script>
                <script src="http://datamaps.github.io/scripts/datamaps.world.min.js?v=1"></script>
            </head>
            """
    html_close = """</body></html>"""

    output_file = open(root_app_dir + file_name, 'w')
    output_file.write(html_open)
    map_elem.build_html()
    output_file.write(map_elem.html_content)

    output_file.write(html_close)

def main():
    write_map_elem_file('test_all_map_elems.html',
     BasicMap())
    write_map_elem_file('test_color_change.html',
        BasicMap(default_fill='rgb(23,48,101)'))

if __name__ == '__main__':
    main()




