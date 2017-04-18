"""
utilities to work with names and strings
"""


"""
removes suffix from given name in string
return: string, name without suffix
"""
def removeSuffix(name):
    edits = name.split('_')

    # check if name doesnt have suffix
    if len(edits) < 2:
        return name
    suffix = '_' + edits[1]
    nameNoSuffix = name[ : -len(suffix)]

    return nameNoSuffix