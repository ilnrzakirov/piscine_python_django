from elem import Elem


class HTML(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')
