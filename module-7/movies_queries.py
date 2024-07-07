import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'movies_user',
    'password': 'popcorn',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("\n-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    cursor.execute("SELECT film_name, film_runtime FROM film where film_runtime < 120")
    shortFilms = cursor.fetchall()
    print("\n-- DISPLAYING Short Film RECORDS --")
    for shortFilm in shortFilms:
        print("Film Name: {}\nRuntime: {}\n".format(shortFilm[0], shortFilm[1]))

    cursor.execute("SELECT film_name, film_director FROM film GROUP BY film_name, film_director ORDER BY film_director")
    directors = cursor.fetchall()
    print("\n-- DISPLAYING Director RECORDS in Order --")
    for director in directors:
        print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()