import sqlite3
import json
from models import Post


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
            a.approved
        FROM posts a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        if data is None:
            return {}

        post= Post(data['id'], data['user_id'], data['title'],
                            data['publication_date'], data['image_url'],
                            data['content'], data['approved'])

        return post.__dict__


def create_post(new_post):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Post
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
        UPDATE Post
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