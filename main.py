import sys

from module import Container


def main():
    if len(sys.argv) != 3:
        print("Incorrect command line!\n"
              "Waited: command in_file out_file")
        sys.exit(1)

    input_file = open(sys.argv[1], "r")

    print('Start')

    container = Container(5)
    container.read_from(input_file)

    print('Filled container')

    output_file = open(sys.argv[2], "w")
    #container.write_to(output_file)
    container.write_two_dim_array_to(output_file)

    container.clear()

    print('Empty container')
    container.write_to(output_file)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
