###Question 1

class Thing(object):
    
    def __init__(self, name):
        self.name = name
        self.owner = None
    
    def is_owned(self):
        return self.owner != None
        
    def get_owner(self):
        return self.owner



### uncomment the lines below ###
#stone = Thing('stone')
#stone2 = Thing('stoning')
#stone2.owner = beng # a Person object whose name is 'beng'
### uncomment the lines above ###

###Question 2

class Thing(object):
    """Put attributes here"""

    def __init__(self, name):
        self.name = name
        self.owner = None
        self.place = None
        
    def get_name(self):
        return self.name
        
    def get_place(self):
        return self.place
        
    def is_owned(self):
        return self.owner != None
        
    def get_owner(self):
        return self.owner


#stone2 = Thing('Stone')
#stone2.owner = beng
#stone2.place = base # a Place object whose name is 'base'

###Question 3

class Thing(MobileObject):
    def __init__(self, name):
        super().__init__(name, None)

    def get_name(self):
        return self.name
        
    def get_place(self):
        return self.place
        
    def is_owned(self):
        return self.owner != None
        
    def get_owner(self):
        return self.owner


# self.place was not initialised in the init function
# need to call super().__init__(name, None)
# get_place function would not work

###Question 5

##ice_cream.__dict__  to get all attributes/fields but not methods

##dir(ice_cream) to get all methods

##help(ice_cream) to show everything including methods inherited from superclass


###Question 6

#not good practice to override attributes by direct access through dot notation
#should use methods to interact with object


###Question 7

#is evaluates to false becasue they are 2 different instances/address in memory


###Question 8

#override __eq__function to compare with name attribute instead of address in memory

##def __eq__(self, other):
##    return isinstance(other, Thing) and self.name == other.name and self.place == other.place

##>>> burger1 = Thing (" burger ")
##>>> burger2 = Thing (" burger ")
##>>> burger1 == burger2
##False
##>>> id(burger1)
##2162713894640
##>>> id(burger2)
##2162714319728
##>>> 


##Are burger1 and burger2 the same object?
##Your answer: No
##
##Would burger1 == burger2 evaluate to True?
##Your answer: they have different id/address in memory 
##
##How would you do it?
##Your answer: override the == comparison with __eq__ function



















    
