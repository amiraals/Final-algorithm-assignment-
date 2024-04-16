import random
from datetime import datetime, timedelta
from enum import Enum


class PostContent(Enum):
    NEWS = "Breaking News Update"
    OPINION = "Opinion Piece"
    MEME = "Funny Meme"
    ANNOUNCEMENT = "Important Announcement"
    ADVERTISEMENT = "Sponsored Advertisement"
    STORY = "Personal Story"
    QUOTE = "Inspirational Quote"

class Post:
    def __init__(self, datetime, content, user, views):
        self.datetime = datetime
        self.content = content
        self.user = user
        self.views = views
    
    def __str__(self):
        return f"{self.datetime}: {self.content.value}, by {self.user} with {self.views} views"
        
def generate_random_posts(n):
    base_datetime = datetime.now()
    posts = []
    for _ in range(n):
        delta = timedelta(days=random.randint(1, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        post_datetime = base_datetime + delta
        content = f"Post content {_}"
        user = f"User{random.randint(1, 10)}"
        views = random.randint(1, 1000)
        post = Post(post_datetime, content, user, views)
        posts.append(post)
    return posts


def display_all_posts(posts):
    if posts:
        for post in posts:
            print(post)
    else:
        print("No posts available.")

def run_menu(post_dict, post_bst, max_heap, posts):
    while True:
        print("\nSocial Media posts management:")
        print("1. Display all posts")
        print("2. Find posts in datetime range")
        print("3. Get post with most views")
        print("4. Find post by datetime")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            display_all_posts(posts)
        elif choice == '2':
            # call function 
        elif choice == '3':
            # call function 
        elif choice == '4':
            # call function 
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")
