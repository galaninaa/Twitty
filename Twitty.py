import array
import urllib
import TwitterAPI
from pprint import pprint
import json
import binascii
import string
import oauth
import ast
from urllib2 import Request, urlopen, URLError

url = "https://api.twitter.com"

Access_Token = "727966279-lqrD5BwFZ4ZKuybId7Z3vdH10CGUhYvD7dKmpPFh"
Access_Token_Secret = "uZjY7uLwIkiPEZyjCZgPLQxL074esv72gWl8kW76EABit"

Consumer_Key = "dW8xwSw28Hf9ZRZxSbBXixpLg"
Consumer_Secret = "jWRrYeIGLD4SqgfwTscv33ULBY4cve9dYOVpMMNrHkKZ6AfMQg"

    #address =  urllib.request.(url + "/1.1/account/verify_credentials.json")

API = TwitterAPI.TwitterAPI(Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret)
json_ = TwitterAPI.TwitterRestPager(oauth,"Galanin_Anton")
    #request = API.request("friends/ids")
    #json_= request.json()
    #print(json_)
'''
request = API.request("friends/list")
json_= request.json()
pprint.pprint(json_)
for users in json_['users']:
    print 'ID', ':', users['id']
    print 'NAME', ':',users['name']
'''

def get_picture(user='@thegrandtour', count=100):
    request = API.request('search/tweets', params = {'q':user,'since_id':'92727851','count':count})
    json_= request.json()
    start = 'u\'media_url\': u\''
    i=1
    for contributors in json_['statuses']:
        try:
            res = contributors['entities']['media']
            srt = str(res)
            #srt = srt.replace('[','')
            #srt = srt.replace(']','')
            #srt = srt.replace('u\'','\'')
            srt = srt[1:len(srt)-1]
            dic = ast.literal_eval(srt)
            print dic[u'media_url_https']
            request_image = Request(dic[u'media_url_https'])
            try:
                response_image = urlopen(request_image)
                load_image = response_image.read()
                f = open('picture'+str(i)+'.jpg','w')
                f.write(load_image)
                f.close()
                print "Done!"
                i+=1
            except:
                print ''
        except:
            pprint('-----------')


def get_status(user='@Galanin_Anton', count=100):
    request = API.request('favorites/list',params = {'screen_name':user})
    json_= request.json()
    pprint(json_)


def get_user_show(user_id='684031588745777154', screen_name='@RichardHammond'):
    request = API.request('users/show',params = {'user_id':user_id,'screen_name':screen_name})
    json_= request.json()
    pprint(json_)


def get_followers(user_id='684031588745777154', screen_name='@RichardHammond'):
    request = API.request('friends/list', params = {'user_id':user_id,'screen_name':screen_name,'count':200})
    json_req = request.json()

    friends = {}
    count = 0
    for friend in json_req['users']:
        new_friend= {'name':friend['name'],'id':friend['id'],'screen_name':friend['screen_name']}
        friends[count]=new_friend
        count+=1
    #pprint(friends)
    return friends,count

    #pprint(json_)


friends,count = get_followers(user_id='757305452539633664',screen_name='@Galanin_Anton')
#pprint(friends)
for user_data in friends.values() :
    friends_of_my_friends,friends_count=get_followers(user_data['id'],user_data['screen_name'])
    print friends_of_my_friends
    print friends_count
    print '------------------------------------------------'






'''
    start = 'u\'media_url\': u\''
    i=1
    for contributors in json_['statuses']:
        try:
            res = contributors['entities']['media']
            srt = str(res)
            #srt = srt.replace('[','')
            #srt = srt.replace(']','')
            #srt = srt.replace('u\'','\'')
            srt = srt[1:len(srt)-1]
            dic = ast.literal_eval(srt)
            print dic[u'media_url_https']
            request_image = Request(dic[u'media_url_https'])
            try:
                response_image = urlopen(request_image)
                load_image = response_image.read()
                f = open('picture'+str(i)+'.jpg','w')
                f.write(load_image)
                f.close()
                print "Done!"
                i+=1
            except:
                print ''
        except:
            pprint('-----------')
        '''



'''


f=open('Screenshot_2016-02-08-15-41-38.png','rb')
with f:
    r = f.read()
    #print binary
#res = bin(r)

request = API.request('media/upload',params = 'media')
print request.status_code

'''
