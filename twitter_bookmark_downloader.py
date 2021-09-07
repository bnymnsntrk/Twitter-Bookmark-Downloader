'''
A script that downloads all the pictures from twitter links given in a file.

Original Author: Krishanu Konar
Edited by: Bunyamin Senturk

'''

import API_Tokens as t
from tweepy import OAuthHandler, API
import os
import wget


def main():
    file1 = open("bookmarks.txt", "r")
    try:
        os.mkdir('bookmarks')
        os.chdir('bookmarks')
    except:
        os.chdir('bookmarks')

    api = authenticate()
    getTweets(api, file1)


def getTweets(api, file1):
    count = 0

    while True:
        count += 1
        full_twt = file1.readline()
        id = full_twt[full_twt.find("status") + 7:]  # id of a tweet starts from "status/"
        tweet = api.get_status(id)  # fetch the tweet
        media = tweet.entities.get('media', [])  # get the media info

        if len(media) > 0:
            wget.download((media[0]['media_url']))  # download the image if media exists

    file1.close()
    return all_tweets


def authenticate():     # developer access
    auth = OAuthHandler(t.CONSUMER_KEY, t.CONSUMER_SECRET)
    auth.set_access_token(t.ACCESS_TOKEN, t.ACCESS_TOKEN_SECRET)
    api = API(auth)
    return api


if __name__ == '__main__':
    main()
