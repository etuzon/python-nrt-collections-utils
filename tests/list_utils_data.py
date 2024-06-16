

compare_lists_data = [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2, 3], [1, 2, 3, 4], False),
    ([1, 2, 3], [1, 2], False),
    ([1, 2, 3], [1, 2, 3, 3], False),
    ([1, 3, 2], [1, 2, 3], True),
    ([1, {'a': 'b'}, 2], [1, 2, {'a': 'b'}], True),
    ([1, 2, 3], [1, 2, '3'], False),
    ([1, 2, 3], [1, 2, 3, '3'], False),
    ([1, 1, 1], [1, 2, 3], False),
    ([1, 2, 3], [1, 1, 1], False),
    ([], [], True),
    ([1], [], False),
    ([], [None], False),
    ([False], [False], True),
    ([1, None, 2], [1, 2, None], True)
]
