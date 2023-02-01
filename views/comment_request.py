import sqlite3
import json
from models import Comment

def get_all_comments_by_post(post_id):
    # Open a connection to the database
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM comments c
        WHERE c.post_id = ?
        """, (post_id, ))

        # Initialize an empty list to hold all comment representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an comment instance from the current row
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])

            # Add the dictionary representation of the comment to the list
            comments.append(comment.__dict__)

    return comments

def create_comment(new_comment):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_comment['post_id'], new_comment['author_id'],
              new_comment['content'] ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the comment dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id


    return new_comment

def delete_comment(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM comments
        WHERE id = ?
        """, (id, ))