'''
A script that downloads all the pictures posted by a given user.

Author: Krishanu Konar
email: krishh_konar

'''

import API_Tokens as t
import json
from tweepy import OAuthHandler, API, Stream
import os
import wget
import sys
import json
import requests


def main():

    # Authentication
    api = authenticate()

    id = 1432845048316669952
    tweet = api.get_status(id)

    tweets_with_media = set()
    media = tweet.entities.get('media', [])
    if len(media) > 0:
        tweets_with_media.add(media[0]['media_url'])
        sys.stdout.write("\rMedia Links fetched: %d" % len(tweets_with_media))
        sys.stdout.flush()

    downloadFiles(tweets_with_media, "deneme")

    """
    print('\n\nTwitter Image Downloader:\n========================\n')
    username = input("\nEnter the twitter handle of the Account to download media from: ")
    max_tweets = int(input("\nEnter Max. number of tweets to search (0 for all tweets): "))

    all_tweets = getTweetsFromUser(username, max_tweets, api)
    # print(all_tweets)
    # file1.write(str(all_tweets))

    media_URLs = getTweetMediaURL(all_tweets)
    # print(media_URLs)
    # file2.write(str(media_URLs))

    downloadFiles(media_URLs, username)
    print('\n\nFinished Downloading.\n')
    
    """


def getTweetMediaURL(all_tweets):
    print('\nCollecting Media URLs.....')
    tweets_with_media = set()
    for tweet in all_tweets:
        media = tweet.entities.get('media', [])
        if len(media) > 0:
            tweets_with_media.add(media[0]['media_url'])
            sys.stdout.write("\rMedia Links fetched: %d" % len(tweets_with_media))
            sys.stdout.flush()
    print('\nFinished fetching ' + str(len(tweets_with_media)) + ' Links.')

    return tweets_with_media


def downloadFiles(media_url, username):

    print('\nDownloading Images.....')
    try:
        os.mkdir('bookmarks')
        os.chdir('bookmarks')
    except:
        os.chdir('bookmarks')

    try:
        os.mkdir(username)
        os.chdir(username)
    except:
        os.chdir(username)

    for url in media_url:
        wget.download(url)


def authenticate():
    auth = OAuthHandler(t.CONSUMER_KEY, t.CONSUMER_SECRET)
    auth.set_access_token(t.ACCESS_TOKEN, t.ACCESS_TOKEN_SECRET)
    api = API(auth)
    return api


if __name__ == '__main__':
    main()
