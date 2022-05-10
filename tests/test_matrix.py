import io

import pytest

from module import Matrix, TwoDimArray, Diagonal, Triangle


def test_read_from():
    matrix = Matrix()
    input = io.StringIO('1\n2\n')
    matrix.read_from(input)
    input.seek(0)

    assert matrix.size == int(input.read(1))


def test_write_to():
    output = io.StringIO()
    matrix = Matrix()
    matrix.size = 2
    matrix.out_type = 2
    matrix.write_to(output)

    output.seek(0)

    test_str = f'\t\tSize: 2\n' \
               f'\t\tOutput type: 2\n'

    assert output.read() == test_str


@pytest.mark.parametrize('input, obj', [
    (io.StringIO('1\n2\n1\n1 2\n3 4\n'), TwoDimArray),
    (io.StringIO('2\n5\n1\n1 2 3 4 5\n'), Diagonal),
    (io.StringIO('3\n3\n1\n1 2 3 4 5 6\n'), Triangle),
])
def test_create_from(input, obj):
    line = input.readline()
    matrix = Matrix.create_from(input, line)
    assert isinstance(matrix, obj)


@pytest.mark.parametrize('input, obj, sum', [
    (io.StringIO('1\n2\n1\n1 2\n3 4\n'), TwoDimArray, 10),
    (io.StringIO('2\n5\n1\n1 2 3 4 5\n'), Diagonal, 15),
    (io.StringIO('3\n3\n1\n1 2 3 4 5 6\n'), Triangle, 21),
])
def test_sum(input, obj, sum):
    line = input.readline()
    matrix = Matrix.create_from(input, line)
    assert matrix.sum() == sum
