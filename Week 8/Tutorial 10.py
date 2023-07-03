###Question 1

def collatz_distance(n):
    if n == 1:
        return 0
    else:
        if n%2 == 0:
            return 1 + collatz_distance(n//2)
        else:
            return 1 + collatz_distance(3*n + 1)

#print(collatz_distance(27))

###Question 2

def max_collatz_distance(n):
    max_distance = None
    for i in range(1, n+1): #enumerate all numbers to find max
        if max_distance == None or collatz_distance(i) > max_distance:
            max_distance = collatz_distance(i)
    return max_distance

#print(max_collatz_distance(18))

###Question 3


memoize_table = {}

def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name] = {}
    table = memoize_table[name]
    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args)
            table[args] = result
            return result
    return helper

def collatz_distance_memo(n):
    def helper(n):
        if n == 1:
            return 0
        else:
            if n%2 == 0:
                return 1 + collatz_distance_memo(n//2)
            else:
                return 1 + collatz_distance_memo(3*n + 1)
    return memoize(helper, "collatz_distance_memo")(n)

def max_collatz_distance_memo(n):
    max_distance = None
    for i in range(1, n+1):
        if max_distance == None or collatz_distance_memo(i) > max_distance:
            max_distance = collatz_distance_memo(i)
    return max_distance

#print(max_collatz_distance_memo(18))

import cProfile
cProfile.run('max_collatz_distance_memo(10000)')
#cProfile.run('max_collatz_distance(10000)')

###Question 4

memo = {}

def max_collatz_distance_memo(n):
    def collatz_distance_memo(n):
        if n in memo:
            return memo[n]
        else:
            if n == 1:
                result = 0
            else:
                if n%2 == 0:
                    result = 1 + collatz_distance_memo(n//2)
                else:
                    result =  1 + collatz_distance_memo(3*n + 1)
            memo[n] = result
        return result
    max_distance = None
    for i in range(1, n+1):
        if max_distance == None or collatz_distance_memo(i) > max_distance:
            max_distance = collatz_distance_memo(i)
    return max_distance

cProfile.run('max_collatz_distance_memo(10000)')

###Question 5

"""
# there could be user related errors such as typing the wrong url
# there could be internet errors such as connection errors
# The HTTP error 404, or more commonly called "404 error", means that the page you are trying to open could not be found on the server. 
# This is a client-side incident which means either the page has been deleted or moved, and the URL has not been modified accordingly, or that you have misspelled the URL
"""

"""
# you might be redirected to the wrong page if an empty string is returned
# it is good to know what kind of error occurred than just returning the wrong output
"""

from urllib.request import urlopen
from urllib.parse import urlsplit
from urllib.error import *


from urllib.request import urlopen
from urllib.parse import urlsplit
from urllib.error import *

class InternetFail(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value) 
## Do not remove the lines above.

def httpget(url):
    parsed = urlsplit(url)
    if not parsed.scheme: #protocol insertion
        url = 'http://'+url
    elif parsed.scheme != 'http':
        raise ValueError("Unknown protocol")
    # Your code here
    try:
        return urlopen(url).read()
    except HTTPError as err:
        raise InternetFail("Internet Fail " + str(err))
    except URLError as err:
        raise ValueError("Value Error " + str(err))


#print(httpget("w.facebook.co"))


URLS = [["","impossible.txt"],["http://google.com/cs1010fc","fail.txt"]]

def download_URLs(URL_filenames):
    for file in URL_filenames:
        url, filename = file
        try:
            contents = httpget(url)
            with open(filename, 'wb') as myFile: 
                myFile.write(contents)
        except (InternetFail, ValueError) as err:
            print("Could not open " + str(url) + str(err))

print(download_URLs(URLS))























