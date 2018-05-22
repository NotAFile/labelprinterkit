"""
Labels are the Base class you derive your Labels from. A few simple Labels are
provided for you.
"""
from typing import Tuple

from PIL import Image


def _coord_add(tup1, tup2):
    """add two tuples of size two"""
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])


class Label:
    """Base class for all labels

    >>> class MyLabel(Label):
    ...     items = [
    ...         Text(), Text()
    ...     ]
    >>> l = MyLabel("text1", "text2")
    >>> printer.print(l)

    """
    items = []  # type: list

    def __init__(self, *args):
        if not self.items:
            raise ValueError(
                "A Labels 'items' attribute must contain a list of "
                "renderable objects")

        arg_it = iter(args)
        self._rendered_items = [
            [item.render(next(arg_it)) for item in line]
            for line in self.items]

    @property
    def size(self) -> Tuple[int, int]:
        width = max(sum(i.size[0] for i in line)
                    for line in self._rendered_items)
        height = sum(max(i.size[1] for i in line)
                     for line in self._rendered_items)

        return width, height

    def render(self, width=None, height=None) -> Image:
        """render the Label.

        Args:
            width: Width request
            height: Height request
        """
        size = self.size
        img = Image.new("1", size, "white")

        pos = [0, 0]

        for line in self._rendered_items:
            for item in line:
                box = (*pos, *_coord_add(item.size, pos))
                img.paste(item, box=box)
                pos[0] += item.size[0]

            pos[0] = 0
            pos[1] += max(i.size[1] for i in line)

        xdim, ydim = img.size
        print("presize", xdim, ydim, height)
        xdim = round((height / ydim) * xdim)

        print("calcsize", xdim, ydim)
        img = img.resize((xdim, height))

        img.save("output.png")
        return img

# print("".join(f"{x:08b}".replace("0", " ") for x in bytes(i)))
