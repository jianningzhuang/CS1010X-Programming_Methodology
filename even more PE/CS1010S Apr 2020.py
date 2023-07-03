from math import ceil

def num_cases(total, r, days):
    result = [1]
    for i in range(1, days + 1):
        new = ceil(result[-1]*r*(1 - sum(result)/total))
        result.append(new)
    return result

#print(num_cases(1000000, 1.08, 100))


class Person:

    time = 0

    def __init__(self, name):
        self.name = name
        self.place = None
        self.contact = {}

    def move(self, p):
        Person.time += 1
        if self.place != None:
            original = self.place
            original.people.remove(self)
            self.place = p
            p.people.append(self)
            for i in p.people:
                for j in p.people:
                    if i != j:
                        if j not in i.contact:
                            i.contact[j] = []
                        i.contact[j].append(Person.time)
            return self.name + " moves from " + original.name + " to " + p.name
        else:
            self.place = p
            p.people.append(self)
            for i in p.people:
                for j in p.people:
                    if i != j:
                        if j not in i.contact:
                            i.contact[j] = []
                        i.contact[j].append(Person.time)
            return self.name + " moves to " + p.name

    def trace_direct(self):
        result = []
        for p in self.contact:
            result.append(p.name)
        return result

    def trace_indirect(self, p):
        if p not in self.contact:
            return []
        t = self.contact[p][0]
        result = []
        for j in self.contact:
            for i in self.contact[j]:
                if i > t:
                    if j.name not in result and j != p:
                        result.append(j.name)
        return result


class Place:

    def __init__(self, name):
        self.name = name
        self.people = []




com1 = Place('COM1')
lt27 = Place('LT27')
s16 = Place('S16')


waikay = Person("Wai Kay")
ben = Person("Ben")
daren = Person("Daren")
jonathan = Person("Jonathan")
kenghwee = Person("Keng Hwee")

print(waikay.move(com1))
print(ben.move(com1))
print(waikay.move(s16))
print(daren.move(com1))
print(jonathan.move(lt27))
print(ben.move(lt27))
print(kenghwee.move(com1))
print(jonathan.move(com1))
print(jonathan.move(s16)) 
print(daren.move(lt27))
print(jonathan.move(com1))
print(ben.move(s16)) 
print(waikay.trace_direct())
print(ben.trace_indirect(waikay))
print(jonathan.trace_indirect(waikay))
print(daren.trace_indirect(waikay))
print(kenghwee.trace_indirect(waikay))










        
        
    
