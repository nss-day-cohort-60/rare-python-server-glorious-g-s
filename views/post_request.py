import sqlite3
import json
from models import Post


def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
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

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
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

        # Load the single result into memory
        data = db_cursor.fetchone()

        if data is None:
            return {}

        # Create an post instance from the current row
        post= Post(data['id'], data['user_id'], data['title'],
                            data['publication_id'], data['image_url'],
                            data['content'], data['approved'])

        return post.__dict__