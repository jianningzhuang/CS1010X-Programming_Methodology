#
# CS1010X --- Programming Methodology
#
# Sidequest 12.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010x-fbdata.json contains:

    {
       "members": {
          "data": [
             {
                "name": "Aadit Kamat",
                "id": "1003982836283025"
             },
             {
                "name": "Rakshit Gogia",
                "id": "10204299775189027"
             },
             ...
          ]
       },
       "description": "This is the official FB Group for ...",
       "name": "CS1010X",
       "feed": {
          "data": [
             {
                "message": "Might be useful for the business analytics ...",
                "from": {
                   "name": "Ben Leong",
                   "id": "10152805891837166"
                },
                "name": "Machine Learning with Python - BDU"
                "id": "409054432560329_1002582839874149",
                "likes": {
                   "data": [
                      {
                         "id": "10208170707289199",
                         "name": "Lim Kian Hwee"
                      },
                      {
                         "id": "10204292869386114",
                         "name": "Siidheesh Theivasigamani"
                      },
                      ...
                   ]
                },
                ...
             },
             ...
          ]
       },
       "id": "409054432560329"
    }

    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())

# CS1010X Facebook Group Data as a dictionary object
fb_data = read_json('cs1010x-fbdata.json')

##########
# Task a #
##########

def count_comments(data):
    result = 0
    for post in data["feed"]["data"]:
        if "comments" in post.keys():
            result += len(post["comments"]["data"])
    return result
    

print("Number of Comments in CS1010X: ", count_comments(fb_data))

##########
# Task b #
##########

def count_likes(data):
    result = 0
    for post in data["feed"]["data"]:
        if "likes" in post.keys():
            result += len(post["likes"]["data"])
        if "comments" in post.keys():
            for info in post["comments"]["data"]:
                result += info["like_count"]
    return result    

print("Number of Likes in CS1010X: ", count_likes(fb_data))

##########
# Task c #
##########

def create_member_dict(data):
    member_by_id = {}
    for member in data["members"]["data"]:
        copy = member.copy()
        member_id = copy.pop("id")
        member_by_id[member_id] = copy
    return member_by_id

        
##        member_data = {}
##        if "gender" in member.keys():
##            member_data["gender"] = member["gender"]
##            member_data["name"] = member["name"]
##        else:
##            member_data["name"] = member["name"]
##        member_by_id[member["id"]] = member_data 
##
##    return member_by_id
            

member_dict = create_member_dict(fb_data)
#print(member_dict["10205702832196255"])

# Q: Why did we choose the id of the member data object to be the key?
# A: id numbers are unique while some people might share the same name
#    id numbers are also immutable in a sense? while we can change our name/have alter egos as i have demonstrated in the previous missions?

# Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
# A: if some people share the same name, the value that goes with that name/key would be overriden and the original member would be lost

##########
# Task d #
##########

def posts_freq(data):
    frequency = {}
    for post in data["feed"]["data"]:
        if post["from"]["id"] in frequency.keys():
            frequency[post["from"]["id"]] += 1
        else:
            frequency[post["from"]["id"]] = 1
    return frequency
            
            
        

#print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########

def comments_freq(data):
    frequency = {}
    for post in data["feed"]["data"]:
        if "comments" in post.keys():
            for info in post["comments"]["data"]:
                if info["from"]["id"] in frequency.keys():
                    frequency[info["from"]["id"]] += 1
                else:
                    frequency[info["from"]["id"]] = 1
    return frequency

#print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########

def likes_freq(data):
    frequency = {}
    for post in data["feed"]["data"]:
        if "likes" in post.keys():
            for liker in post["likes"]["data"]:
                if liker["id"] in frequency.keys():
                    frequency[liker["id"]] += 1
                else:
                    frequency[liker["id"]] = 1
    return frequency


#print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########

def popularity_score(data):
    popularity = {}
    for post in data["feed"]["data"]:
        if "likes" in post.keys():
            if post["from"]["id"] in popularity.keys():
                popularity[post["from"]["id"]] += len(post["likes"]["data"])
            else:
                popularity[post["from"]["id"]] = len(post["likes"]["data"])
        if "comments" in post.keys():
            for info in post["comments"]["data"]:
                if info["like_count"] != 0:
                    if info["from"]["id"] in popularity.keys():
                        popularity[info["from"]["id"]] += info["like_count"]
                    else:
                        popularity[info["from"]["id"]] = info["like_count"]
    return popularity

#print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########

def member_stats(data):
    member_dict = create_member_dict(data)
    for member_id in member_dict.keys():
        if member_id in posts_freq(data):
            member_dict[member_id]["posts_count"] = posts_freq(data)[member_id]
        else:
            member_dict[member_id]["posts_count"] = 0
        if member_id in comments_freq(data):
            member_dict[member_id]["comments_count"] = comments_freq(data)[member_id]
        else:
            member_dict[member_id]["comments_count"] = 0
        if member_id in likes_freq(data):
            member_dict[member_id]["likes_count"] = likes_freq(data)[member_id]
        else:
            member_dict[member_id]["likes_count"] = 0
    return member_dict
            

stats = member_stats(fb_data)
#print(stats["10152805891837166"])

##########
# Task i #
##########

def activity_score(data):
    stats = member_stats(data)
    member_score = {}
    for member_id in stats.keys():
        score = stats[member_id]["posts_count"]*3 + stats[member_id]["comments_count"]*2 + stats[member_id]["likes_count"]
        member_score[member_id] = score
    return member_score
        

scores = activity_score(fb_data)
#print(scores["10153020766393769"]) # => 30
#print(scores["857756387629369"]) # => 8


##########
# Task j #
##########

def active_members_of_type(data, k, type_fn):
    active_members = []
    member_dict = create_member_dict(data)
    fn_dict = type_fn(data)
    for member_id in fn_dict.keys():
        if fn_dict[member_id] >= k and member_id in member_dict.keys():
            active_members.append([member_dict[member_id]["name"], fn_dict[member_id]])
    active_members.sort(key = lambda x: x[0])
    active_members.sort(key = lambda x: x[1], reverse = True)
    return active_members
    
    

#print(active_members_of_type(fb_data, 2, posts_freq))

# print(active_members_of_type(fb_data, 20, comments_freq))

# print(active_members_of_type(fb_data, 40, likes_freq))

# print(active_members_of_type(fb_data, 20, popularity_score))

print(active_members_of_type(fb_data, 80, activity_score))




########### DO NOT REMOVE THE TEST BELOW ###########

def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print('==================')
    answers = json.loads(open('grading.json', 'r',  encoding='utf-8').read())
    total, correct = 0, 0
    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return 'Passed!'
        else:
            return 'Failed.'
            
    print('Testing count_comments... ', pass_or_fail(count_comments(fb_data), answers['count_comments']))
    print('Testing count_likes... ', pass_or_fail(count_likes(fb_data), answers['count_likes']))
    print('Testing create_member_dict... ', pass_or_fail(create_member_dict(fb_data), answers['create_member_dict']))
    print('Testing posts_freq... ', pass_or_fail(posts_freq(fb_data), answers['posts_freq']))
    print('Testing comments_freq... ', pass_or_fail(comments_freq(fb_data), answers['comments_freq']))
    print('Testing likes_freq... ', pass_or_fail(likes_freq(fb_data), answers['likes_freq']))
    print('Testing popularity_score... ', pass_or_fail(popularity_score(fb_data), answers['popularity_score']))
    print('Testing member_stats... ', pass_or_fail(member_stats(fb_data), answers['member_stats']))
    print('Testing activity_score... ', pass_or_fail(activity_score(fb_data), answers['activity_score']))
    print('Testing members with >= 1 posts... ', pass_or_fail(active_members_of_type(fb_data, 1, posts_freq), answers['active_posters']))
    print('Testing members with >= 4 comments... ', pass_or_fail(active_members_of_type(fb_data, 4, comments_freq), answers['active_commenters']))
    print('Testing members with >= 4 likes... ', pass_or_fail(active_members_of_type(fb_data, 4, likes_freq), answers['active_likers']))
    print('Testing members who have >= 3 likes... ', pass_or_fail(active_members_of_type(fb_data, 3, popularity_score), answers['popular']))
    print('Testing members with an activity score of >= 10... ', pass_or_fail(active_members_of_type(fb_data, 10, activity_score), answers['overall_active']))
    print('==================')
    print('Grades: ' + str(correct) + '/' + str(total) + '\n')

gradeit()
