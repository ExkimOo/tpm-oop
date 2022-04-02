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

    def sort(self):
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                if self.data[i].compare(self.data[j]):
                    self.data[i], self.data[j] = self.data[j], self.data[i]


class Matrix:
    def __init__(self):
        self.size = 0

    def read_from(self, stream):
        self.size = int(stream.readline().rstrip('\n'))

    def write_to(self, stream):
        stream.write(f'\tSize: {self.size}\n')

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

    def sum(self):
        s = 0
        for item in self.data:
            if isinstance(item, int):
                s += item
            else:
                s += sum(item)
        return s

    def compare(self, other):
        return self.sum() < other.sum()


class TwoDimArray(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        super().read_from(stream)
        for i in range(self.size):
            line = stream.readline().rstrip('\n')
            self.data.append(list(map(lambda x: int(x), line.split())))

    def write_to(self, stream):
        stream.write('\tThis is two-dimensional array\n')
        for row in self.data:
            stream.write(f'\t\t{row}\n')
        super().write_to(stream)


class Diagonal(Matrix):
    def __init__(self):
        super().__init__()
        self.data = None

    def read_from(self, stream):
        super().read_from(stream)
        self.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))

    def write_to(self, stream):
        stream.write('\tThis is diagonal matrix\n')
        stream.write(f'\t\t{self.data}\n')
        super().write_to(stream)
