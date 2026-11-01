def disemvowel(string_):
    return "".join(i for i in string_ if i not in "aeiouAEIOU")

def to_alternating_case(string):
    return string.swapcase()


def replace_exclamation(st):
    return "!".join(i for i in st if i not in "aeiouAEIOU")


