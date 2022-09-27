import re
from starlette.requests import Request


def makeslug(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


def get_db(request: Request):
    return request.state.db
