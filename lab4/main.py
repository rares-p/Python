def ex1():
    class Stack:
        def __init__(self):
            self.__stack = []

        def push(self, x):
            self.__stack.append(x)

        def pop(self):
            if len(self.__stack) == 0:
                return None
            return self.__stack.pop()

        def peek(self):
            if len(self.__stack) == 0:
                return None
            return self.__stack[-1]

    # test = Stack()
    # test.push(1)
    # test.push(2)
    # test.push(3)
    # test.push(4)
    # print(test._Stack__stack[1])  # asta merge
    # print(test.peek())
    # print(test.pop())
    # print(test.pop())


def ex2():
    class Queue:
        def __init__(self):
            self.__queue = []

        def push(self, x):
            self.__queue.append(x)

        def pop(self):
            if len(self.__queue) == 0:
                return None
            return self.__queue.pop(0)

        def peek(self):
            if len(self.__queue) == 0:
                return None
            return self.__queue[0]

    # test = Queue()
    # test.push(1)
    # test.push(2)
    # test.push(3)
    # test.push(4)
    # print(test._Queue__queue[1])  # asta merge
    # print(test.peek())
    # print(test.pop())
    # print(test.pop())


def ex3():
    class Matrix:
        def __init__(self, n, m):
            if n < 0 or m < 0:
                raise Exception("Wrong size")
            self.n = n
            self.m = m
            self.__matrix = [[0 for j in range(m)] for i in range(n)]

        def get(self, i, j):
            if i < 0 or j < 0 or i >= self.n or j >= self.m:
                return None
            return self.__matrix[i][j]

        def set(self, i, j, value):
            self.__matrix[i][j] = value

        def transpose(self):
            transposed = Matrix(self.m, self.n)
            for i in range(self.n):
                for j in range(self.m):
                    transposed.set(j, i, self.get(i, j))
            return transposed

        def multiply(self, other):
            if self.m != other.n:
                raise ValueError("Wrong size")
            result = Matrix(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    result.set(i, j, sum(self.get(i, k) * other.get(k, j) for k in range(self.m)))
            return result

        def transform(self, _lambda):
            for i in range(self.n):
                for j in range(self.m):
                    self.__matrix[i][j] = _lambda(self.__matrix[i][j])

        def __str__(self):
            return "\n".join(["\t".join(map(str, i)) for i in self.__matrix])


if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
