import random
from enum import Enum
import datetime
import heapq

# Defining post content types using an enumeration for maintainability
class PostContent(Enum):
    NEWS = "Breaking News Update"
    OPINION = "Opinion Piece"
    MEME = "Funny Meme"
    ANNOUNCEMENT = "Important Announcement"
    ADVERTISEMENT = "Sponsored Advertisement"
    STORY = "Personal Story"
    QUOTE = "Inspirational Quote"


class Post:
    """Defining a class to represent a social media post with datetime, content, user, and views"""
    def __init__(self, datetime, content, user, views):
        self.datetime = datetime
        self.content = content
        self.user = user
        self.views = views

    # Providing a string representation for a Post object
    def __str__(self):
        return f"{self.datetime.strftime('%Y-%m-%d %H:%M')}: {self.content.value}, by {self.user} with {self.views} views"


# A function to generate a list of random posts
def generate_random_posts(n):
    posts = []
    content_choices = list(PostContent)
    # Setting a fixed start date and end date for the period during which the posts can be created
    start_date = datetime.datetime(2022, 1, 1, 0, 0)
    end_date = datetime.datetime(2024, 12, 31, 23, 59)

    # Loop over the number of posts to generate (n)
    for i in range(n):
        random_seconds = random.randint(0, (end_date - start_date).total_seconds())
        random_date_time = start_date + datetime.timedelta(seconds=random_seconds)    # The generated datetime has its seconds and microseconds set to zero to normalize the time
        content = random.choice(content_choices)
        user = f"User {i+1}"
        views = random.randint(1, 100000)
        post = Post(random_date_time, content, user, views)
        posts.append(post)
    return posts



# A function to create and initialize data structures used in the program
def create_data_structures(posts):
    post_dict = {}  # Initialize an empty dictionary which will serve as a hash table
    root = None  # Root node for the BST
    max_heap = []  # Max-heap to get the post with most views efficiently

    # Iterating over each post in the list of posts to populate the data structures
    for post in posts:
        key = post.datetime.replace(second=0, microsecond=0)    # Normalizing the datetime key for the hash table to minute precision
        post_dict[key] = post   # Store the post in the hash table with the normalized datetime as the key

        # If this is the first post, it becomes the root of the BST
        # Otherwise insert the post into the BST to maintain the sorted order of posts
        if root is None:
            root = Node(post)
        else:
            root.insert(post)

        # Adding the post to the max-heap, using negative views as the key to create a max-heap
        heapq.heappush(max_heap, (-post.views, post))
    return post_dict, root, max_heap


# A function to find a post by its datetime
def find_post_by_datetime(post_dict):
    # Asking the user for the datetime of the post they wish to find
    datetime_str = input("Enter the datetime of the post (format YYYY-MM-DD HH:MM): ")

    try:
        # Attempting to parse the input string into a datetime object
        datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        # Normalize the datetime object to minute precision by zeroing out seconds and microseconds
        datetime_obj = datetime_obj.replace(second=0, microsecond=0)
        # Retrieving the post from the hash table (post_dict) using the normalized datetime as the key
        post = post_dict.get(datetime_obj, None)

        # If a post is found, print it; otherwise, inform the user that no post was found
        if post:
            print(f"Found Post: {post}")
        else:
            print("No post found with that datetime.")
    except ValueError:
        print("Invalid datetime format.")


# A function to display all posts
def display_all_posts(posts):
    if posts:
        for post in posts:
            print(post)
    else:
        print("No posts available.")


def create_max_heap(posts):
    max_heap = []
    for post in posts:
        heapq.heappush(max_heap, (-post.views, post))  # Use negative views for max heap
    return max_heap

def find_post_with_most_views(max_heap):
    if max_heap:
        views, post = max_heap[0]
        return post
    else:
        return None

# Node class for a binary search tree (BST)
class Node:
    def __init__(self, post):
        self.post = post
        self.left = None
        self.right = None

    # Insert method to add posts to the BST
    def insert(self, post):
        # Comparison is made based on the year and month
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

    # A method to find and return posts within a specific datetime range.
    def find_in_range(self, start_datetime, end_datetime, results):
        if self.left is not None:
            self.left.find_in_range(start_datetime, end_datetime, results)

        if (start_datetime.year, start_datetime.month) <= (self.post.datetime.year, self.post.datetime.month) <= (
        end_datetime.year, end_datetime.month):
            results.append(self.post)

        if self.right is not None:
            self.right.find_in_range(start_datetime, end_datetime, results)

# A function to find posts within a given range of datetimes.
def find_posts_in_range(root):
    # Prompt the user for the start and end dates of the range.
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


# Menu function to navigate through the application.
def run_menu(post_dict, root, max_heap, posts):
    while True:
        print("\nMenu:")
        print("1. Find post by datetime")
        print("2. Find posts in datetime range")
        print("3. Display post with most views")
        print("4. Display all posts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            find_post_by_datetime(post_dict)
        elif choice == '2':
            find_posts_in_range(root)
        elif choice == '3':
            post_with_most_views = find_post_with_most_views(max_heap)
            if post_with_most_views:
                print(f"Post with the most views: {post_with_most_views}")
            else:
                print("No posts available.")
        elif choice == '4':
            display_all_posts(posts)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")


def main():
    num_posts = int(input("Enter the number of posts to generate: "))
    posts = generate_random_posts(num_posts)
    display_all_posts(posts)
    post_dict, root, max_heap = create_data_structures(posts)
    run_menu(post_dict, root, max_heap, posts) 

main()
