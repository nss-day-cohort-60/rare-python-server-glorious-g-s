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

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_post['id'] = id


    return new_post



def delete_post(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))