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
    intersection = []
    b_map = {}
    for x in b:
        if x in b_map:
            b_map[x] += 1
        else:
            b_map[x] = 1
    b_map_saved = b_map.copy()
    for x in a:
        if x in b_map and b_map[x] > 0:
            intersection.append(x)
            b_map[x] -= 1
    union = []
    for x in a:
        union.append(x)
        if x in b_map and b_map[x] > 0:
            b_map[x] -= 1
    for x in b:
        if b_map[x] > 0:
            b_map[x] -= 1
            union.append(x)
    b_map = b_map_saved.copy()
    a_minus_b = []
    for x in a:
        if x not in b_map:
            a_minus_b.append(x)
        elif b_map[x] > 0:
            b_map[x] -= 1
        else:
            a_minus_b.append(x)
    a_map = {}
    for x in a:
        if x in a_map:
            a_map[x] += 1
        else:
            a_map[x] = 1
    b_minus_a = []
    for x in b:
        if x not in a_map:
            b_minus_a.append(x)
        elif a_map[x] > 0:
            a_map[x] -= 1
        else:
            b_minus_a.append(x)

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


# Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element
# will be the greatest palindrome number.
def ex7(numbers: list[int]) -> tuple[int, int]:
    no_pal: int = 0
    biggest_pal: int = -1
    for number in numbers:
        if str(number) == str(number)[::-1]:
            no_pal += 1
            if number > biggest_pal:
                biggest_pal = number
    return no_pal, biggest_pal


# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to
# True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
# Example:x = 2, ["test", "hello", "lab002"], flag = False  ????????????????????????????????????????????????????????????
def ex8(strings: list[str], x: int = None, flag: bool = None):
    if x is None:
        x = 2
    if flag is None:
        flag = True
    result = []
    for string in strings:
        current_result = []
        for char in string:
            if ord(char) % x == 0 if flag else ord(char) % x != 0:
                current_result.append(char)
        if current_result:
            result.append(current_result)
    return result


# Write a function that receives as parameter a matrix which represents the heights of the spectators in a stadium and
# will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A
# spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are
# occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest
# row from the field. Example: FIELD [[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]
# Will return : [(2, 2), (3, 4), (2, 4)]
def ex9(matrix: list[list[int]]) -> list[tuple[int, int]]:
    n = len(matrix)
    m = len(matrix[0])
    result = []
    for j in range(m):
        tallest = matrix[0][j]
        for i in range(1, n):
            if matrix[i][j] < tallest:
                result.append((i, j))
            tallest = max(tallest, matrix[i][j])
    return result


# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple
# contains the first items in the lists, the second element contains the items on the position 2 in the lists,
# etc. Example: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. Note: If
# input lists do not have the same number of items, missing items will be replaced with None to be able to generate
# max ([len(x) for x in input_lists]) tuples.
def ex10(*args: list) -> list[tuple]:
    return list(tuple(arg[i] if len(arg) > i else None for arg in args) for i in range(max(len(arg) for arg in args)))


# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
# tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def ex11(string_list: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return sorted(string_list, key=lambda x: x[1][2])


# Write a function that will receive a list of words as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters. Example: group_by_rhyme(['ana',
# 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]
def ex12(words: list[str]) -> list[list[str]]:
    result = {}
    for word in words:
        if word[-2:] in result:
            result[word[-2:]].append(word)
        else:
            result[word[-2:]] = [word]
    return list(result.values())


if __name__ == '__main__':
    # print(ex1(8))
    # print(ex2([7, 4, 2, 1, 235, 35, 3, 7, 88, 2, 0, 1, 15, 16, 17, 80, 81, 82, 97]))
    print(ex3([2, 3, 6, 3], [7, 4, 2, 8, 6, 2]))
    # print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    # print(ex5([[1, 2, 3, 2],
    #            [2, 4, 4, 3],
    #            [5, 5, 2, 5],
    #            [6, 6, 7, 6]]))
    # print(ex6([[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]], 2))
    # print(ex7([5, 67, 767, 1001, 2, 1002, 111]))
    # print(ex8(["test", "hello", "lab002"], 2, False))
    # print(ex9([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))
    # print(ex10([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
    # print(ex11([('abc', 'bcd'), ('abc', 'zza')]))
    # print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))
    pass
