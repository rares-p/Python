# Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a
# intersected with b, a reunited with b, a - b, b - a)
def ex1(a: list, b: list) -> list:
    return [set.intersection(set(a), set(b)), set.union(set(a), set(b)),
            set.difference(set(a), set(b)), set.difference(set(b), set(a))]


# Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given
# text. Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
def ex2(string: str):
    result = {}
    for x in string:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result


# Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be
# recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def ex3(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return False
        return all(ex3(a[x], b[x]) for x in a.keys())
    if isinstance(a, list) or isinstance(b, tuple):
        if len(a) != len(b):
            return all(ex3(a[i], b[i]) for i in range(len(a)))
    return not (a != b)


# The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
# name-parameters. Build and return a string that represents the corresponding XML element.
def ex4(tag, content, **kwargs):
    result = f'<{tag.strip()}'
    for key, value in kwargs.items():
        result += f" {key.strip()}=\"{value.strip()}\""
    result += f">{content.strip()}</{tag.strip()}>"
    return result


# The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a
# dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix",
# "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at
# the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the
# rules, False otherwise. Example: the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules
# are respected for "key1" and "key2" "key3" that does not appear in the rules.
def ex5(rules, x):
    for k in x.keys():
        if k not in (rule[0] for rule in rules):
            return False
    for rule in rules:
        if rule[0] not in x.keys():
            continue
        if not x[rule[0]].startswith(rule[1]):
            return False
        if rule[2] not in x[rule[0]][1:-1]:
            return False
        if not x[rule[0]][::-1].startswith(rule[3]):
            return False
    return True
    pass


# Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique
# elements in the list, and b representing the number of duplicate elements in the list.
def ex6(elem):
    a = 0
    b = 0
    for x in set(elem):
        if elem.count(x) > 1:
            b += 1
        else:
            a += 1
    return a, b


# Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -.
def ex7(*args):
    result = {}
    for a in args:
        for b in args:
            if a is not b:
                result[f"{str(a)} | {str(b)}"] = set.union(a, b)
                result[f"{str(a)} & {str(b)}"] = set.intersection(a, b)
                result[f"{str(a)} - {str(b)}"] = set.difference(a, b)
                # result[f"{str(b)} - {str(a)}"] = set.difference(b, a) - nu este nevoie de b - a
    return result


# Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key
# "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the
# following way: the value of the current key is the key for the next value, until you find a loop (a key that was
# visited before). The function must return the list of objects obtained as previously described. Ex: loop({'start':
# 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']
# de ce nu ['a', '6', 'z', '2', '2']
def ex10(mapping):
    key = 'start'
    visited = set()
    result = []
    while key not in visited:
        result.append(mapping[key])
        visited.add(key)
        key = mapping[key]
    return result


# Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
# adn will return the number of positional arguments whose values can be found among keyword arguments values. Ex:
def ex11(*args, **kwargs):
    return len(set.intersection(set(args), set(kwargs.values())))


if __name__ == '__main__':
    # print(ex3({'a': 1, 'b': {2, 3}, 'c': {'x': 4, 'y': {5}}}, {'a': 1, 'b': {3, 2}, 'c': {'x': 4, 'y': {5}}}))
    print(ex4 ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
    # print(ex5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
    #           {"key1": "come inside, it's too cold out"}))
    # print(ex6([1, 2, 2, 3, 4, 4, 5]))
    # print(ex7({1, 2}, {2, 3}))
    # print(ex10({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    # print(ex11(1, 2, 3, 4, x=1, y=2, z=3, w=5))
    pass
