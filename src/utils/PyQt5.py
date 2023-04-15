from PyQt5.QtWidgets import (
    QWidget,
    QLayout,
)


def find_all_layouts(layout):
    """
    Recursively find all layouts in a given layout.
    Returns a dictionary with layout names as keys and layout objects as values.
    """
    layouts = {}
    for i in range(layout.count()):
        item = layout.itemAt(i)
        if isinstance(item, QLayout):
            layouts[item.objectName()] = item
            # Recursively find layouts in nested layouts
            nested_layouts = find_all_layouts(item)
            layouts.update(nested_layouts)
    return layouts
