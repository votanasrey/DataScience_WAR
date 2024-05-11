from urllib.request import Request, urlretrieve
import pandas as pd 
import sqlite3

def get_table_name_sqlite_file(db_file_part):
    conn = sqlite3.connect(db_file_part)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    conn.close()
def get_table_columns_name_sqlite_file(db_file_part, table_name):
    conn = sqlite3.connect(db_file_part)
    cursor = conn.cursor() 
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    for column in columns:
        print(column[1])
    conn.close()

def load_sqlite_file(db_file_path, query):
    try:
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close() 
        return rows
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
    except FileNotFoundError:
        print(f"File '{db_file_path}' not found.")
        return None

db_file_path = './data/IMDB_Movies_2021.db' 
table_name = 'REVIEWS'
query_1 = ''' 

SELECT AUTHOR, AVG(RATING) AS AVG_RATING
FROM REVIEWS
GROUP BY 1
ORDER BY AVG_RATING DESC
LIMIT 3; 

'''
query_2 = ''' SELECT TITLE FROM REVIEWS WHERE TITLE LIKE "%Story%" '''
query_3 = ''' 

SELECT r1.TITLE AS movie_title_1, r2.TITLE AS movie_title_2, r1.AUTHOR AS reviewer
FROM REVIEWS r1
INNER JOIN REVIEWS r2 ON r1.AUTHOR = r2.AUTHOR
AND r1.TITLE <> r2.TITLE 

'''


print("**"*50)
print("List all the tables within DATABASE")
get_table_name_sqlite_file(db_file_path)
print("**"*50)
print("\n\n\n")

print("**"*50)
print("List all the COLUMNS within DATABASE")
get_table_columns_name_sqlite_file(db_file_path, table_name)
print("**"*50)
print("\n\n\n")

print("**"*50)
print("TOP 3 HIGHEST RATE MOVIES")
print("**"*50)

data_1 = load_sqlite_file(db_file_path, query_1)
if data_1 is not None:
    for row in data_1:
        print(row)
print("\n\n\n")

print("**"*50)
print("MOVIES TITLE EXISTS - STORY WORD WITHIN")
print("**"*50)

data_2 = load_sqlite_file(db_file_path, query_2)
if data_2 is not None:
    for row in data_2:
        print(row)
print("\n\n\n")


print("**"*50)
print("MOVIES THAT HAVE THE SAME REVIEWERS")
print("**"*50)

data_3 = load_sqlite_file(db_file_path, query_3)
if data_3 is not None:
    for row in data_3:
        print(row)
print("\n\n\n")
