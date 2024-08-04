import csv
from datetime import datetime
from colorama import Fore, init

from data import email_details as ed


init(autoreset=True)

error = Fore.RED
enter = Fore.CYAN
re_enter = Fore.MAGENTA
success = Fore.LIGHTGREEN_EX
prints = Fore.YELLOW
command = Fore.LIGHTCYAN_EX


class User:
    def __init__(self, id_of: int, full_name: str, username: str, email: str, password: str, status: str, created_at=None):
        """Initialize user with given details and validate password, email, phone."""
        if not self.validate_password(password):
            raise ValueError("Password must be at least 8 characters long, contain at least one uppercase letter, "
                             "one lowercase letter, one digit, and one special character.")

        if not self.validate_email(email):
            raise ValueError("Invalid email address.")

        self.id_of = id_of
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        if created_at:
            self.created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.created_at = datetime.now()

    @staticmethod
    def validate_password(password: str) -> bool:
        """Validate password"""
        if len(password) < 8:
            return False
        return True

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email address"""
        if not email.endswith(ed):
            return False
        return True

    def get_my_posts(self):
        """Get all posts of current user"""
        try:
            with open(file='posts.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    if int(line[2]) == self.id_of:
                        print(prints+f"ID: {line[0]}\n"
                              f"    Text: {line[1]}\n"
                              f"    Created At: {line[3]}\n"
                              f"----------------------------------------------------------------")
        except FileNotFoundError:
            print(error+f"{self.username} - Bu User Xech Qanday Post Joylamagan!")

    def get_my_comments(self):
        """Get all comments of current user"""
        try:
            with open(file='posts.csv', mode='r', encoding='utf-8') as j:
                file = csv.reader(j)
                for x in range(1, len(list(file))+1):
                    try:
                        with open(file=f'Comment/{x}-comments.csv', mode='r', encoding='utf8') as f:
                            lines = csv.reader(f, delimiter='|')
                            for line in lines:
                                if int(line[2]) == self.id_of:
                                    with open(file='posts.csv', mode='r', encoding='utf8') as e:
                                        post_lines = csv.reader(e, delimiter='|')
                                        for post_line in post_lines:
                                            if post_line[0] == line[3]:
                                                post_info = post_line
                                    print(prints+f"ID: {line[0]}\n"
                                          f"    Yozilgan Sharh: {line[1]}\n"
                                          f"    Sharh Yozilgan Post: {post_info[1]}\n"
                                          f"    Created At: {line[4]}\n"
                                          f"----------------------------------------------------------------")
                    except FileNotFoundError:
                        continue
        except FileNotFoundError:
            print(error+f"{self.username} - Bu User Xech Qanday Comment Joylamagan!")

    def get_my_likes(self):
        """Get all likes of current user"""
        try:
            with open(file='posts.csv', mode='r', encoding='utf-8') as k:
                file_of = csv.reader(k)
                for h in range(1, len(list(file_of))+1):
                    try:
                        with open(file=f'Like/{h}_likes.csv', mode='r', encoding='utf8') as f:
                            lines = csv.reader(f, delimiter='|')
                            for line in lines:
                                if int(line[2]) == self.id_of:
                                    with open(file='posts.csv', mode='r', encoding='utf8') as r:
                                        post_lines = csv.reader(r, delimiter='|')
                                        for post_line in post_lines:
                                            if post_line[0] == line[2]:
                                                post_info = post_line
                                    print(prints+f"ID: {line[0]}\n"
                                          f"    Liked Post: {post_info[1]}\n"
                                          f"    Created: {line[3]}")
                    except FileNotFoundError:
                        continue
        except FileNotFoundError:
            print(error+f"{self.username} - Bu User Xech Qanday Postlarga Like Bosmagan!")

    def __str__(self):
        """String info of user"""
        return (prints+f"ID: {self.id_of}\nFull Name: {self.full_name}\n"
                f"Username: {self.username}\nEmail: {self.email}\n"
                f"Password: {self.password}\nCreated At: {self.created_at}")


class Post:
    def __init__(self, id_post: int, message: str, author: User):
        """Initialize post with given message and author."""
        self.id_post = id_post
        self.message = message
        self.author = author
        self.created_at = datetime.now()

    def __str__(self):
        """String info of post"""
        return (prints+f"Message: {self.message}\nAuthor: {self.author.full_name}\n"
                f"Created At: {self.created_at}")


class Comment:
    def __init__(self, id_comment: int, message: str, author: User, post: Post):
        """Initialize comment with given message, author and post."""
        self.id_comment = id_comment
        self.message = message
        self.author = author
        self.post = post
        self.created_at = datetime.now()

    def __str__(self):
        """String info of comment"""
        return (prints+f"Message: {self.message}\nAuthor: {self.author.full_name}\n"
                f"Post: {self.post.message}\nCreated At: {self.created_at}")


class Like:
    def __init__(self, id_like: int, author: User, post: Post):
        """Initialize like with given author and post."""
        self.id_like = id_like
        self.author = author
        self.post = post
        self.created_at = datetime.now()

    def __str__(self):
        """String info of like"""
        return (prints+f"Author: {self.author.full_name}\nPost: {self.post.message}\n"
                f"Created At: {self.created_at}")


class Twitter:
    def create_user(self, full_name: str, username: str, email: str, password: str, status=None) -> User:
        """Create a new user"""
        try:
            with open(file='users.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    if line[2] == username:
                        print(error+"Username already exists.")
                        exit()
                    id_of = int(line[0])
        except FileNotFoundError:
            id_of = 0
        if status is None:
            status = "User"
        user = User(id_of+1, full_name, username, email, password, status)
        with open(file='users.csv', mode='a', encoding='utf8') as f:
            f.write(f"{user.id_of}|{user.full_name}|{user.username}|{user.email}|"
                    f"{user.password}|{user.created_at}|{user.status}\n")
            print(success+f"{user.full_name} - Created Successfully!")
        return user

    def login(self, username: str, password: str):
        """Login with username and password"""
        try:
            with open(file='users.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    if line[2] == username and line[4] == password:
                        if line[6] == "Admin":
                            print(success+f"{line[1]} - Salom Admin!")
                        else:
                            print(success+f"{line[1]} - Salom Siz Muvaffaqiyatli Login Qildingiz!")
                        return User(int(line[0]), line[1], line[2], line[3], line[4], line[6])
            print("Invalid username or password.")
            exit()
        except FileNotFoundError:
            return "No User found"

    def create_post(self, author: User, message: str):
        """Create a new post"""
        try:
            with open(file='posts.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    if line[1] == message:
                        raise ValueError("Post already exists.")
                    id_post = int(line[0])
        except FileNotFoundError:
            id_post = 0
        post = Post(id_post+1, message, author)
        with open(file='posts.csv', mode='a', encoding='utf8') as f:
            f.write(f"{post.id_post}|{post.message}|{post.author.id_of}|{post.created_at}\n")
            print(success+f"Post - {post.message[:11]} - Created Successfully!")
        return post

    def post_finder(self, id_post):
        """Find post by id"""
        try:
            with open(file='posts.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    if line[0] == str(id_post):
                        post_info = line
                        with open(file='users.csv', mode='r', encoding='utf8') as r:
                            user_lines = csv.reader(r, delimiter='|')
                            for user_line in user_lines:
                                if user_line[0] == post_info[2]:
                                    post_author = User(id_of=int(user_line[0]), full_name=user_line[1],
                                                       username=user_line[2], email=user_line[3],
                                                       password=user_line[4], status=user_line[6],
                                                       created_at=user_line[5])
                        return Post(int(post_info[0]), post_info[1], post_author)
        except FileNotFoundError:
            return "No Post found"

    def like_post(self, author: User, post: int):
        """Like a post"""
        post = self.post_finder(post)
        try:
            with open(file=f'Like/{post.id_post}_likes.csv', mode='r', encoding='utf8') as t:
                lines = csv.reader(t, delimiter='|')
                for line in lines:
                    if int(line[1]) == author.id_of:
                        print(error+"You already liked this post.")
                        return None
                    id_like = int(line[0])
        except FileNotFoundError:
            id_like = 0
        like = Like(id_like+1, author, post)
        with open(file=f'Like/{post.id_post}_likes.csv', mode='a', encoding='utf8') as f:
            f.write(f"{like.id_like}|{like.author.id_of}|{like.post.id_post}|{like.created_at}\n")
        print(success+f"{author.full_name} liked {post.message[:10]}")

    def comment_post(self, author: User, post: int, message: str):
        """Comment to post"""
        try:
            with open(file=f'Comment/{post}-comments.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    id_comment = int(line[0])
        except FileNotFoundError:
            id_comment = 0
        post = self.post_finder(post)
        comment = Comment(id_comment+1, message, author, post)
        with open(file=f'Comment/{post.id_post}-comments.csv', mode='a', encoding='utf8') as f:
            f.write(f"{comment.id_comment}|{comment.message}|{comment.author.id_of}|"
                    f"{comment.post.id_post}|{comment.created_at}\n")
            print(success+f"{author.full_name} commented on {post.message[:10]}")

    def get_all_users(self):
        """Get all users"""
        try:
            with open(file='users.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    print("Users:")
                    print(prints+f"ID: {line[0]}\n"
                          f"    Full Name: {line[1]}\n"
                          f"    Username: {line[2]}\n"
                          f"    Email: {line[3]}\n"
                          f"    Phone: {line[4]}\n"
                          f"    Created At: {line[5]}\n"
                          f"    Status: {line[6]}\n")
                    print("----------------------------------------")
        except FileNotFoundError:
            print(error+"No User found")

    def get_user_info(self, id_of: str):
        """Get user info by id"""
        try:
            with open(file='users.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    if line[0] == id_of:
                        print(prints+f"    ID: {line[0]}\n"
                              f"        Full Name: {line[1]}\n"
                              f"        Username: {line[2]}\n"
                              f"        Email: {line[3]}\n"
                              f"        Password: {line[4]}\n"
                              f"        Created At: {line[5]}\n"
                              f"        Status: {line[6]}")
        except FileNotFoundError:
            print(error+"No User found")

    def get_post_info(self, id_post: str):
        """Get post info by id"""
        try:
            with open(file='posts.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for line in lines:
                    if line[0] == id_post:
                        print(prints+f"    ID: {line[0]}\n"
                              f"        Message: {line[1]}\n"
                              f"        Author ID: ")
                        self.get_user_info(line[2])
                        print(prints+f"        Created At: {line[3]}\n")
        except FileNotFoundError:
            print(error+"No Post found")

    def get_all_likes(self):
        """Get all likes"""
        try:
            with open(file='posts.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for post_id in range(1, len(list(lines))+1):
                    try:
                        with open(file=f'Like/{post_id}_likes.csv', mode='r', encoding='utf8') as f:
                            lines = csv.reader(f, delimiter='|')
                            for line in lines:
                                print(f"Likes for Post ID: {post_id}")
                                print(prints+f"ID: {line[0]}\n"
                                      f"    Author: ")
                                self.get_user_info(line[1])
                                print(prints+f"    Post: ")
                                self.get_post_info(line[2])
                                print(prints+f"    Created At: {line[3]}\n"
                                      "----------------------------------------")
                    except FileNotFoundError:
                        continue
        except FileNotFoundError:
            print(error+"No Like found!")

    def get_all_comments(self):
        """Get all comments"""
        try:
            with open(file='posts.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                for post_id in range(1, len(list(lines))+1):
                    try:
                        with open(file=f'Comment/{post_id}-comments.csv', mode='r', encoding='utf8') as f:
                            lines = csv.reader(f, delimiter='|')
                            for line in lines:
                                print(f"Comments for Post ID: {post_id}")
                                print(prints+f"    ID: {line[0]}\n"
                                      f"        Message: {line[1]}\n"
                                      f"        Author: {self.get_user_info(line[2])}\n"
                                      f"        Post: {self.get_post_info(str(post_id))}\n"
                                      f"        Created At: {line[4]}\n")
                                print("----------------------------------------")
                    except FileNotFoundError:
                        pass
        except FileNotFoundError:
            print(error+"No Comments found!")

    def search_posts(self, text: str):
        """Search posts by text"""
        try:
            text = text.strip(", ")
            print("----------------------------------------")
            print(f"Search Results for '{text}':")
            print("----------------------------------------")
            with open(file='posts.csv', mode='r', encoding='utf8') as f:
                lines = csv.reader(f, delimiter='|')
                st = []
                for line in lines:
                    for x in text:
                        if x.lower() in line[1].lower():
                            if line not in st:
                                st.append(line)
                                print(prints+f"ID: {line[0]}\n"
                                      f"    Text: {line[1]}\n"
                                      f"    Author: ")
                                self.get_user_info(line[2])
                                print(prints+f"    Created At: {line[3]}\n"
                                      "----------------------------------------")
        except FileNotFoundError:
            print(error+"No Post found!")


class Paginator:
    def __init__(self, page_size=5):
        with open(file='posts.csv', mode='r', encoding='utf-8') as f:
            lines = csv.reader(f, delimiter='|')
            self.items = [line for line in lines]
        self.page_size = page_size
        self.current = 1
        self.pages = (len(self.items) - 1 + page_size) // page_size

    def get_page(self):
        start = (self.current - 1) * self.page_size
        end = (self.current - 1) * self.page_size + self.page_size
        item = self.items[start:end]
        for x in item:
            print(prints+f"ID: {x[0]}\n"
                  f"    Text: {x[1]}")
            print(prints+"    Author: ")
            my_twitter.get_user_info(id_of=x[2])
            print(prints+f"    Created At: {x[3]}\n"
                  "----------------------------------------")
        print(re_enter+f"\nPage {self.current}/{self.pages}")

    def next_page(self):
        if self.current < self.pages:
            self.current += 1
        self.get_page()

    def previous_page(self):
        if self.current > 1:
            self.current -= 1
        self.get_page()


# For Usage
def get_all_posts():
    choose = input(enter+"1 ta Page da Nechta Malumot Chiqsin: ")
    while not choose.isdigit():
        print(error+"Bu yerda xatolik. Iltimos, raqam kiriting!")
        choose = input(re_enter+"1 ta Page da Nechta Malumot Chiqsin: ")
    paginator = Paginator(int(choose))
    paginator.get_page()
    while True:
        print(command+f"\n1. Previous | Hozirgi Sahifa {paginator.current} | 2. Next\n"
              f"3. Stop")
        action = input(enter+"Enter your choice: ")
        if action == '1':
            paginator.previous_page()
        elif action == '2':
            paginator.next_page()
        elif action == '3':
            break
        else:
            print(error+"Boshidan Kiriting!")


def get_all_posts_for_like():
    choose = input(enter+"1 ta Page da Nechta Malumot Chiqsin: ")
    while not choose.isdigit():
        print(error+"Bu yerda xatolik. Iltimos, raqam kiriting!")
        choose = input(re_enter+"1 ta Page da Nechta Malumot Chiqsin: ")
    paginator = Paginator(int(choose))
    paginator.get_page()
    while True:
        print(command+f"\n1. Previous | Hozirgi Sahifa {paginator.current} | 2. Next\n"
              f"3. Stop\n"
              f"Birortasiga Layk Bosmoqchi Bo'lsangiz choice= va ID sini kiriting!")
        action = input(enter+"Enter your choice: ")
        if action == '1':
            paginator.previous_page()
        elif action == '2':
            paginator.next_page()
        elif action == '3':
            break
        elif str(action).startswith("choice="):
            post_id = int(str(action).split("=")[1])
            my_twitter.like_post(user, post_id)
        else:
            print(error+"Boshidan Kiriting!")


def get_all_posts_for_comment():
    choose = input(enter+"1 ta Page da Nechta Malumot Chiqsin: ")
    while not choose.isdigit():
        print(error+"Bu yerda xatolik. Iltimos, raqam kiriting!")
        choose = input(enter+"1 ta Page da Nechta Malumot Chiqsin: ")
    paginator = Paginator(int(choose))
    paginator.get_page()
    while True:
        print(command+f"\n1. Previous | Hozirgi Sahifa {paginator.current} | 2. Next\n"
              f"3. Stop\n"
              f"Birortasiga Commentariya Yozmoqchi Bo'lsangiz choice= va ID sini kiriting!")
        action = input(enter+"Enter your choice: ")
        if action == '1':
            paginator.previous_page()
        elif action == '2':
            paginator.next_page()
        elif action == '3':
            break
        elif str(action).startswith("choice="):
            post_id = int(str(action).split("=")[1])
            comm = input(enter+"Enter comment: ")
            my_twitter.comment_post(user, post_id, comm)
        else:
            print(error+"Boshidan Kiriting!")


def after_login_admin():
    print(command+"\nChoose an action:\n"
          "1. Create a new post\n"
          "2. Create a new comment for post\n"
          "3. Create a new like for post\n"
          "4. Get Your Posts\n"
          "5. Get Your Comments\n"
          "6. Get Your Likes\n"
          "7. Get All Posts\n"
          "8. Get My Info\n"
          "9. Search with keywords(, bilan yozing)\n"
          "For Admin:\n"
          "    10. Get All Users\n"
          "    11. Get All Comments\n"
          "    12. Get All Likes\n"
          "13. Logout")
    action = input(enter+"Enter your choice: ")
    if action == '1':
        message = input(enter+"Enter post message: ")
        my_twitter.create_post(user, message)
    elif action == '2':
        get_all_posts_for_comment()
    elif action == '3':
        get_all_posts_for_like()
    elif action == '4':
        user.get_my_posts()
    elif action == '5':
        user.get_my_comments()
    elif action == '6':
        user.get_my_likes()
    elif action == '7':
        get_all_posts()
    elif action == '8':
        print(user)
    elif action == '9':
        text = input(enter+"Enter: ")
        my_twitter.search_posts(text)
    elif action == '10':
        my_twitter.get_all_users()
    elif action == '11':
        my_twitter.get_all_comments()
    elif action == '12':
        my_twitter.get_all_likes()
    elif action == '13':
        return 'salom'


def after_login_user():
    print(command+"\nChoose an action:\n"
          "1. Create a new post\n"
          "2. Create a new comment for post\n"
          "3. Create a new like for post\n"
          "4. Get Your Posts\n"
          "5. Get Your Comments\n"
          "6. Get Your Likes\n"
          "7. Get All Posts\n"
          "8. Get My Info\n"
          "9. Search with keywords(, bilan yozing)\n"
          "10. Logout")
    action = input(enter+"Enter your choice: ")
    if action == '1':
        message = input(enter+"Enter post message: ")
        my_twitter.create_post(user, message)
    elif action == '2':
        get_all_posts_for_comment()
    elif action == '3':
        get_all_posts_for_like()
    elif action == '4':
        user.get_my_posts()
    elif action == '5':
        user.get_my_comments()
    elif action == '6':
        user.get_my_likes()
    elif action == '7':
        get_all_posts()
    elif action == '8':
        print(user)
    elif action == '9':
        text = input(enter+"Enter: ")
        my_twitter.search_posts(text)
    elif action == '10':
        return 'salom'


def after_login():
    if user:
        if user.status == "Admin":
            return after_login_admin()
        after_login_user()


# Usage
my_twitter = Twitter()

while True:
    print(command+"\nChoose an action:\n"
          "1. Register\n"
          "2. Login\n"
          "3. Exit")
    choice = input(enter+"Enter your choice: ")

    if choice == '1':
        username = input(enter+"Enter username: ")
        password = input(enter+"Enter password: ")
        email = input(enter+"Enter email: ")
        full_name = input(enter+"Enter full name: ")
        status = input(enter+"Enter status (Muhim Emas): ")

        user = my_twitter.create_user(username=username, password=password, email=email,
                                      full_name=full_name, status=status)
        while True:
            a = after_login()
            if a:
                break
    elif choice == '2':
        username = input(enter+"Enter username: ")
        password = input(enter+"Enter password: ")

        user = my_twitter.login(username, password)
        if user != 'No User found':
            while True:
                a = after_login()
                if a:
                    break
        break
    elif choice == '3':
        break
    else:
        print(error+"Invalid choice!")
