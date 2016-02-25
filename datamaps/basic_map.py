from jinja2 import Environment, PackageLoader


class BasicMap:


    def __init__(self, **kwargs):
        '''
        This is the base class for map elements. The following
        keywords are accepted:

        :keyword: **
        '''
        package_loader = PackageLoader('datamaps', 'templates')
        env = Environment(loader=package_loader)
        template_page = env.get_template('basic_map.html')

        self.template_page = template_page

    def build_html(self):
        self.html_content = self.template_page.render()
        print(self.html_content)
