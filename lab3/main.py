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
            result[x] = 0


# Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be
# recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def ex3(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return False
        for x in a.keys():
            return ex3(a[x], b[x])
    if isinstance(a, list) or isinstance(b, tuple):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            return ex3(a[i], b[i])
    return not (a != b)


# The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
# name-parameters. Build and return a string that represents the corresponding XML element. Example:
# build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns
# the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "
def ex4(tag, content, **kwargs):
    result = f'<{tag}'
    for key, value in kwargs.items():
        result += f" {key}=\"{value}\""
    result += f"> {content}"
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


if __name__ == '__main__':
    # print(ex4 ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
    print(ex5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
              {"key1": "come inside, it's too cold out"}))
