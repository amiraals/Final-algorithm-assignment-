import random
from enum import Enum
import datetime
import heapq

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

def create_data_structures(posts):
    post_dict = {}
    max_heap = create_max_heap(posts)
    for post in posts:
        key = post.datetime.replace(second=0, microsecond=0)
        post_dict[key] = post
    return post_dict, max_heap

def run_menu(post_dict, max_heap, posts):
    while True:
        print("\nMenu:")
        print("1. Find post by datetime")
        print("2. Find posts in datetime range")
        print("3. Display all posts")
        print("4. Display post with most views")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            find_post_by_datetime(post_dict)
        elif choice == '2':
            find_posts_in_range(post_dict)
        elif choice == '3':
            display_all_posts(posts)
        elif choice == '4':
            post_with_most_views = find_post_with_most_views(max_heap)
            if post_with_most_views:
                print(f"Post with the most views: {post_with_most_views}")
            else:
                print("No posts available.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

def find_posts_in_range(post_dict):
    start_str = input("Enter the start year and month (format YYYY-MM): ")
    end_str = input("Enter the end year and month (format YYYY-MM): ")
    try:
        start_datetime = datetime.datetime.strptime(start_str + "-01",
                                                    "%Y-%m-%d")  # Default to the first day of the start month
        end_datetime = datetime.datetime.strptime(end_str + "-01",
                                                  "%Y-%m-%d")  # Default to the first day of the end month
        results = []
        for key, post in post_dict.items():
            if start_datetime <= key <= end_datetime:
                results.append(post)
        if results:
            for post in results:
                print(post)
        else:
            print("No posts found in that range.")
    except ValueError:
        print("Invalid datetime format. Please enter the datetime in the correct format (YYYY-MM).")

def main():
    num_posts = int(input("Enter the number of posts to generate: "))
    posts = generate_random_posts(num_posts)
    post_dict, max_heap = create_data_structures(posts)
    run_menu(post_dict, max_heap, posts)

main()
