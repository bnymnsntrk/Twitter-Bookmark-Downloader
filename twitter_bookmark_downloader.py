'''
A script that downloads all the pictures from twitter links given in a file.

Author: Bunyamin Senturk
Inspired by: Krishanu Konar

'''

import API_Tokens as t
from tweepy import OAuthHandler, API
import os
import wget
import time
import progressbar


def main():

    file1 = open("bookmarks.txt", "r")
    line_count = 0
    for line in file1:
        if line != "\n":
            line_count += 1
    file1.seek(0)
    print("Found ", line_count, " links.")

    try:
        os.mkdir('bookmarks')
        os.chdir('bookmarks')
    except:
        os.chdir('bookmarks')

    api = authenticate()
    getTweets(api, file1, line_count)
    file1.close()


def getTweets(api, file1, line):

    count = 0
    inv_count = 0
    for i in progressbar.progressbar(range(line), redirect_stdout=True):
        full_twt = file1.readline()
        twid = full_twt[full_twt.find("status") + 7:]  # id of a tweet starts from "status/"
        try:
            tweet = api.get_status(twid)  # fetch the tweet
            media = tweet.entities.get('media', [])  # get the media info
            if len(media) > 0:
                count += 1
                wget.download((media[0]['media_url']))  # download the image if media exists
                time.sleep(0.1)
        except:
            inv_count += 1
    print(count, " images downloaded successfully, ", inv_count, " of the links were invalid")

def authenticate():  # developer access

    auth = OAuthHandler(t.CONSUMER_KEY, t.CONSUMER_SECRET)
    auth.set_access_token(t.ACCESS_TOKEN, t.ACCESS_TOKEN_SECRET)
    api = API(auth)
    return api


if __name__ == '__main__':
    main()
