#!/usr/bin/python3
import praw

def top_ten(subreddit):
    try:
        reddit = praw.Reddit(client_id='your_client_id', client_secret='your_client_secret', user_agent='your_user_agent')
        posts = reddit.subreddit(subreddit).hot(limit=10)
        for post in posts:
            print(post.title)
    except praw.exceptions.Redirect:
        print("None") 
