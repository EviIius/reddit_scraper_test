import pandas as pd
import praw

# reddit_authorized = praw.Reddit(user_agent= '',
#                      client_id='',
#                      client_secret='',
#                      username='', password='')

reddit_read_only = praw.Reddit(client_id="",         # your client id
                               client_secret="",      # your client secret
                               user_agent="")        # your user agent

subreddit = reddit_read_only.subreddit("Python")
 
# # Display the name of the Subreddit
# print("Display Name:", subreddit.display_name)
 
# # Display the title of the Subreddit
# print("Title:", subreddit.title)
 
# # Display the description of the Subreddit
# print("Description:", subreddit.description)

# for post in subreddit.hot(limit=5):
#     print(post.title)
#     print()


posts = subreddit.top("month")
# Scraping the top posts of the current month
 
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
 
for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
     
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
     
    # The score of a post
    posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    posts_dict["Post URL"].append(post.url)

top_posts = pd.DataFrame(posts_dict)
top_posts

top_posts.to_csv("Top Posts.csv", index=True, )