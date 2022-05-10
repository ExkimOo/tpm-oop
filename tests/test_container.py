from module import Container


def test_clear():
    container = Container(10)
    for i in range(10):
        container.push_back(i)

    container.clear()

    assert len(container) == 0


def test_push_back():
    container = Container(5)
    container.push_back('123')
    container.push_back((1, 2, 3))
    container.push_back([1, 2, 3])

    array = [item for item in container.data]

    assert ['123', (1, 2, 3), [1, 2, 3]] == array


def test_len():
    container = Container(10)
    for i in range(10):
        container.push_back(i)

    assert len(container) == 10


def test_read_from():
    container = Container(10)

    with open('tests/input.txt', 'r') as file:
        container.read_from(file)

    assert len(container) != 0


def test_write_to():
    container = Container(10)

    with open('tests/input.txt', 'r') as file:
        container.read_from(file)

    with open('tests/output.txt', 'w') as file:
        container.write_to(file)

    file_obs = open("tests/output.txt", "r")
    file_exp = open("tests/output_test_write.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()


def test_sort():
    container = Container(10)

    with open('tests/input.txt', 'r') as file:
        container.read_from(file)

    container.sort()
    with open("tests/output_test_sort.txt", "w") as file:
        container.write_to(file)

    file_obs = open("tests/output_sort.txt", "r")
    file_exp = open("tests/output_test_sort.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()


def test_write_two_dim_array_to():
    container = Container(10)

    with open('tests/input.txt', 'r') as file:
        container.read_from(file)

    with open("tests/output_test_write_two_dim_array_to.txt", "w") as file:
        container.write_to(file)

    file_obs = open("tests/output_write_two_dim_array.txt", "r")
    file_exp = open("tests/output_test_write_two_dim_array_to.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()
