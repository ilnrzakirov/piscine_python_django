class Elem:
    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("incorrect behaviour.")

    def __init__(self, tag="div", content=None, attr={}, tag_type="double"):
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type
        self.content = []
        if not (self.check_type(content) or content is None):
            raise self.ValidationError
        if content:
            self.add_content(content)

    @staticmethod
    def check_type(content):
        if not isinstance(content, Elem) and not isinstance(content, Text) and not isinstance(content, list):
            return False

        if isinstance(content, list):
            for elem in content:
                if not isinstance(elem, Text) and not isinstance(elem, Elem):
                    return False
        return True

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if isinstance(content, list):
            self.content += [x for x in content if x != Text('')]
        elif content != Text(''):
            self.content.append(content)


    def __str__(self):

class Text(str):
    def __str__(self):
        out = super().__str__()
        out = out.replace('"', '&quot;')
        out = out.replace('<', '&lt;')
        out = out.replace('>', '&gt;')
        out = out.replace('\n', '\n<br />\n')
        return out
