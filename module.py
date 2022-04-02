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
        stream.write(f'Container contains {self.size} elements\n')

        if self.data != None:
            for item in self.data:
                item.write_to(stream)

    def clear(self):
        self.size = 0
        self.__capacity = None
        self.data = None

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.data)


class Matrix:
    def __init__(self):
        self.size = 0

    def read_from(self, stream):
        self.size = int(stream.readline().rstrip('\n'))

    def write_to(self, stream, out_type=3):
        stream.write(f'Size: {self.size}\n')

    @staticmethod
    def create_from(stream, line):
        k = int(line)

        if k == 1:
            matrix = TwoDimArray()
        elif k == 2:
            matrix = Diagonal()
        else:
            stream.close()
            raise Exception('Error type')

        matrix.read_from(stream)
        return matrix


class OutputType(Enum):
    by_row = 1,
    by_col = 2,
    one_line = 3


class TwoDimArray(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        super().read_from(stream)
        for i in range(self.size):
            line = stream.readline().rstrip('\n')
            self.data.append(list(map(lambda x: int(x), line.split())))

    def write_to(self, stream, out_type=OutputType.one_line):
        stream.write('\tThis is two-dimensional array\n')

        if out_type == OutputType.by_row:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f'{self.data[i][j]} ')
                stream.write('\n\t\t')

        elif out_type == OutputType.by_col:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f'{self.data[j][i]} ')
                stream.write('\n\t\t')

        elif out_type == OutputType.one_line:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f'{self.data[i][j]} ')
            stream.write('\n\t\t')
        else:
            stream.write('\tError matrix output type\n')

        super().write_to(stream)


class Diagonal(Matrix):
    def __init__(self):
        super().__init__()
        self.data = None

    def read_from(self, stream):
        super().read_from(stream)
        self.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))

    def write_to(self, stream, out_type=OutputType.one_line):
        stream.write('\tThis is diagonal matrix\n')

        if out_type == OutputType.by_row or out_type == OutputType.by_col:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write('{} '.format(self.data[i] if i == j else 0))
                stream.write('\n\t\t')

        elif out_type == OutputType.one_line:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write('{} '.format(self.data[i] if i == j else 0))
            stream.write('\n\t\t')
        else:
            stream.write('\tError matrix output type\n')

        super().write_to(stream)
