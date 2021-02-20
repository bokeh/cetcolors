# CET_merge.py - create updated `aliases` and `mapping` for CET_to_py.py
# 1. MATLAB/octave script `make_csvs_from_colorcet.m` must be run first
# 2. Existing `aliases` and `mapping` from CET_to_py.py must be pasted below
# 3. After running script:
#    a. Add the new mapsdir to the `paths` list in CET_to_py.py.
#    b. Replace the existing `aliases` and `mapping` in CET_to_py.py with those printed by this script.

from CET_updates import new_aliases, new_mappings, new_mapsdir

# paste `aliases` from CET_to_py.py here
aliases = dict()

# paste `mapping` from CET_to_py.py here
mapping = {}


aliases.update(new_aliases)
mapping.update(new_mappings)

def print_dict(name, d, braces=False, tabs = 0, evenspace=False):
    if evenspace:
        k_maxlen = 0
        for k in d:
            k_maxlen = max(k_maxlen, len(k))
        fmt0 = "{{0:{0:d}s}}".format(k_maxlen)
    else:
        fmt0 = "{0}"
    start = "{" if braces else "dict("
    fmt = ("'{0}': {1}" if braces else "{0} = {1}").format(fmt0, '{1}')
    end = "}" if braces else ")"
    s4 = ' '*4
    tabs = s4*tabs
    print(tabs + "{0} = {1}".format(name, start))
    for k in sorted(d, key=lambda k: k):
        print(tabs + s4 + fmt.format(k, d[k]))
    print(tabs + end)

print("new_mapsdir = '{0}'".format(new_mapsdir))
print_dict('aliases', aliases, evenspace=True)
print_dict('mapping', mapping, braces=True)
