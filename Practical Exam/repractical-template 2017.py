###############
# Question 1A #
###############

def factors(n):
    result = []
    for i in range(1, n+1):
        if n%i == 0:
            result.append(i)
    return result

def test1a():
    print('=== Q1a ===')
    print(factors(2)==[1,2])
    print(factors(13)==[1,13])
    print(factors(18)==[1, 2, 3, 6, 9, 18])
test1a()

###############
# Question 1B #
###############

def repetitions(s):
    for i in range(1, len(s)+1):
        substring = s[:i]
        if substring * (len(s)//i) == s:
            return len(s)//i

def test1b():
    print('=== Q1b ===')
    print(repetitions("aaaaa")==5)
    print(repetitions("ababab")==3)
    print(repetitions("abababc")==1)
    print(repetitions("abadbabcabadbabc")==2)
test1b()

##############
# Question 2 #
##############

import csv
def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)[1:]


###############
# Question 2A #
###############

def clean_data(filename):
    data = read_csv(filename)
    result = []
    for entry in data:
        if len(entry) != 6:
            continue
        else:
            director, genre, actor, movie, rating, year = entry
            if director != "" and genre != "" and actor != "" and movie != "" \
               and rating != "" and 0 <= float(rating) <= 10 and year != "" and 1916 <= int(year) <= 2016:
                result.append([director, genre, actor, movie, rating, year])
    return result

    
def test2a():
    print('=== Q2a ===')
    answer1 = [['Christopher Nolan', 'Adventure|Drama|Sci-Fi', 'Matthew McConaughey', 'Interstellar', '8.6', '2014'],\
          ['Alan Taylor', 'Action|Adventure|Sci-Fi', 'J.K. Simmons', 'Terminator Genisys', '8.6', '2015'],\
          ['Francis Lawrence', 'Adventure|Sci-Fi', 'Jennifer Lawrence', 'The Hunger Games: Mockingjay - Part 2', '8.6', '2015'], \
          ['Duncan Jones', 'Action|Adventure|Fantasy', 'Dominic Cooper', 'Warcraft', '8.6', '2016'], \
          ['James Bobin', 'Adventure|Family|Fantasy', 'Johnny Depp', 'Alice Through the Looking Glass', '8.6', '2016']]
    print(clean_data("IMDB_small.csv")==answer1)
    answer2 = [['A. Raven Cruz', 'Action|Adventure|Comedy|Fantasy|Sci-Fi', 'Scott Levy', 'The Helix... Loaded', '4.9', '2005'], \
               ['Aaron Hann', 'Drama|Horror|Mystery|Sci-Fi|Thriller', 'Jordi Vilasuso', 'Circle', '5.3', '2015']]
    print(clean_data("IMDB.csv")[:2]==answer2)
test2a()

###############
# Question 2B #
###############

def best_movies(filename, genre, k):
    data = clean_data(filename)
    result = []
    for entry in data:
        if genre in entry[1]:
            result.append([entry[3], float(entry[4])])
    result.sort(key = lambda x: x[0])
    result.sort(key = lambda x: x[1], reverse = True)
    best = list(map(lambda x: x[0], result))
    return best[:k]


def test2b():
    print('=== Q2b ===')
    print(best_movies("IMDB_small.csv", "Comedy",5)==[])
    print(best_movies("IMDB_small.csv", "Action",3)==['Terminator Genisys', 'Warcraft'])
    print(best_movies("IMDB.csv", "Comedy",5)==['Up', 'Monsters vs. Aliens', 'Evan Almighty', 'Suicide Squad', 'Wild Wild West'])
    print(best_movies("IMDB.csv", "Action",3)==['Jupiter Ascending', 'The Legend of Tarzan', 'The Dark Knight'])
test2b()
    
###############
# Question 2C #
###############

def best_actor(filename, start_year, end_year):
    data = clean_data(filename)
    ratings = {}
    for entry in data:
        if start_year <= int(entry[5]) <= end_year:
            if entry[2] not in ratings:
                ratings[entry[2]] = [float(entry[4])]
            else:
                ratings[entry[2]].append(float(entry[4]))
    result = []
    for actor, total in ratings.items():
        result.append([actor, sum(total)/len(total)])
    result.sort(key = lambda x: x[1], reverse = True)
    if result == []:
        return None
    elif len(result) == 1:
        return result[0][0]
    else:
        best = [result[0][0]]
        for i in range(1, len(result)):
            if result[i][1] == result[0][1]:
                best.append(result[i][0])
    if len(best) == 1:
        return best[0]
    else:
        return best
        
    
def test2c():
    print('=== Q2c ===')
    print(best_actor("IMDB_small.csv", 1916, 1940)==None)
    print(sorted(best_actor("IMDB_small.csv", 1940, 2016)) == \
          sorted(['Matthew McConaughey', 'J.K. Simmons', 'Jennifer Lawrence', 'Dominic Cooper', 'Johnny Depp']))
    print(best_actor("IMDB.csv", 1916, 1940)=="Mel Blanc")
    print(best_actor("IMDB.csv", 1941, 1990)=="Ronny Cox")
    print(best_actor("IMDB.csv", 1991, 2016)=="Steve Bastoni")

test2c()

##############
# Question 3 #
##############

class SwimmingCompetition:

    def __init__(self, laps = 2, lanes = 8):
        self.length = 50
        self.laps = laps
        self.lanes = lanes
        self.swimmers = {}

    def add_swimmer(self, name, speed, turning):
        if self.lanes == 0:
            return "No more lanes!"
        else:
            self.swimmers[name] = [speed, turning]
            self.lanes -= 1

    def set_length(self, length):
        self.length = length

    def get_position(self, swimmer, t):
        if swimmer not in self.swimmers:
            return "No such swimmer"
        speed, turning = self.swimmers[swimmer]
        lap_time = self.length/speed
        if t >= self.finish_time(swimmer) or t == 0:
            return 0
        lap_no = 1
        while t - lap_time >= 0:
            t -= lap_time
            lap_no += 1
            if t <= turning:
                t = 0
                break
            t -= turning
                
        if lap_no%2 == 1:
            return t*speed
        else:
            return self.length - t*speed
            

        

    def finish_time(self, swimmer):
        if swimmer not in self.swimmers:
            return "No such swimmer"
        else:
            speed, turning = self.swimmers[swimmer]
            time = (self.length * self.laps / speed) + turning * (self.laps - 1)
            return time

    def winner(self, *k):
        standings = []
        for competitor in self.swimmers:
            standings.append([competitor, self.finish_time(competitor)])

        standings.sort(key = lambda x: x[1])
        names = list(map(lambda x: x[0], standings))

        if k == ():
            return names[0]
        else:
            return names[:k[0]]
            
        
        
        

        
        

def test3():
    def approx(v1,v2):
        return abs(v1-v2)<0.01
    
    print('=== Q3 ===')
    s1 = SwimmingCompetition()
    s1.add_swimmer("Joseph Schooling", 1.96, 0.39)
    s1.add_swimmer("Laszlo Cseh",1.955, 0.37)
    s1.add_swimmer("Tom Shields",1.953, 0.38)
    s1.add_swimmer("Michael Phelps",1.95, 0.42)
    s1.add_swimmer("Mehdy Metella",1.945, 0.42)
    print(approx(s1.finish_time("Joseph Schooling"),51.41))
    print(approx(s1.finish_time("Laszlo Cseh"),51.52))
    print(approx(s1.finish_time("Tom Shields"),51.58))
    print(approx(s1.finish_time("Michael Phelps"),51.70))
    print(approx(s1.finish_time("Mehdy Metella"),51.83))
    print(s1.winner()=="Joseph Schooling")
    print(s1.winner(2)==['Joseph Schooling', 'Laszlo Cseh'])
    print(s1.winner(5)==['Joseph Schooling', 'Laszlo Cseh', 'Tom Shields', 'Michael Phelps', 'Mehdy Metella'])
    print(s1.winner(6)==['Joseph Schooling', 'Laszlo Cseh', 'Tom Shields', 'Michael Phelps', 'Mehdy Metella'])

    print(approx(s1.get_position("Joseph Schooling",0),0.0))
    print(approx(s1.get_position("Joseph Schooling",10),19.6))
    print(approx(s1.get_position("Joseph Schooling",25.5),49.98))
    print(approx(s1.get_position("Joseph Schooling",25.7),50))
    print(approx(s1.get_position("Joseph Schooling",25.8),50))
    print("check")
    print(approx(s1.get_position("Joseph Schooling",26),49.80))
    print(approx(s1.get_position("Joseph Schooling",27),47.84))
    print(approx(s1.get_position("Joseph Schooling",50),2.76))
    print(approx(s1.get_position("Joseph Schooling",60),0))

    s2 = SwimmingCompetition(1,3)
    s2.add_swimmer("Joseph Schooling", 1.96, 0.39)
    s2.add_swimmer("Laszlo Cseh",1.955, 0.37)
    s2.add_swimmer("Tom Shields",1.953, 0.38)
    print(s2.add_swimmer("Michael Phelps",1.95, 0.42)=="No more lanes!")
    print(s2.add_swimmer("Mehdy Metella",1.945, 0.42)=="No more lanes!")
    print(s2.winner()=="Joseph Schooling")
    print(s2.winner(2)==['Joseph Schooling', 'Laszlo Cseh'])
    print(s2.winner(4)==['Joseph Schooling', 'Laszlo Cseh', 'Tom Shields'])
    print(s2.get_position("Trump",0)=="No such swimmer")

test3()
            

