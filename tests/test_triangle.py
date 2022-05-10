import io

from module import Triangle


def test_read_from():
    input = io.StringIO('3\n1\n1 2 3 4 5 6\n')
    array = Triangle()
    array.read_from(input)
    input.seek(0)

    assert array.size == 3
    assert array.out_type == 1
    assert array.data == [1, 2, 3, 4, 5, 6]


def test_write_to():
    test_input = io.StringIO('''\tThis is triangle matrix
		1 2 3 
		0 4 5 
		0 0 6 
		Sum: 21
		Size: 3
		Output type: 1\n''')

    input = io.StringIO()

    array = Triangle()
    array.size = 3
    array.out_type = 1
    array.data = [1, 2, 3, 4, 5, 6]
    array.write_to(input)

    input.seek(0)

    assert input.read() == test_input.read()
