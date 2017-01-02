# Reddit image downloader for a specific subreddit

This small library can be used to download the image submission on a specific subreddit.
Dependencies:
- praw
- requests

## Example
```python
import redditImg
import praw

reddit = praw.Reddit(
  client_id = CLIENT_ID,
  client_secret = CLIENT_SECRET,
  user_agent = USER_AGENT_STRING)

redditImg.downloadImages(reddit.subredit('earthporn'), './images')
```

Parameters for dowloadImages:
- ```subreddit``` instance of ```praw.models.Subreddit``` from which to download the images
- ```downloadFolder``` path to the folder in which the images will be stored (will be created if it does not exist)
- ```amount = 15``` number of  images to download
- ```modifier = 'hot'``` possible values: ```'top'|'hot'|'new'```
- ```datafile = 'ids.json'``` The filename in which the ids of the already downloaded images are stored. Will be created in the ```downloadFolder```.

See the example file ```example.py``` for more information.
