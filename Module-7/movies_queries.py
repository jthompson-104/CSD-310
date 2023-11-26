import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "SnuggleSQL#10",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

# finally:
    # db.close()

cursor = db.cursor()

# ------------------------- STUDIO QUERY
def studio_query():
    cursor.execute("SELECT studio_id, studio_name FROM studio")

    studios = cursor.fetchall()

    print("\n-- DISPLAYING Studio RECORDS --")

    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# -------------------------- GENRE QUERY
def genre_query():
    cursor.execute("SELECT genre_id, genre_name FROM genre")

    genres = cursor.fetchall()

    print("-- DISPLAYING Genre RECORDS --")

    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# -------------------------- SHORT FILM QUERY
def short_film_query():
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

    short_films = cursor.fetchall()

    print("-- DISPLAYING Short Film RECORDS --")

    for short_film in short_films:
        print("Film Name: {}\nRuntime: {}\n".format(short_film[0],short_film[1]))

# -------------------------- DIRECTOR QUERY (Ordered)
def director_query_ordered():
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

    directors = cursor.fetchall()

    print("-- DISPLAYING Director RECORDS in Order --")

    for director in directors:
        print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))

studio_query()
genre_query()
short_film_query()
director_query_ordered()

db.close()