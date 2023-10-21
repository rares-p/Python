import math


# Write a function to return a list of the first n numbers in the Fibonacci string.
def ex1(n: int) -> list[int]:
    if n == 0:
        return []
    elif n == 1:
        return [1]
    lista = [1]
    a = 0
    b = 1
    for i in range(n - 1):
        lista.append(a + b)
        b = a + b
        a = b - a
    return lista


# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def ex2(initial_list: list[int]) -> list[int]:
    prime_list = []
    for x in initial_list:
        if x == 2:
            pass
        elif x & 1 and x > 2:
            prime = True
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                if x % i == 0:
                    prime = False
                    break
            if not prime:
                continue
        else:
            continue
        prime_list.append(x)

    return prime_list


# Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with
# b, a - b, b - a)
def ex3(a: list, b: list) -> tuple[list, list, list, list]:
    intersection = list(set.intersection(set(a), set(b)))
    union = list(set().union(set(a), set(b)))
    a_minus_b = list(set(a).difference(set(b)))
    b_minus_a = list(set(b).difference(set(a)))

    return intersection, union, a_minus_b, b_minus_a


# Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a
# start position (integer). The function will return the song composed by going through the musical notes beginning
# with the start position and following the moves given as parameter. Example : compose(["do", "re", "mi", "fa",
# "sol"], [1, -3, 4, 2], 2)  will return ["mi", "fa", "do", "sol", "re"]
def ex4(notes: list[str], pos: list[int], start: int) -> list[str]:
    result: list[str] = [notes[start]]
    for p in pos:
        start += p
        if start >= len(notes):
            start %= len(notes)
        elif start < 0:
            start += len(notes) * (abs(start) // len(notes) + 1)
        result.append(notes[start])
    return result


# Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
# elements under the main diagonal with 0 (zero).
def ex5(a: list[list[int]]) -> list[list[int]]:
    n = len(a)
    for i in range(1, n):
        for j in range(0, i):
            a[i][j] = 0
    return a


# Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list
# containing the items that appear exactly x times in the incoming lists. Example: For the [1,2,3], [2,3,4],[4,5,6],
# [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.
def ex6(lists: list[list], x: int) -> list:
    freq = {}
    result = []
    for i_list in lists:
        for i in i_list:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    for key in freq:
        if freq[key] == x:
            result.append(key)
    return result


if __name__ == '__main__':
    # print(ex1(8))
    # print(ex2([7, 4, 2, 1, 235, 35, 3, 7, 88, 2, 0, 1, 15, 16, 17, 80, 81, 82, 97]))
    # print(ex3([2, 3, 6, 3], [7, 4, 2, 8, 6]))
    # print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    # print(ex5([[1, 2, 3, 2],
    #            [2, 4, 4, 3],
    #            [5, 5, 2, 5],
    #            [6, 6, 7, 6]]))
    # print(ex6([[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]], 2))
    pass
