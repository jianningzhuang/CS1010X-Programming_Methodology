def attach_tag(type_tag, contents):
    return (type_tag, ) + contents

def type_tag(datum):
    if type(datum) == tuple and len(datum) == 3:
        return datum[0]
    else:
        raise Exception("Bad tagged datum -- type_tag" + str(datum))

###Table implementation

def get(op, types):
    return procs[op][types]

def put(op, types, proc):
    if op not in procs:   #procs is a dict of dicts
        procs[op] = {}
    procs[op][types] = proc #types is key to inner dict

#procs = {"real_part" : {"rectangular" : real_part_rectangular, "polar" : real_part_polar}, ....}


###Question 1

#dictionary keys must be of immutable type (NOT lists or dicts)

###Question 3

d = {'a': 1, 'b': 2}

d["c"] = 3

#print(d)

###Question 7

def increase_by_one(d):
    for key in d.keys():
        if d[key] == {}:
            continue
        elif type(d[key]) == dict:
            d[key] = increase_by_one(d[key])
        else:
            d[key] += 1
    return d

#print(increase_by_one({'1':2.7, '11':16, '111':{'a':5, 't':8}}))

###Question 8

def sum_all(*args):
    result = 0
    for value in args:
        result += value
    return result
print(sum_all(1, 2, 3, 4, 5))
















