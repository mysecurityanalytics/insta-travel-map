import json
import os
import time

import instaloader

L = instaloader.Instaloader()
while True:
    try:
        L.load_session_from_file(os.environ['INSTA_USERNAME'])
        break
    except:
        print("Waiting for login...")
        time.sleep(10)


def get_user_data(username):
    try:
        user = instaloader.Profile.from_username(L.context, username)
    except instaloader.exceptions.ProfileNotExistsException:
        return {"error": "User does not exist."}
    data = {
        "user": {
            "username": user.username,
            "name": user.full_name,
            "bio": user.biography,
            "profilePic": user.profile_pic_url,
            "isPriv": user.is_private,
            "countFollowers": user.followers,
            "countFollowees": user.followees,
            "countMedia": user.mediacount
        },
        "posts": [],
        "connection": []
    }
    for post in user.get_posts():
        if post.location and post.location.lat != None:
            postData = {
                "shortcode": post.shortcode,
                "locationName": post.location.name,
                "caption": "" if (post.caption is None) else post.caption.replace("\n", "\\n").replace("\r", "\\r"),
                "lat": post.location.lat,
                "lng": post.location.lng,
                "thumbnail": post.url,
                "video": post.video_url,
                "time": "" if (post.caption is None) else post.date.strftime("%d/%m/%Y, %H:%M:%S")
            }
            data["posts"].append(postData)
            data['connection'].append([post.location.lat, post.location.lng, 9.8])
    data['posts'].reverse()
    data['connection'].reverse()
    data['connection'] = json.dumps(data['connection'])
    print(data)
    return data


def get_hashtag_data(hashtag):
    data = {"posts": [], "latlngs": ""}
    latlngs = []
    try:
        for post in L.get_hashtag_posts(hashtag):
            if post.location and post.location.lat != None:
                post_data = {
                    "user": post.owner_username,
                    "locationName": post.location.name,
                    "lat": post.location.lat,
                    "lng": post.location.lng,
                    "thumbnail": post.url,
                    "caption": "" if (post.caption is None) else post.caption.replace("\n", "\\n").replace("\r", "\\r"),
                    "video": post.video_url,
                    "time": "" if (post.caption is None) else post.date.strftime("%d/%m/%Y, %H:%M:%S"),
                    "shortcode": post.shortcode
                }
                print(post_data)
                data["posts"].append(post_data)
                latlngs.append([post.location.lat, post.location.lng, 1.0])
            if len(data["posts"]) >= 7:
                break
        data["latlngs"] = str(latlngs)
    except instaloader.exceptions.QueryReturnedNotFoundException:
        return {"error": "Could not find any post."}
    return data
