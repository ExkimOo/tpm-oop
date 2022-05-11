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
        while line := stream.readline():
            item = Matrix.create_from(stream, line)
            self.push_back(item)

    def write_to(self, stream):
        stream.write(f"Container contains {self.size} elements\n")

        if self.data != None:
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


class Matrix:
    def __init__(self):
        self.size = 0
        self.out_type = 0

    def read_from(self, stream):
        try:
            self.size = int(stream.readline().rstrip("\n"))
        except Exception:
            print("Reading size error")
            stream.close()
            sys.exit(1)

        try:
            self.out_type = int(stream.readline().rstrip("\n"))
        except Exception:
            print("Reading out type error")
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f"\t\tSize: {self.size}\n")
            stream.write(f"\t\tOutput type: {self.out_type}\n")
        except Exception:
            print("Writing to file error")
            stream.close()
            sys.exit(1)

    def sum(self):
        try:
            s = 0
            for item in self.data:
                if isinstance(item, int):
                    s += item
                else:
                    s += sum(item)
            return s
        except Exception:
            print("Sum calculation error")

    def compare(self, other):
        return self.sum() < other.sum()

    @staticmethod
    def create_from(stream, line):
        try:
            k = int(line)
        except Exception:
            print("Conversion to int error")
            stream.close()
            sys.exit(1)

        if k == 1:
            matrix = TwoDimArray()
        elif k == 2:
            matrix = Diagonal()
        elif k == 3:
            matrix = Triangle()
        else:
            stream.close()
            raise Exception("Error type")

        matrix.read_from(stream)
        return matrix

    def write_two_dim_array_to(self, stream):
        pass


class TwoDimArray(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        super().read_from(stream)
        try:
            for i in range(self.size):
                line = stream.readline().rstrip("\n")
                self.data.append(list(map(lambda x: int(x), line.split())))
        except Exception:
            print("Reading two-dimensional array from file error")
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
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
        except Exception:
            print("Writing two-dimensional array to file error")
            stream.close()
            sys.exit(1)

    def write_two_dim_array_to(self, stream):
        try:
            self.write_to(stream)
        except Exception:
            print("Writing two-dimensional array to file error")
            stream.close()
            sys.exit(1)


class Diagonal(Matrix):
    def __init__(self):
        super().__init__()
        self.data = None

    def read_from(self, stream):
        try:
            super().read_from(stream)
            self.data = list(
                map(lambda x: int(x), stream.readline().rstrip("\n").split())
            )
        except Exception:
            print("Reading diagonal matrix from file error")
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
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
        except Exception:
            print("Writing diagonal matrix to file error")
            stream.close()
            sys.exit(1)


class Triangle(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        try:
            super().read_from(stream)
            self.data = list(
                map(lambda x: int(x), stream.readline().rstrip("\n").split())
            )
        except Exception:
            print("Reading triangle matrix from file error")
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
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
        except Exception:
            print("Writing triangle matrix to file error")
            stream.close()
            sys.exit(1)
