# Twitter Bookmark Downloader
Downloads images/photos from links given in a file.

### Dependencies

This tool uses the Python [tweepy](www.tweepy.org) library and [wget](https://www.gnu.org/software/wget/) package.

You can install requirements using `requirements.txt`.

`pip install -r requirements.txt`

You will also need to create an app account on https://dev.twitter.com/apps to get authorization tokens

1. Sign in with your Twitter account
2. Create a new app account
3. Fill necessary details
4. Generate a new OAuth token with those permissions

Following these steps will create 4 tokens that you will need to authenticate your account.

### How to Use
Edit the `API_Tokens.py` file and add all the 4 tokens you got in the previous step and save.
Run the script by `python twitter_image_downloader.py`

If everything is ok, when you run the code it will save all the images in a folder called "bookmarks". 

