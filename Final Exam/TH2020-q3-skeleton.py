# function 1
def make_empty_db(): 
    return () 

# function 2
def add_person(db, name, home, workplace, caseType):
    pRec = (name, home, workplace, caseType) 
    return db + (pRec,) 

# function 3
def remove_person(db, name):
    temp = db
    db = ()
    for p in temp:
        if name==get_name(p):
            continue
        db = db + (p,)
    return db


# function 4
def same_home_or_office_as(db, name):
    pRec = find_record(db, name)
    pHome = get_home(pRec)
    pOffice = get_workplace(pRec)
    result = ()
    for p in db:
        if name == get_name(p):
            continue
        if get_home(p)==pHome or get_workplace(p)==pOffice or \
           get_home(p)==pOffice or get_workplace(p)==pHome:
            result += (get_name(p),)
    return result

# function 5
def add_visited_places(db, name, places):
    pRec = find_record(db, name)
    for p in places:
        pRec += (p,)
    db = remove_person(db, name)
    return add_record(db, pRec)

# function 6
def same_visited_places_as(db, name):
    pRec = find_record( db, name )
    places = pRec[4:]
    result=()
    for person in db:
        for l in person[4:]:
	        if l in places and get_name(person) != name:
		        result += (person[0], )
    return result 

# function 7
def set_case_to_quarantined(db, name):
    pRec = (find_record(db, name))
    if get_case_type(pRec) == "c":
        print("Already confirmed before:", name, "-- no quarantined needed")
        return db
    if get_case_type(pRec) == "q":
        print("Already quarantined before:", name)
        return db
    pRec = set_case_type(pRec, "q")
    db = remove_person(db, name)
    db = add_record(db, pRec)
    print("Done quarantine:", name)
    return db

# function 8
def set_case_to_confirm(db, name):
    pRec = (find_record(db, name))
    pRec = set_case_type(pRec, "c") 
    db = remove_person(db, name)
    db = add_record(db, pRec)
    print("Done confirm:", name)
    people_to_quarantine = same_home_or_office_as(db, name) + \
           same_visited_places_as(db, name)
    for p in people_to_quarantine:
        db = set_case_to_quarantined(db, p)
    return db

#### starting of other helper functions
def find_record(db, name):
    for p in db:
        if name==get_name(p):
            return p
        
def add_record(db, pRec):
    return db + (pRec, )

def get_name(pRec):
    return pRec[0]

def get_home(pRec):
    return pRec[1]

def get_workplace(pRec):
    return pRec[2]

def get_case_type(pRec):
    return pRec[3]

def set_case_type(pRec, t):
    rec = pRec[:3] + (t,) + pRec[4:]
    return rec
## ending of helper functions

# Question 3
##
## Sample Execution - material similar to midterm
##
print("======== Question 3 =========")
print("==== Sample Execution -- Midterm stuff ====")

print("")

db = make_empty_db()
db = add_person( db, "Alice", "H01", "W01", "n")
db = add_person( db, "Ben", "H01", "W02", "n")
db = add_person( db, "Cathy", "H03", "W01", "n")
db = add_person( db, "Dennis", "H04", "H03", "n")
db = add_person( db, "John", "H04", "W01", "n" )
db = add_person( db, "Kevin", "H06", "W06", "n" )
print( same_home_or_office_as( db, "Alice" ) )  # ('Ben', 'Cathy', 'John')
print( same_home_or_office_as( db, "Dennis" ) ) # ('Cathy', 'John')
db = add_visited_places( db, "Dennis", ("VivoCity", "SAFRA", "Jurong East") )
db = add_visited_places( db, "Ben", ("SAFRA", "NUS") )
print( same_visited_places_as(db, "Dennis")) # ('Ben',)


## A
print("")
print("======== Question 3A =========")
print("explain your answer in the box provided in coursemology")
print("")

my clusterDB is a list of clusters, which is made up of a dictionary of people in the cluster
each person in the dictionary is linked to their case_number and linked_to values by another dictionary

for example [{('Dennis', 'H04', 'H03', 'c', 'VivoCity', 'SAFRA', 'Jurong East'): {'case_number': 1, 'linked_to': 0}, ('John', 'H04', 'W01', 'c'): {'case_number': 2, 'linked_to': 1}},
{('Kevin', 'H06', 'W06', 'c'): {'case_number': 3, 'linked_to': 0}}]

## B
print("======== Question 3B =========")
print("write your code and cut-and-paste to coursemology")
print("")
## B(i)
def make_empty_clusterDB():
    return []

## B(ii)
def get_number_of_cases(clusterDB):
    seen = []
    for cluster in clusterDB:
        for person in cluster:
            name = get_name(person)
            if name not in seen:
                seen.append(name)
    return len(seen)

## B(iii)
def get_number_of_clusters(clusterDB):
    return len(clusterDB)

## B(iv)
def get_people_in_largest_cluster(clusterDB):
    largest = None
    max_val = None
    for cluster in clusterDB:
        if max_val == None or len(cluster) > max_val:
            max_val = len(cluster)
            largest = cluster
    result = ()
    for person in largest:
        result += (get_name(person), )
    return result

## C
print("======== Question 3C =========")
print("write your code and cut-and-paste to coursemology")
print("")
def add_person_to_clusterDB(db, clusterDB, name):
    p = find_record(db, name)
    case_number = get_number_of_cases(clusterDB) + 1
    contact = []
    for person in same_home_or_office_as(db, name):
        if find_record(db, person) not in contact:
            contact.append(find_record(db, person))
    for person1 in same_visited_places_as(db, name):
        if find_record(db, person1) not in contact:
            contact.append(find_record(db, person1))
    found = False
    for cluster in clusterDB:
        for person2 in cluster:
            if person2 in contact:
                cluster[p] = {}
                cluster[p]["case_number"] = case_number
                cluster[p]["linked_to"] = cluster[person2]["case_number"]
                found = True
                break
    if found == False:
        clusterDB.append({p:{"case_number" : case_number, "linked_to" : 0}})
    return clusterDB
        
        

##########################
##
## Sample Execution
##
##########################
print("==== Sample Execution -- Clustering ====")
clusterDB = make_empty_clusterDB()
db = set_case_to_confirm( db, "Dennis")
#Done confirm: Dennis
#Done quarantine: Cathy
#Done quarantine: John
#Done quarantine: Ben

# Adding Dennis into the cluster database
clusterDB = add_person_to_clusterDB(db, clusterDB, "Dennis")
print("Number of confirmed cases:", get_number_of_cases(clusterDB))
#Number of confirmed cases: 1
print("Number of clusters:", get_number_of_clusters(clusterDB))
#Number of clusters: 1

# Second confirmed case: John, in the same cluster as Dennis
db = set_case_to_confirm( db, "John")
#Done confirm: John
#Done quarantine: Alice
#Already confirmed before: Dennis -- no quarantined needed
#Already quarantined before: Cathy
clusterDB = add_person_to_clusterDB(db, clusterDB, "John")
print("Number of confirmed cases:", get_number_of_cases(clusterDB))
#Number of confirmed cases: 2
print("Number of clusters:", get_number_of_clusters(clusterDB))
#Number of clusters: 1

# Third confirmed case: Kevin, forming a new cluster
db = set_case_to_confirm( db, "Kevin")
#Done confirm: Kevin
clusterDB = add_person_to_clusterDB(db, clusterDB, "Kevin")
print("Number of confirmed cases:", get_number_of_cases(clusterDB))
#Number of confirmed cases: 3
print("Number of clusters:", get_number_of_clusters(clusterDB))
#Number of clusters: 2

# Find the people in the largest cluster. If there are more than one such 
# cluster, just take anyone of them to list out the people in the cluster
print( get_people_in_largest_cluster(clusterDB))
#('Dennis', 'John')




