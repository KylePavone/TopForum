import re


def makeslug(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)
