import sys
from module import Container


def main():
    if len(sys.argv) != 3:
        print("Incorrect command line input")
        sys.exit(1)

    # container.sort()
    try:
        with open(sys.argv[1], "r") as input_file:
            print("Start")

            container = Container(5)
            container.read_from(input_file)
    except (OSError, FileNotFoundError):
        print(f"Can't open file {sys.argv[1]}")

    print("Filled container")

    try:
        with open(sys.argv[2], "w") as output_file:
            container.write_to(output_file)
            # container.write_two_dim_array_to(output_file)
            container.check_matrices()

            container.clear()

            print("Empty container")
            container.write_to(output_file)
    except OSError:
        print(f"Can't write to file {sys.argv[2]}")


if __name__ == "__main__":
    main()
