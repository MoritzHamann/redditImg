import redditImg
import praw
import json

# main function if file is executed directly
if __name__ == '__main__':

    """
    load credentials for reddit
    creds.json has the following structure:
    {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "user_agent": USER_AGENT_STRING,
    }
    """
    creds = {}
    with open('creds.json', 'r') as f:
        creds = json.load(f)

    # instantiate
    reddit = praw.Reddit(**creds)

    # download latest 15 images from earthporn
    redditImg.downloadImages(reddit.subreddit('earthporn'), './images')
