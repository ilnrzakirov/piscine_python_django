from elem import Elem


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content, tag_type='double')

class Meta(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')