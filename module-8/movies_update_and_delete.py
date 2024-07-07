import mysql.connector
from mysql.connector import errorcode

# All changes are currently temporary to make the changes permanent you would uncomment the db.commit() function at the end of the code.

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.

    # Inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # Get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Setting up connection to the movies database using the movies_user.
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

# Showing a pre edited version of the films table.
    show_films(cursor, "DISPLAYING FILMS")

# Inserting Us into the film table
    cursor.execute("""
        INSERT INTO film (film_director, film_name, film_releaseDate, film_runtime, genre_id, studio_id)
        VALUES 
            ('Jordan Peele', 'Us', '2019', 116, (SELECT genre_id FROM genre WHERE genre_name = 'Horror'), (SELECT studio_id FROM studio WHERE studio_name = 'Blumhouse Productions'))
        """)

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Updating aliens genre to Horror!
    cursor.execute("""
        UPDATE film
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name  = 'Alien'
    """)

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

# Deleting Gladiator from the database.
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    """)
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Error catching when connecting to the database.
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
# Commit changes and then close the connection with the database.
#    db.commit()
    db.close()