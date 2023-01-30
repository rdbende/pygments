"""
    get_css_properties
    ~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""


from pygments.util import format_lines
import json
import urllib.request

HEADER = '''\
"""
    pygments.lexers._css_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This file is autogenerated by scripts/get_css_properties.py

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
'''

if __name__ == "__main__":
    data_request = urllib.request.urlopen('https://www.w3.org/Style/CSS/all-properties.en.json')
    data = json.load(data_request)
    names = set([p['property'] for p in data if p['property'] != '--*'])

    with open('../pygments/lexers/_css_builtins.py', 'w', encoding='utf-8') as builtin_file:
        builtin_file.write(HEADER)
        builtin_file.write(format_lines('_css_properties', sorted(names)))
