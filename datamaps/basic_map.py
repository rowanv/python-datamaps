from jinja2 import Environment, PackageLoader


class BasicMap:


    def __init__(self, **kwargs):
        '''
        This is the base class for map elements. The following
        keywords are accepted:

        :keyword: **element_id** - default - 'container'
        :keyword: **default_fill** - default - ``None``
        :keyword: **height** - default - ``None``
        :keyword: **width** - default - ``None``
        :keyword: **projection** - default - ``None``
        :keyword: **scope** - default - ``None``
        :keyword: **responsive** - default - ``None``
        :keyword: **bubbles_config** - default - ``None``
        '''
        package_loader = PackageLoader('datamaps', 'templates')
        env = Environment(loader=package_loader)
        template_page = env.get_template('basic_map.html')

        self.template_page = template_page
        self.element_id = kwargs.get('element_id', 'container')
        self.default_fill = kwargs.get('default_fill', None)
        self.height = kwargs.get('height', None)
        self.width = kwargs.get('width', None)
        self.projection = kwargs.get('projection', None)
        self.scope = kwargs.get('scope', None)
        self.responsive = kwargs.get('responsive', None)

        # Bubbles Config
        self.bubbles_config = kwargs.get('bubbles_config', None)


    def build_html(self):
        self.html_content = self.template_page.render(map_elem=self)
