import sqlite3
import json
from models import Post
from models import User


def get_all_posts():
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.user_id,
            a.title,
            a.publication_date,
            a.image_url,
            a.content,
            a.approved
        FROM posts a
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:


            post = Post(row['id'], row['user_id'], row["title"], row["publication_date"], row["image_url"],
                        row['content'], row['approved'])

            posts.append(post.__dict__)

    return posts

def get_single_post(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.user_id,
            a.title,
            a.publication_date,
            a.image_url,
            a.content,
            a.approved,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Posts a
        JOIN Users u
            ON u.id = a.user_id
        WHERE a.id = ?
        """, ( id, ))

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(row['id'], row['user_id'], row['title'],
                                row['publication_date'], row['image_url'],
                                row['content'], row['approved'])

            user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                                row['bio'], row['username'], row['password'], row['profile_image_url'],row['created_on'], row['active'])


            post.user = user.__dict__


            posts.append(post.__dict__)

    return posts




def create_post(new_post):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, title, publication_date, image_url, content, approved )
        VALUES
            ( ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['title'],
            new_post['publication_date'], new_post['image_url'],
            new_post['content'], new_post['approved'] ))

        id = db_cursor.lastrowid

        new_post['id'] = id


    return new_post




def delete_post(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))

def get_all_posts_by_title(title):
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.user_id,
            a.title,
            a.publication_date,
            a.image_url,
            a.content,
            a.approved
        FROM Posts a
        WHERE a.title = ?
        """, (title, ))

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(row['id'], row['user_id'], row['title'],
                            row['publication_date'], row['image_url'],
                            row['content'], row['approved'])

            posts.append(post.__dict__)

    return posts

def get_all_posts_by_user(user_id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.user_id,
            a.title,
            a.publication_date,
            a.image_url,
            a.content,
            a.approved
        FROM Posts a
        WHERE a.user_id = ?
        """, (user_id, ))

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['title'],
                            row['publication_date'], row['image_url'],
                            row['content'], row['approved'])
        
            posts.append(post.__dict__)


    return posts


def update_post(id, new_post):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
                user_id = ?,
                title = ?,
                publication_date = ?,
                image_url = ?,
                content = ?,
                approved = ?
        WHERE id = ?
        """, (new_post['user_id'], new_post['title'],
            new_post['publication_date'], new_post['image_url'],
            new_post['content'], new_post['approved'], id,  ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True