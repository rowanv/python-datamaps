# Run from root: python3 -m datamaps.tests.qunit.create_test_map_elems

from datamaps import BasicMap


def write_map_elem_file(file_name, map_elem):
    root_app_dir = 'datamaps/tests/test_app/templates/'

    output_file = open(root_app_dir + file_name, 'w')
    map_elem.build_html()
    output_file.write(map_elem.html_content)


def main():
    write_map_elem_file('test_all_map_elems.html',
     BasicMap())
    write_map_elem_file('test_color_change.html',
        BasicMap(default_fill='rgb(23,48,101)',
            element_id='map_container'))

if __name__ == '__main__':
    main()




