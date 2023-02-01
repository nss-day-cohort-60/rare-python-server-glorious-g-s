import sqlite3
import json
from models import User

def get_all_users():
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        """)

        users = []

        dataset = db_cursor.fetchall()

        for row in dataset:

                user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                                row['bio'], row['username'], row['password'], row['profile_image_url'],row['created_on'], row['active'])

                users.append(user.__dict__)

    return users



def get_single_user(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        WHERE u.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        user = User(data['id'], data['first_name'], data['last_name'], data['email'],
                                data['bio'], data['username'], data['password'], data['profile_image_url'], data['created_on'], data['active'])

        return user.__dict__


def get_user_by_username(username):

    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        from Users u
        WHERE u.username = ?
        """, (username,))

        data = db_cursor.fetchone()

        user = User(data['id'], data['first_name'], data['last_name'], data['email'],
                                data['bio'], data['username'], data['password'], data['profile_image_url'], data['created_on'], data['active'])

        return user.__dict__