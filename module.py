import sys
from enum import Enum


class Container:
    def __init__(self, capacity):
        self.size = 0
        self.data = []
        self.__capacity = capacity

    def push_back(self, elem):
        if self.size + 1 <= self.__capacity:
            self.size += 1
            self.data.append(elem)
        else:
            raise OverflowError

    def read_from(self, stream):
        counter = 0
        while line := stream.readline():
            counter += 1
            print(f"Try to read {counter}", end=": ")

            item = Matrix.create_from(stream, line)
            if item:
                print("OK")
                self.push_back(item)

    def write_to(self, stream):
        stream.write(f"Container contains {self.size} elements\n")

        if self.data:
            for item in self.data:
                item.write_to(stream)

    def clear(self):
        self.size = 0
        self.__capacity = None
        self.data = None

    def write_two_dim_array_to(self, stream):
        stream.write("Only two dimensional arrays\n")

        for item in self.data:
            item.write_two_dim_array_to(stream)

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.data)

    def sort(self):
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                if self.data[i].compare(self.data[j]):
                    self.data[i], self.data[j] = self.data[j], self.data[i]

    def __iter__(self):
        return self.data

    def check_matrices(self):
        matrices_1 = [item for item in self.data]
        matrices_2 = matrices_1.copy()

        for matrix_1 in matrices_1:
            for matrix_2 in matrices_2:
                Matrix.check_matrices(matrix_1, matrix_2)


class Matrix:
    data: list or None

    def __init__(self):
        self.size = 0
        self.out_type = 0

    def read_from(self, stream):
        try:
            self.size = int(stream.readline().rstrip("\n"))
        except ValueError:
            print("Reading size error")
            return

        try:
            self.out_type = int(stream.readline().rstrip("\n"))
        except ValueError:
            print("Reading out type error")
            return

    def write_to(self, stream):
        stream.write(f"\t\tSize: {self.size}\n")
        stream.write(f"\t\tOutput type: {self.out_type}\n")

    def sum(self):
        try:
            s = 0
            for item in self.data:
                if isinstance(item, int):
                    s += item
                else:
                    s += sum(item)
            return s
        except (TypeError, RecursionError):
            print("Sum calculation error")

    def compare(self, other):
        return self.sum() < other.sum()

    @staticmethod
    def create_from(stream, line):
        try:
            k = int(line)
            if k == 1:
                matrix = TwoDimArray()
            elif k == 2:
                matrix = Diagonal()
            elif k == 3:
                matrix = Triangle()
            else:
                print("Wrong type")
                return
            matrix.read_from(stream)
            return matrix
        except ValueError:
            print("Conversion to int error")

    def write_two_dim_array_to(self, stream):
        pass

    @staticmethod
    def check_matrices(matrix_1, matrix_2):
        match matrix_1, matrix_2:
            case TwoDimArray(), TwoDimArray():
                print("Matrices are the same type: TwoDimArray and TwoDimArray")

            case TwoDimArray(), Diagonal():
                print("Matrices are different type: TwoDimArray and Diagonal")

            case TwoDimArray(), Triangle():
                print("Matrices are different type: TwoDimArray and Triangle")

            case Diagonal(), TwoDimArray():
                print("Matrices are different type: Diagonal and TwoDimArray")

            case Diagonal(), Diagonal():
                print("Matrices are the same type: Diagonal and Diagonal")

            case Diagonal(), Triangle():
                print("Matrices are different type: Diagonal and Triangle")

            case Triangle(), TwoDimArray():
                print("Matrices are different type: Triangle and TwoDimArray")

            case Triangle(), Diagonal():
                print("Matrices are different type: Triangle and Diagonal")

            case Triangle(), Triangle():
                print("Matrices are the same type: Triangle and TwoDimArray")

            case _:
                print('Unknown type')
                return

        print(f"First: {matrix_1}, second: {matrix_2}")
        print()


class TwoDimArray(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        super().read_from(stream)
        for _ in range(self.size):
            line = stream.readline().rstrip("\n")
            try:
                self.data.append(list(map(int, line.split())))
            except ValueError:
                print(f"Error parsing line: {line}")

    def write_to(self, stream):
        stream.write("\tThis is two-dimensional array\n")
        if self.out_type == 1:
            stream.write("\t\t")
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f"{self.data[i][j]} ")
                stream.write("\n\t\t")

        elif self.out_type == 2:
            # stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f"{self.data[j][i]} ")
                stream.write("\n\t\t")

        elif self.out_type == 3:
            # stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f"{self.data[i][j]} ")
            # stream.write('\n\t\t')
        else:
            stream.write("\tError matrix output type\n")

        stream.write(f"Sum: {self.sum()}\n")
        super().write_to(stream)

    def write_two_dim_array_to(self, stream):
        self.write_to(stream)


class Diagonal(Matrix):
    def __init__(self):
        super().__init__()
        self.data = None

    def read_from(self, stream):
        try:
            super().read_from(stream)
            self.data = list(
                map(int, stream.readline().rstrip("\n").split())
            )
        except ValueError:
            print("Reading diagonal matrix from file error")
            return

    def write_to(self, stream):
        stream.write("\tThis is diagonal matrix\n")

        if self.out_type == 1 or self.out_type == 2:
            stream.write("\t\t")
            for i in range(self.size):
                for j in range(self.size):
                    stream.write("{} ".format(self.data[i] if i == j else 0))
                stream.write("\n\t\t")

        elif self.out_type == 3:
            stream.write("\t\t")
            for i in range(self.size):
                for j in range(self.size):
                    stream.write("{} ".format(self.data[i] if i == j else 0))
            # stream.write('\n\t\t')
        else:
            stream.write("\tError matrix output type\n")

        stream.write(f"Sum: {self.sum()}\n")
        super().write_to(stream)


class Triangle(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        try:
            super().read_from(stream)
            self.data = list(
                map(int, stream.readline().rstrip("\n").split())
            )
        except ValueError:
            print("Reading triangle matrix from file error")

    def write_to(self, stream):
        stream.write("\tThis is triangle matrix\n")

        if self.out_type == 1 or self.out_type == 2:
            stream.write("\t\t")
            index = 0
            for i in range(self.size):
                for j in range(self.size):
                    if j >= i:
                        stream.write(str(self.data[index]) + " ")
                        index += 1
                    else:
                        stream.write("0 ")
                stream.write("\n\t\t")

        elif self.out_type == 3:
            stream.write("\t\t")
            for i in range(self.size):
                for j in range(self.size):
                    stream.write("{} ".format(self.data[i] if i == j else 0))
            # stream.write('\n\t\t')
        else:
            stream.write("\tError matrix output type\n")

        stream.write(f"Sum: {self.sum()}\n")
        super().write_to(stream)
