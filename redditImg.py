import json
import requests
from urllib.parse import urlparse
from os import path, makedirs
import shutil


def downloadImages(subreddit, folder, amount = 15, modifier = 'hot', datafile = 'ids.json'):
    whitelist = ['png', 'jpg', 'jpeg']
    ids = []
    posts = []

    # create folder path, if it not already exists
    makedirs(folder, exist_ok = True)

    # read ids from already downloaded images
    try:
        with open(path.join(folder, datafile), 'r') as f:
            ids = json.load(f)
    except:
        pass

    # get posts
    if modifier == 'new':
        posts = subreddit.new(limit = amount)
    elif modifier == 'top':
        posts = subreddit.top(limit = amount)
    else:
        posts = subreddit.hot(limit = amount)

    # download all attached images
    for p in posts:
        filename = urlparse(p.url)[2].split("/")[-1]
        suffix = filename.split(".")[-1]

        # if not whitelisted, continue to next post
        # TODO: optimize somehow, that urls without suffix can also be downloaded
        if (not suffix in whitelist) or p.stickied or (p.id in ids):
            continue

        new_filename = path.normpath(path.join(folder, filename))

        # download file
        r = requests.get(p.url, stream = True)

        if r.status_code == 200:
            with open(new_filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                ids.append(p.id)

    # save new ids into data file
    with open(path.join(folder, datafile), 'w') as f:
        json.dump(ids, f)
