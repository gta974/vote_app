#!/usr/bin/env python
# coding: utf-8

import sqlite3
import os, errno

path =  "./" # path to created DB
DB_name = "votes.db" # DB name
conn = sqlite3.connect(path + DB_name) # connexion a la base de donnee
cursor = conn.cursor()

# creation de la table si elle n existe pass
cursor.execute("""
CREATE TABLE IF NOT EXISTS Main_table(
	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	vote TEXT,
	ip TEXT,
	Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
conn.close()

# conn = sqlite3.connect(path + DB_name) # connexion a la base de donnee
# cursor = conn.cursor()
# # creation de la table si elle n existe pass
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS news(
# 	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
# 	post_title TEXT,
# 	post TEXT
# )
# """)
# conn.commit()
# conn.close()
