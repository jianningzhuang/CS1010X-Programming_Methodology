class Food(object):
    count = 0
    def __init__(self, name, nutrition_value, good_until):
        self.name = name
        self.nutrition_value = nutrition_value
        self.good_until = good_until
        self.age = 0
        Food.count += 1
        

    def sit_there(self, time):
        self.age += time
        

    def eat(self):
        if self.age < self.good_until:
            return self.nutrition_value
        else:
            return 0

class AgedFood(Food):
    def  __init__(self, name, nutrition_value, good_until, good_after):
        super().__init__(name, nutrition_value, good_until)
        self.good_after = good_after

    def sniff(self):
        return self.age >= self.good_after

    def eat(self):
        if self.sniff():
            return super().eat()
        else:
            return 0

class VendingMachine(object):
    def __init__(self, name, nutrition_value, good_until):
        self.name = name
        self.nutrition_value = nutrition_value
        self.good_until = good_until
        self.age = 0

    def sit_there(self, time):
        self.age += (time//2)

    def sell_food(self):
        print(self.good_until)
        print(self.age)
        return Food(self.name, self.nutrition_value, self.good_until - self.age)

def mapn(fn, lsts):
    if not lsts[0]:
        return ()
    else:
        first = tuple(map(lambda x: x[0], lsts))
        rest = tuple(map(lambda x: x[1:], lsts))
        return (fn(*first), ) + mapn(fn, rest)   #f(*args) forces tuple into arguments
#print(mapn ( lambda x ,y , z : (z , x + y ) ,
#(( 1 , 2 , 3 ) , (4 , 5 , 6 ) , ('first ', 'second ', 'third '))))
    
    
        


            
banana = Food("banana", 50, 10)
avacado = AgedFood("avacado", 100, 20, 15)
milk = VendingMachine("milk", 120, 30)
milk.sit_there(40)




class PatternMatcher(object):
    def __init__(self):
        self.pattern = []
        self.index = 0
        
        
    def clear(self):
        self.pattern = []
        
        
    def learn(self, *args):
        for elem in args:
            self.pattern.append(elem)
            
    def match(self, *args):
        if self.pattern == []:
            return "No pattern learnt"
        match = False
        for elem in args:
            if elem == self.pattern[self.index] and self.index < len(self.pattern) - 1:
                self.index += 1
                match = True
            elif elem != self.pattern[self.index] and self.index < len(self.pattern):
                self.index = 0
                match = False
            else:
                self.index = 0
                match = True
        if self.index == 0 and match == True:
            return "Patern matched!"
        else:
            return match




my_pattern = PatternMatcher()
my_pattern.learn(1, 2, 3)



class JoinableTransformer(object):
    
    def __init__(self, n):
        self.size = n
        self.index = 1
        self.brothers = [None]*n
        self.brothers[0] = self
        self.leader = self
        self.created = [None]*n
        self.created[0] = [self]
    def get_brother(self, k):
        if k < 1 or k > self.size:
            return "Invalid index"
        elif self.created[k-1] != None:
            print("copy")
            return self.created[k-1]
        else:
            brother = JoinableTransformer(self.size)
            brother.index = k
            brother.brothers = [None]*self.size
            brother.brothers[k-1] = brother
            brother.leader = self
            self.created[0] = self
            self.created[k-1] = brother
            return brother
    def join(self, b):
        if self.leader != b.leader:
            return "Can't join"
        elif self.index == b.index:
            return "Can't join"
        else:
            if b not in self.brothers:
                for brother in self.brothers:
                    if brother != None:
                        brother.brothers[b.index - 1] = b
                        b.brothers[brother.index - 1] = brother
                return "Transformers joined"
            else:
                return "Already joined"
            
    def separate(self):
        count = 0
        for elem in self.brothers:
            if elem == None:
                count += 1
        print(count)
        if count == self.size - 1:
            return "Not joined"
        else:
            for brother in self.brothers:
                if brother == self or brother == None:
                    continue
                else:
                    brother.brothers[self.index - 1] = None
            self.brothers = [None]*self.size
            self.brothers[self.index-1] = self

        return "Transformers separated"
        
    def fight(self, b):
        if self.leader == b.leader:
            return "You're kidding"
        count1 = 0
        count2 = 0
        for i in self.brothers:
            if i != None:
                count1 += 1
        for j in b.brothers:
            if j != None:
                count2 += 1
        if count1 > count2:
            return "Fight won"
        elif count2 > count1:
            return "Fight lost"
        else:
            return "Fight ends in draw"
      
######################################################################
######################################################################
######### DO NOT MODIFY ANYTHING BELOW ###############################
######################################################################
######################################################################

# These are the evil Decepticon Constructicons - they can combine into
# this nasty giant Decepticon called Devastator
overload = JoinableTransformer(5)
mixmaster = overload.get_brother(2)
longhaul = overload.get_brother(3)
rampage = overload.get_brother(4)
scrapper = overload.get_brother(5)
scrapper2 = overload.get_brother(5)
scrapper is scrapper2 # => True
scrapper is longhaul # => False

# These are the small Autobot twins - they can combine into a pink and
# white ice cream van
mudflap = JoinableTransformer(2)
skids = mudflap.get_brother(2)
mudflap.join(rampage)  # => "Can't join"
mudflap.join(mudflap)  # => "Can't join"
mudflap.fight(rampage) # => "Fight ends in draw"























