#******************************************************
#*
#*  CS1010S Re-Practical Exam
#*  AY2016/2015, Semester 1
#*  Name: <fill in your name here>
#*
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

###
### Question 1
###

def compute(f, x):
    result = 0
    for term in f:
        result += term[0]*(x**term[1])
    return result


def deriv(f):
    result = ()
    for term in f:
        if term[1] > 0:
            result += ((term[0]*term[1], term[1] - 1),)
    return result


def root(f, x0, d):
    new = x0 - compute(f, x0)/compute(deriv(f), x0)
    delta = abs(x0 - new)
    while delta > d:
        current = new
        new = current - compute(f, current)/compute(deriv(f), current)
        delta = abs(current - new)
    return new
        


# Test cases
def test_q1a():
    print(compute(((3,2), (-8,0)), 8))
    print(compute(((1,3), (-2,2), (-11,1), (12,0)), -3))
    print(compute(((5,1),), 5))

def test_q1b():
    print(deriv(((3,2), (-8,0))))
    print(deriv(((1,3), (-2,2), (-11,1), (12,0))))
    print(deriv(((5,1),)))

def test_q1c():
    print(root(((3,2), (-8,0)), -1, 0.0001))
    print(root(((3,2), (-8,0)), 1, 0.0001))
    print(root(((1,3), (-2,2), (-11,1), (12,0)), 2.35287527, 0.0001))
    
# Uncomment to test
#test_q1a()
#test_q1b()
#test_q1c()

##############
# Question 2 #
##############

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows


def statistics(fname, module_code):
    data = read_csv(fname)[1:]
    students = {}
    for student, module, ca, marks in data:
        if module == module_code:
            if student not in students:
                students[student] = 0
            students[student] += int(marks)
    result = []
    for student in students:
        result.append(students[student])
    result.sort()
    mean = round(sum(result)/len(result), 2)
    if len(result)%2 == 1:
        median = result[len(result)//2]
    else:
        median = (result[len(result)//2])
    return (median, mean)
            
        


def top_students(fname, module_code):
    data = read_csv(fname)[1:]
    students = {}
    for student, module, ca, marks in data:
        if module == module_code:
            if student not in students:
                students[student] = {}
            students[student][ca] = int(marks)
    result = []
    for student in students:
        result.append([student, (students[student]["Midterm"], students[student]["PE"],students[student]["Project"])])
    result.sort(key = lambda x: sum(x[1]), reverse = True)
    cut_off = len(result)//10
    if len(result) < 10:
        cut_off = 1
    award = {}
    for student in result:
        if sum(student[1]) >= sum(result[cut_off - 1][1]):
            award[student[0]] = student[1]
    return award
    
    


# Test cases
def test_q2a():
    print(statistics("evil.csv", "CS1010E"))
    print(statistics("evil.csv", "MA1105"))
    print(statistics("evil.csv", "CM1101"))

def test_q2b():
    print(top_students('evil.csv', 'CS2105') ==
          { 'A00584X': (20, 11, 12), 'A00862H': (19, 13, 14),
            'A00249V': (17, 15, 15), 'A00270U': (17, 11, 15),
            'A00691H': (17, 15, 10), 'A00547W': (19, 12, 15),
            'A00619O': (14, 13, 15) })
    print(top_students('evil.csv', 'CM1101') ==
          { 'A00732A': (16, 13, 15) })
    print(top_students('evil.csv', 'EG1109') ==
          { 'A00060A': (17, 12, 15), 'A00467J': (16, 14, 14),
            'A00897P': (18, 15, 10), 'A00051B': (19, 14, 12),
            'A00148Y': (19, 12, 14), 'A00911R': (19, 12, 12), 
            'A00642Y': (14, 14, 15), 'A00700Y': (18, 15, 15) })

# Uncomment to test
#test_q2a()
#test_q2b()

##############
# Question 3 #
##############

class Artifact:

    def __init__(self, name, charge, magics):
        self.name = name
        self.charge = charge
        self.magics = magics
        self.masters = []
        self.equipped = []

    def get_name(self):
        return self.name

    def get_magics(self):
        return tuple(self.magics)

    def get_charges(self):
        return self.charge

    def get_masters(self):
        result = ()
        for master in self.masters:
            if master in self.equipped:
                result += (master.name,)
        return result

    def choose(self, sorcerer):
        if sorcerer in self.masters:
            return sorcerer.name + " is already chosen by " + self.name
        else:
            self.masters.append(sorcerer)
            return self.name + " chooses " + sorcerer.name

    def abandon(self, sorcerer):
        if sorcerer not in self.masters:
            return sorcerer.name + " is not chosen by " + self.name
        else:
            self.masters.remove(sorcerer)
            return self.name + " abandons " + sorcerer.name
            


class Sorcerer:

    def __init__(self, name):
        self.name = name
        self.artifacts = []
        self.magic = {}

    def get_name(self):
        return self.name

    def get_artifacts(self):
        result = ()
        for artifact in self.artifacts:
            result += (artifact.name,)
        return result

    def get_magics(self):
        result = {}
        for artifact in self.artifacts:
            if artifact.masters == [] or self in artifact.masters:
                if artifact.charge > 0:
                    for magic in artifact.get_magics():
                        if magic not in result:
                            result[magic] = self.magic[magic]
        return result
                
        

    def equip(self, artifact):
        if artifact in self.artifacts:
            return self.name + " is already equipping the " + artifact.name
        else:
            self.artifacts.append(artifact)
            artifact.equipped.append(self)
            for magic in artifact.get_magics():
                if magic not in self.magic:
                    self.magic[magic] = 1
            return self.name + " equips " + artifact.name

    def unequip(self, artifact):
        if artifact not in self.artifacts:
            return self.name + " is not equipped with the " + artifact.name
        else:
            self.artifacts.remove(artifact)
            artifact.equipped.remove(self)
            return self.name + " unequips " + artifact.name
        

    def train(self):
        if self.get_magics() == {}:
            return self.name + " does not have any magic"
        else:
            lowest = None
            increase = None
            for magic in self.get_magics():
                if lowest == None or self.magic[magic] < lowest:
                    lowest = self.magic[magic]
                    increase = magic
            self.magic[increase] += 1
            return self.name + " trains " + increase + " to level " + str(self.magic[increase])

    def valid_artifacts(self, spell):
        result = []
        for artifact in self.artifacts:
            if spell in artifact.get_magics():
                result.append(artifact)
        return result
        
                

    def chant(self, spell):
        if spell not in self.get_magics():
            return self.name + " cannot " + spell
        valid = []
        for artifact in self.valid_artifacts(spell):
            if artifact.masters == [] and artifact.charge > 0:
                valid.append(artifact)
            elif self in artifact.masters and artifact.charge > 0:
                valid.append(artifact)
        if valid == []:
            return self.name + " cannot " + spell
        highest = None
        use = None
        for artifact in valid:
            if highest == None or artifact.charge > highest:
                highest = artifact.charge
                use = artifact
        use.charge = max(0, use.charge - self.magic[spell])
        return self.name + " does " + spell + " with " + use.name
                
        
            
        


# Test cases
def test_q3():
    eye_of_agamotto = Artifact("Eye of Agamotto", 3, ("Time magic", "Levitation", "Hypnosis"))
    cloak_of_levitation = Artifact("Cloak of Levitation", 2, ("Levitation",))

    silver_dagger = Sorcerer("Silver Dagger")
    stephen_strange = Sorcerer("Doctor Strange")

    print('stephen_strange.get_name():\t', stephen_strange.get_name() == "Doctor Strange")
    print('silver_dagger.get_magics():\t', silver_dagger.get_magics() == {})
    print('eye_of_agamotto.get_name():\t', eye_of_agamotto.get_name() == "Eye of Agamotto")
    print('eye_of_agamotto.get_magics():\t', sorted(eye_of_agamotto.get_magics()) == ['Hypnosis', 'Levitation', 'Time magic'])
    print('silver_dagger.equip(eye_of_agamotto):\t', silver_dagger.equip(eye_of_agamotto) == "Silver Dagger equips Eye of Agamotto")
    print('silver_dagger.equip(eye_of_agamotto):\t', silver_dagger.equip(eye_of_agamotto) == "Silver Dagger is already equipping the Eye of Agamotto")
    print('silver_dagger.get_magics():\t', silver_dagger.get_magics() == {'Levitation': 1, 'Time magic': 1, 'Hypnosis': 1})
    print('silver_dagger.unequip(cloak_of_levitation):\t', silver_dagger.unequip(cloak_of_levitation) == "Silver Dagger is not equipped with the Cloak of Levitation")
    print('silver_dagger.equip(cloak_of_levitation):\t', silver_dagger.equip(cloak_of_levitation) == "Silver Dagger equips Cloak of Levitation")
    print('silver_dagger.get_magics():\t', silver_dagger.get_magics() == {'Levitation': 1, 'Time magic': 1, 'Hypnosis': 1})
    print('eye_of_agamotto.get_charges():\t', eye_of_agamotto.get_charges() == 3)
    print('silver_dagger.chant("Levitation"):\t', silver_dagger.chant("Levitation") == "Silver Dagger does Levitation with Eye of Agamotto")
    print('eye_of_agamotto.get_charges():\t', eye_of_agamotto.get_charges() == 2)
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ())
    print('eye_of_agamotto.choose(stephen_strange):\t', eye_of_agamotto.choose(stephen_strange) == "Eye of Agamotto chooses Doctor Strange")
    print(silver_dagger.get_magics())
    print('silver_dagger.get_magics():\t', silver_dagger.get_magics() == {'Levitation': 1})
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() == {})
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ())
    print('silver_dagger.unequip(eye_of_agamotto):\t', silver_dagger.unequip(eye_of_agamotto) == "Silver Dagger unequips Eye of Agamotto")
    print('stephen_strange.equip(eye_of_agamotto):\t', stephen_strange.equip(eye_of_agamotto) == "Doctor Strange equips Eye of Agamotto")
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() == {'Levitation': 1, 'Time magic': 1, 'Hypnosis': 1})
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ('Doctor Strange',))
    print('stephen_strange.train():\t', stephen_strange.train() in ("Doctor Strange trains Levitation to level 2",
                                                                    "Doctor Strange trains Hypnosis to level 2",
                                                                    "Doctor Strange trains Time magic to level 2"))
    print('stephen_strange.unequip(eye_of_agamotto):\t', stephen_strange.unequip(eye_of_agamotto) == "Doctor Strange unequips Eye of Agamotto")
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ())
    print('stephen_strange.train():\t', stephen_strange.train() == "Doctor Strange does not have any magic")
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() == {})
    print('stephen_strange.equip(eye_of_agamotto):\t', stephen_strange.equip(eye_of_agamotto) == "Doctor Strange equips Eye of Agamotto")
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() in ({'Levitation': 2, 'Time magic': 1, 'Hypnosis': 1},
                                                                              {'Levitation': 1, 'Time magic': 2, 'Hypnosis': 1},
                                                                              {'Levitation': 1, 'Time magic': 1, 'Hypnosis': 2}))
    print('stephen_strange.train():\t', stephen_strange.train() in ("Doctor Strange trains Levitation to level 2",
                                                                    "Doctor Strange trains Hypnosis to level 2",
                                                                    "Doctor Strange trains Time magic to level 2"))
    print('stephen_strange.train():\t', stephen_strange.train() in ("Doctor Strange trains Levitation to level 2",
                                                                    "Doctor Strange trains Hypnosis to level 2",
                                                                    "Doctor Strange trains Time magic to level 2"))
    print('stephen_strange.get_magics():\t', stephen_strange.get_magics() == {'Levitation': 2, 'Time magic': 2, 'Hypnosis': 2})
    print('eye_of_agamotto.choose(silver_dagger):\t', eye_of_agamotto.choose(silver_dagger) == "Eye of Agamotto chooses Silver Dagger")
    print('silver_dagger.equip(eye_of_agamotto):\t', silver_dagger.equip(eye_of_agamotto) == "Silver Dagger equips Eye of Agamotto")
    print('stephen_strange.chant("Hypnosis"):\t', stephen_strange.chant("Hypnosis") == "Doctor Strange does Hypnosis with Eye of Agamotto")
    print('silver_dagger.chant("Time magic"):\t', silver_dagger.chant("Time magic") == "Silver Dagger cannot Time magic")
    print('silver_dagger.chant("Levitation"):\t', silver_dagger.chant("Levitation") == "Silver Dagger does Levitation with Cloak of Levitation")
    print('eye_of_agamotto.get_masters():\t', eye_of_agamotto.get_masters() == ('Doctor Strange', 'Silver Dagger'))
    print('cloak_of_levitation.abandon(silver_dagger):\t', cloak_of_levitation.abandon(silver_dagger) == "Silver Dagger is not chosen by Cloak of Levitation")
    print('eye_of_agamotto.abandon(silver_dagger):\t', eye_of_agamotto.abandon(silver_dagger) == "Eye of Agamotto abandons Silver Dagger")


# uncomment to test
test_q3()
