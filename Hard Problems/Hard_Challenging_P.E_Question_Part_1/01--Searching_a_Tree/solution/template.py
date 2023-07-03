def find_x(x, tree):
    def helper(ls):
        for i, elem in enumerate(ls):
            if type(elem) is list:
                index = helper(elem)
                if index is not None:
                    return '[%d]%s' % (i, index)
            elif elem is x:
                return '[%d]' % i
        else:
            return None

    res = helper(tree)
    if res is None:
        return res
    else:
        return str(tree) + res
