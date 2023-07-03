def make_acct(name, bal):
    return (name, bal)

def get_name(acct):
    return acct[0]

def get_bal(acct):
    return acct[1]

def set_bal(acct, bal):
    return make_acct(get_name(acct), bal)

def deposit(acct, val):
    bal = get_bal(acct)
    set_bal(acct, bal + val)

def withdraw(acct, val):
    bal = get_bal(acct)
    if val > bal:
        return "Not enough money"
    else:
        set_bal(acct, bal - val)

jn = make_acct("jn", 1000)

###Question 1

class Mammal(object):
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def say(self):
        return "What does the " + self.name + " say"

#print(Mammal("Dog").say())

###Question 2

class Dog(Mammal):
    def __init__(self):
        super().__init__("Dog")


# Cat definition should go here
class Cat(Mammal):
    def __init__(self):
        super().__init__("Cat")

# Fox definition should go here
class Fox(Mammal):
    def __init__(self):
        super().__init__("Fox")

#print(Dog().get_name())

###Question 3

class Dog(Mammal):
    def __init__(self):
        super().__init__("Dog")
    def say(self):
        return "Woof"
        
class Cat(Mammal):
    def __init__(self):
        super().__init__("Cat")
    def say(self):
        return "Meow"
        
class Fox(Mammal):
    def __init__(self):
        super().__init__("Fox")
    def say(self):
        return "Ring-ding-ding-ding-dingeringeding"

#print(Dog().say())

###Question 4

class Artist(object):
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def get_name(self):
        return self.name

        
    def get_dob(self):
        return self.dob
        
        
# Used for public test cases.
# You DO NOT have to include this in your submission.
jt = Artist("Justin Timberlake", (1981, 1, 31))

###Question 5

def get_date_today():
    return (2013, 10, 30)

class Artist(object):
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def get_name(self):
        return self.name

        
    def get_dob(self):
        return self.dob
        
    def age(self):
        today = get_date_today()
        if today[1] > self.dob[1]:
            return today[0] - self.dob[0]
        elif today[1] == self.dob[1]:
            if today[2] >= self.dob[2]:
                return today[0] - self.dob[0]
            else:
                return today[0] - self.dob[0] - 1
                
        else:
            return today[0] - self.dob[0] - 1
        

# Used for public test cases.
# You DO NOT have to include this in your submission
jt = Artist("Justin Timberlake", (1981, 1, 31))

#print(jt.age())

###Question 6

class Duration(object):
    def __init__(self, minutes, seconds):
        self.total_seconds = minutes*60 + seconds
        
    def get_minutes(self):
        return self.total_seconds//60
    
    def get_seconds(self):
        return self.total_seconds%60

#print((Duration(3, 30)).total_seconds)

###Question 7 & 8

class Duration(object):
    def __init__(self, minutes, seconds):
        self.total_seconds = minutes*60 + seconds
        
    def get_minutes(self):
        return self.total_seconds//60
    
    def get_seconds(self):
        return self.total_seconds%60
        
    def __str__(self):
        if self.get_minutes() < 10:
            mins = "0" + str(self.get_minutes())
        else:
            mins = str(self.get_minutes())
        if self.get_seconds() < 10:
            secs = "0" + str(self.get_seconds())
        else:
            secs = str(self.get_seconds())
        return mins + ":" + secs
    def __add__(self, other):
        return Duration((self.total_seconds + other.total_seconds)//60, (self.total_seconds + other.total_seconds)%60)

#print(str(Duration(103, 20)))

#print(str(Duration(0,20) + Duration(0,30)))

###Question 9

class Song(object):
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration
        
    
    def get_artist(self):
        return self.artist
        
    
    def get_title(self):
        return self.title
        
        
    def get_duration(self):
        return self.duration

###Question 10

class Album(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
    
    def total_runtime(self):
        runtime = Duration(0, 0)
        for song in self.songs:
            runtime = runtime + song.get_duration()
        return runtime























































    
