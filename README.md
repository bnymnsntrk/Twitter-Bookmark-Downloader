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
Install chrome extension from here https://chrome.google.com/webstore/detail/dewey/occohfgiljdagdmklhpplgmcnliljmgi and grab your bookmarks. (Go to https://twitter.com/i/bookmarks and click on the button above, if you don't see it restart your browser.) 
![Step 1](https://i.imgur.com/zamrINN.jpg)

Now click on the dewey icon on top right of the browser and click your bookmarks. Don't click on "select all" yet, because it only applies it to a few pages. You need to slide until there is no more pages left (yeah this is a pain but believe me this is the best way). Then select all and export to clipboard. 
![Step 2](https://i.imgur.com/5NyNA9F.jpg)
![Step 3](https://i.imgur.com/7Ndcqge.jpg)

Create a file in the same directory where python files located and name it "bookmarks.txt". Paste the links you got from dewey here.

Edit the `API_Tokens.py` file and add all the 4 tokens you got in the previous step and save.
Run the script by `python twitter_image_downloader.py`

If everything is ok, when you run the code it will save all the images in a folder called "bookmarks". 

