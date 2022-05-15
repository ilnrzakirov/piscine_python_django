import elements
from elem import Elem, Text


class Page:
    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise Elem.ValidationError
        self.elem = elem

    def is_valid(self):
        if not (isinstance(self.elem, (elements.Html, elements.Head, elements.Body, elements.Title, elements.Meta,
                                 elements.Img, elements.Table, elements.Th, elements.Tr, elements.Td, elements.Ul,
                                 elements.Ol, elements.Li, elements.H1, elements.H2, elements.P, elements.Div,
                                 elements.Span, elements.Hr, elements.Br)) or type(self.elem) == Text):
            return False