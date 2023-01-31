import sqlite3
import json
from models import User


USERS = [
    {
        "id": 1,
        "first_name": "Pat",
        "last_name": "Mahomes",
        "email": "pat@pat.com",
        "bio": "Football player",
        "username": "pat",
        "password" : "pat",
        "profile_image_url": "https://www.history.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTU3ODc4NjAwMDI2ODkxNTkz/the-nfl-begins-football-grass-2014-hero-2.jpg", 
        "created_on": 1312023,
        "active": 1,

    },
        {
        "id": 2,
        "first_name": "Jalen",
        "last_name": "Hurts",
        "email": "hurts@hurts.com",
        "bio": "Football player",
        "username": "jalen",
        "password" : "hurt",
        "profile_image_url": "https://assets3.cbsnewsstatic.com/hub/i/r/2022/03/14/08c8764e-029d-4bf2-8319-db05c67a20d3/thumbnail/640x392/be38c4b9e67216d7a78628552724738c/tom-brady-football.jpg", 
        "created_on": 1312023,
        "active": 1,

    }
]


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
            u.active,
        FROM Users u
        WHERE u.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        user = User(data['id'], data['first_name'], data['last_name'], data['email'],
                                data['bio'], data['username'], data['password'], data['profile_image_url'],data['created_on'], data['active'])
        

        return user.__dict__


