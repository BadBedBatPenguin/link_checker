import re
from typing import List
import typer
from requests import get, post, put, patch, delete, options, head


INVALID_STATUS_CODES = (405,)
METHODS = [
    ['GET', get],
    ['POST', post],
    ['PUT', put],
    ['PATCH', patch],
    ['DELETE', delete],
    ['OPTIONS', options],
    ['HEAD', head],
]


def links_checker(string_set:List[str])->dict:
    '''returns response code for links in given string set'''
    # string_set = links.split(', ')
    result_dict = {}
    for string in string_set:
        if not re.match((
                '^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.'
                '[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$'
            ), string):
            print(f'Строка "{string}" не является ссылкой.')
        else:
            codes = {}
            for method, function in METHODS:
                code = function(string, timeout=15).status_code
                if code not in INVALID_STATUS_CODES:
                    codes[method] = code
            result_dict[string] = codes
    return result_dict
    # print(result_dict)
    # return []


# assert isinstance(links_checker(''), dict), (
#     f'program returns {type(links_checker(''))} instead of dict'
# )
# assert
# print(links_checker(('https://google.com', 'https://www.facebook.com')))
# if __name__ == '__main__':
#     typer.run(links_checker)
