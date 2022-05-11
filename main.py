import sys

from module import Container


def main():
    if len(sys.argv) != 3:
        print('Incorrect command line input')
        sys.exit(1)

    try:
        input_file = open(sys.argv[1], "r")
    except OSError:
        print('Opening file error')
        sys.exit(1)

    print('Start')

    container = Container(5)
    container.read_from(input_file)

    print('Filled container')

    # container.sort()
    try:
        output_file = open(sys.argv[2], "w")
    except OSError:
        print('Opening file error')
        sys.exit(1)
    finally:
        input_file.close()

    container.write_to(output_file)
    # container.write_two_dim_array_to(output_file)

    container.clear()

    print('Empty container')
    container.write_to(output_file)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
