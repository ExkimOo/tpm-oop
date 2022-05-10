import io

from module import TwoDimArray


def test_read_from():
    input = io.StringIO('1\n1\n5\n')
    array = TwoDimArray()
    array.read_from(input)
    input.seek(0)

    assert array.size == 1
    assert array.out_type == 1
    assert array.data == [[5]]

# def test_write_to():
#     test_input = io.StringIO('''\tThis is two-dimensional array
# 		1 2
# 		3 4
# 		Sum: 10
# 		Size: 2
# 		Output type: 1\n''')
#
#     input = io.StringIO()
#
#     array = TwoDimArray()
#     array.size = 2
#     array.out_type = 1
#     array.data = [[1, 2], [3, 4]]
#     array.write_to(input)
#
#     input.seek(0)
#
#     assert input.read() == test_input.read()
