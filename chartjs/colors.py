COLORS = [
    (202, 201, 197, 1.0),  # Light gray
    (171, 9, 0, 1.0),  # Red
    (166, 78, 46, 1.0),  # Light orange
    (255, 190, 67, 1.0),  # Yellow
    (163, 191, 63, 1.0),  # Light green
    (122, 159, 191, 1.0),  # Light blue
    (140, 5, 84, 1.0),  # Pink
    (166, 133, 93, 1.0),  # Light brown
    (75, 64, 191, 1.0),  # Red blue
    (237, 124, 60, 1.0),  # orange
]


def next_color(color_list=COLORS):
    """Create a different color from a base color list.

    >>> color_list = (
    ...    (122, 159, 191),  # Light blue
    ...    (202, 201, 197),  # Light gray,
    ... )
    >>> g = next_color(color_list)
    >>> next(g)
    [122, 159, 191]
    >>> next(g)
    [202, 201, 197]
    >>> next(g)
    [63, 100, 132]
    >>> next(g)
    [143, 142, 138]
    >>> next(g)
    [4, 41, 73]
    >>> next(g)
    [84, 83, 79]
    """
    step = 0
    while True:
        for color in color_list:
            yield list(map(lambda base: (base + step) % 256, color))
        step += 197
