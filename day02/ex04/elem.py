class Elem:
    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("incorrect behaviour.")

    def __init__(self, tag="div", attr={}, content=None, tag_type="double"):
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type
        self.content = []
        if content:
            self.add_content(content)
        elif content is not None and not isinstance(content, Text):
            raise self.ValidationError

    @staticmethod
    def check_type(content) -> bool:
        """
        Проверка контента на принадлежность инстансу класса Elem, Text
        :param content: Elem, Text, None
        :return: boolean
        """
        if not isinstance(content, Elem) and not isinstance(content, Text) and not isinstance(content, list):
            return False

        if isinstance(content, list):
            for elem in content:
                if not isinstance(elem, Text) and not isinstance(elem, Elem):
                    return False
        return True

    def add_content(self, content):
        """
        Добавление нового контента в список
        :param content: Elem, Text, None
        """
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if isinstance(content, list):
            self.content += [x for x in content if x != Text('')]
        elif content != Text(''):
            self.content.append(content)

    def get_attr(self):
        ret = ""
        for x in sorted(self.attr.items()):
            ret += " " + str(x[0]) + "=" + str(x[1])
        return ret

    def get_content(self):
        if not self.content:
            return ""
        ret = "\n"
        for x in self.content:
            ret += " " + str(x).replace("\n", "\n ") + "\n"
        return ret

    def __str__(self):
        if self.tag_type == "double":
            return f"<{str(self.tag)}>{self.get_attr()}{self.get_content()}</{self.tag}>"
        elif self.tag_type == "simple":
            return f"<{str(self.tag)}{self.get_attr()}></{self.get_attr()}>"


class Text(str):
    def __str__(self):
        """
        Замена ковычек и угловых скобок на специальные символы
        :return: str
        """
        out = super().__str__()
        out = out.replace('"', '&quot;')
        out = out.replace('<', '&lt;')
        out = out.replace('>', '&gt;')
        out = out.replace('\n', '\n<br />\n')
        return out


print(Elem())
print(Elem('div', {}, None, 'double'))
print(Elem(tag='body', attr={}, content=Elem(), tag_type='double'))
