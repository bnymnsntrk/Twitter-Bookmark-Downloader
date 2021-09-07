'''
A script that downloads all the pictures posted by a given user.

Author: Krishanu Konar
email: krishh_konar

'''

import API_Tokens as t
from tweepy import OAuthHandler, API, Stream
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
        id = full_twt[full_twt.find("status") + 7:]
        tweet = api.get_status(id)
        media = tweet.entities.get('media', [])

        if len(media) > 0:
            wget.download((media[0]['media_url']))

    file1.close()
    return all_tweets


def downloadFiles(media_url, username):

    print('\nDownloading Images.....')
    wget.download(media_url)


def authenticate():
    auth = OAuthHandler(t.CONSUMER_KEY, t.CONSUMER_SECRET)
    auth.set_access_token(t.ACCESS_TOKEN, t.ACCESS_TOKEN_SECRET)
    api = API(auth)
    return api


if __name__ == '__main__':
    main()