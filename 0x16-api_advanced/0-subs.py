#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'YourBotName'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the status code is 200 (OK)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        # Return 0 if the subreddit is invalid or there is another issue
        return 0

# Example usage:
subreddit = 'python'
print(number_of_subscribers(subreddit))  # Output the number of subscribers for the 'python' subreddit

