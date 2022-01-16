import requests
import json
import time

# parameters / variables
sub='mentalhealth'
after = '1577836800' # January 1 2020
before = '1577923199' # 24hs later
redditPostData = [] # stores all post data
redditCommentData = [] # stores all comment data



# returns data on all reddit posts of a subreddit from a start date to an end date, caps at ~100 posts
def getRedditPostData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub) # generate api url
    print(url)
    r = requests.get(url) # make api call
    data = json.loads(r.text) # convert json data to python dictionary object
    return data['data'] # returns data as list

# returns reddit post data from a given subreddit and within a given time frame
def getFullPostData(after, before, sub):
    postData = [];
    nextPostData = getRedditPostData(after, before, sub) # get first ~100 posts

    # continuously update start date -> get post data, until all post data is collected
    count = 0
    while len(nextPostData) > 0:
        postData = postData + nextPostData
        print(len(postData))
        after = nextPostData[-1]['created_utc']
        nextPostData = getRedditPostData(after, before, sub)
        count+=1
        if(count % 5 == 0): # throttle amount of api calls
            time.sleep(5)
            continue
        else:
            continue
    
    return postData



# returns data on all reddit comments within a subreddit from a start date to an end date, caps at ~100 comments
def getRedditCommentData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/comment/?size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub) # generate api url
    print(url)
    r = requests.get(url) # make api call
    data = json.loads(r.text) # convert json data to python dictionary object
    return data['data'] # returns data as list

# returns reddit comment data from a given subreddit and within a given time frame
def getFullCommentData(after, before, sub):
    commentData = []
    nextCommentData = getRedditCommentData(after, before, sub) # get first ~100 comments

    # continuously update start date -> get comment data, until all comment data is collected
    count = 0
    while len(nextCommentData) > 0:
        commentData = commentData + nextCommentData
        print(len(commentData))
        after = nextCommentData[-1]['created_utc']
        nextCommentData = getRedditCommentData(after, before, sub)
        count+=1
        if(count % 5 == 0): # throttle amount of api calls
            time.sleep(5)
            continue
        else:
            continue
    
    return commentData



# returns data on all reddit comments within a subreddit by post ID, caps at ~100 comments
def getRedditCommentDataByPost(link_id, sub):
    url = 'https://api.pushshift.io/reddit/search/comment/?size=1000&link_id='+str(link_id)+'&subreddit='+str(sub) # generate api url
    print(url)
    r = requests.get(url) # make api call
    try:
        data = json.loads(r.text) # convert json data to python dictionary object
        return data['data'] # returns data as list
    except:
        return

# accepts list of post data, returns reddit comment data from posts (max 100 comments per post)
def getFullCommentDataByPost(postData):
    commentData = []
    count = 4
    print(len(postData))
    for post in postData:
        sub = post['subreddit']
        link_id = post['id']
        commentData = commentData + getRedditCommentDataByPost(link_id, sub) # get ~100 comments of post
        print(len(commentData))        
        count+=1
        if(count % 5 == 0): # throttle amount of api calls
            time.sleep(5)
            continue
        else:
            continue
    
    return commentData


redditPostData = getFullPostData(after, before, sub)
redditCommentData = getFullCommentData(after, before, sub)
# redditCommentData = getFullCommentDataByPost(redditPostData)