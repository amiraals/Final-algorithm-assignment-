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
