import elements
from elem import Elem


class Page:
    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise Elem.ValidationError
        self.elem = elem

