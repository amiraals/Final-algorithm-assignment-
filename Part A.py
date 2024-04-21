import random
from enum import Enum
import datetime


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
        return f"{self.datetime.strftime('%Y-%m-%d %H:%M')}: {self.content.value}, by {self.user} with {self.views} views"


def generate_random_posts(n):
    posts = []
    content_choices = list(PostContent)
    start_date = datetime.datetime(2022, 1, 1, 0, 0)
    end_date = datetime.datetime(2024, 12, 31, 23, 59)
    for _ in range(n):
        random_seconds = random.randint(0, (end_date - start_date).total_seconds())
        random_date_time = start_date + datetime.timedelta(seconds=random_seconds)
        content = random.choice(content_choices)
        user = f"User {random.randint(1, 10)}"
        views = random.randint(1, 1000)
        post = Post(random_date_time, content, user, views)
        posts.append(post)
    return posts


def create_data_structures(posts):
    post_dict = {}
    root = None
    for post in posts:
        key = post.datetime.replace(second=0, microsecond=0)
        post_dict[key] = post
        if root is None:
            root = Node(post)
        else:
            root.insert(post)
    return post_dict, root


def find_post_by_datetime(post_dict):
    datetime_str = input("Enter the datetime of the post (format YYYY-MM-DD HH:MM): ")
    try:
        datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")  # Adjust to match input format without seconds
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
        if (post.datetime.year, post.datetime.month) < (self.post.datetime.year, self.post.datetime.month):
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

        if (start_datetime.year, start_datetime.month) <= (self.post.datetime.year, self.post.datetime.month) <= (
        end_datetime.year, end_datetime.month):
            results.append(self.post)

        if self.right is not None:
            self.right.find_in_range(start_datetime, end_datetime, results)


def find_posts_in_range(root):
    start_str = input("Enter the start year and month (format YYYY-MM): ")
    end_str = input("Enter the end year and month (format YYYY-MM): ")

    try:
        start_datetime = datetime.datetime.strptime(start_str + "-01",
                                                    "%Y-%m-%d")  # Default to the first day of the start month
        end_datetime = datetime.datetime.strptime(end_str + "-01",
                                                  "%Y-%m-%d")  # Default to the first day of the end month

        results = []
        root.find_in_range(start_datetime, end_datetime, results)
        if results:
            for post in results:
                print(post)
        else:
            print("No posts found in that range.")
    except ValueError:
        print("Invalid datetime format. Please enter the datetime in the correct format (YYYY-MM).")


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
