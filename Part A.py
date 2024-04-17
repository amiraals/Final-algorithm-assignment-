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
    content_choices = list(PostContent)
    for _ in range(n):
        delta = timedelta(days=random.randint(1, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        post_datetime = base_datetime + delta
        content = random.choice(content_choices)
        user = f"User{random.randint(1, 10)}"
        views = random.randint(1, 1000)
        post = Post(post_datetime, content, user, views)
        posts.append(post)
    return posts

def create_data_structures(posts):
    post_dict = {}
    root = None
    
    for post in posts:
        post_dict[post.datetime] = post
        if root is None:
            root = Node(post)
        else:
            root.insert(post)
    
    return post_dict, root

def find_post_by_datetime(post_dict):
    datetime_str = input("Enter the datetime of the post (format YYYY-MM-DD HH:MM:SS): ")
    try:
        datetime_obj = datetime.fromisoformat(datetime_str)
        post = post_dict.get(datetime_obj, None)
        if post:
            print(f"Found Post: {post}")
        else:
            print("No post found with that datetime.")
    except ValueError:
        print("Invalid datetime format.")

def display_all_posts(posts):
    if posts:
        for post in posts:
            print(post)
    else:
        print("No posts available.")

class Node:
    def __init__(self, post):
        self.post = post
        self.left = None
        self.right = None

    def insert(self, post):
        if post.datetime < self.post.datetime:
            if self.left is None:
                self.left = Node(post)
            else:
                self.left.insert(post)
        else:
            if self.right is None:
                self.right = Node(post)
            else:
                self.right.insert(post)

    def find_in_range(self, start_datetime, end_datetime, results):
        if self.left is not None:
            self.left.find_in_range(start_datetime, end_datetime, results)
        if start_datetime <= self.post.datetime <= end_datetime:
            results.append(self.post)
        if self.right is not None:
            self.right.find_in_range(start_datetime, end_datetime, results)


def find_posts_in_range(root):
    start_str = input("Enter the start datetime (format YYYY-MM-DD HH:MM:SS): ")
    end_str = input("Enter the end datetime (format YYYY-MM-DD HH:MM:SS): ")

    start_str_iso = start_str.replace(" ", "T")
    end_str_iso = end_str.replace(" ", "T")

    try:
        start_datetime = datetime.fromisoformat(start_str_iso)
        end_datetime = datetime.fromisoformat(end_str_iso)
        results = []
        root.find_in_range(start_datetime, end_datetime, results)
        if results:
            for post in results:
                print(post)
        else:
            print("No posts found in that range.")
    except ValueError:
        print("Invalid datetime format. Please enter the datetime in the correct format (YYYY-MM-DD HH:MM:SS).")



def run_menu(post_dict, root, posts):
    while True:
        print("\nMenu:")
        print("1. Find post by datetime")
        print("2. Find posts in datetime range")
        print("3. Display all posts")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            find_post_by_datetime(post_dict)
        elif choice == '2':
            find_posts_in_range(root)
        elif choice == '3':
            display_all_posts(posts)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")
            
def main():
    num_posts = int(input("Enter the number of posts to generate: "))
    posts = generate_random_posts(num_posts)
    post_dict, root = create_data_structures(posts)
    run_menu(post_dict, root, posts)

main()
