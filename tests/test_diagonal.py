import io

from module import Diagonal


def test_read_from():
    input = io.StringIO('5\n1\n1 2 3 4 5\n')
    array = Diagonal()
    array.read_from(input)
    input.seek(0)

    assert array.size == 5
    assert array.out_type == 1
    assert array.data == [1, 2, 3, 4, 5]


def test_write_to():
    test_input = io.StringIO('''\tThis is diagonal matrix
		1 0 0 0 0 
		0 2 0 0 0 
		0 0 3 0 0 
		0 0 0 4 0 
		0 0 0 0 5 
		Sum: 15
		Size: 5
		Output type: 1\n''')

    input = io.StringIO()

    array = Diagonal()
    array.size = 5
    array.out_type = 1
    array.data = [1, 2, 3, 4, 5]
    array.write_to(input)

    input.seek(0)

    assert input.read() == test_input.read()
