#script to put information from Json to database in MySQL

#By Jonathan Helmond
#22.10.2020


#This script extracts information from a JSON file which structure should be {"movietitle":{"Title":"movietitle","Year":2014,...}}
#This Json is generated by the movies_to_json script in this resporitory, https://github.com/JonathanKit/movie_database
#The database has many-to-many relations for genre, language and actors
#ratings are saved as int or floats

import json
import mysql.connector

path_movies_json = 'D:\Sofia_courses\Database\All_movies_json.txt'


#database info
#The databse used is a MySQL database, check google how to set it up
user = "root"
passwd = "root"
host = '127.0.0.1'
port = 3306
database = "movies"

def save_in_database(json_data):
    
    if(json_data['Response']):
        title = json_data['Title']
        # Goes through the json dataset and extracts information if it is available
        if json_data['Year']!='N/A':
            year = int(json_data['Year'])
        else:
            year = "Nan"
        if json_data['Rated']!='N/A':
            rated = json_data['Rated']
        else:
            rated = "Nan"
        if json_data['Released']!='N/A':
            released = json_data['Released']
        else:
            released = "Nan"
        if json_data['Runtime']!='N/A':
            runtime = int(json_data['Runtime'].split()[0])
        else:
            runtime = "Nan"
        if json_data['Genre']!='N/A':
            genre = (json_data['Genre'].split(", "))
        else:
            genre = "Nan"
        if json_data['Director']!='N/A':
            director = json_data['Director']
        else:
            director = "Nan"
        if json_data['Writer']!='N/A':
            writer = json_data['Writer']
        else:
            writer = "Nan"
        if json_data['Actors']!='N/A':
            actors = (json_data['Actors'].split(", "))
        else:
            actors = "Nan"
        if json_data['Plot']!='N/A':
            plot = json_data['Plot']
        else:
            plot = "Nan"
        if json_data['Language']!='N/A':
            language = (json_data['Language'].split(", "))
        else:
            language = "Nan"
        if json_data['Country']!='N/A':
            country = json_data['Country']
        else:
            country = "Nan"
        if json_data['Awards']!='N/A':
            awards = json_data['Awards']
        else:
            awards = "Nan"
        if json_data['Poster']!='N/A':
            poster = json_data['Poster']
        else:
            poster = "Nan"
        if json_data['Ratings']!='N/A':
            for one_rating in json_data['Ratings']:
                if (one_rating['Source']=="Internet Movie Database"):
                    rating_imd = float(one_rating['Value'].split("/")[0])
                else:
                    rating_imd = "Nan"
                if (one_rating['Source']=="Rotten Tomatoes"):
                    rating_rt = float(one_rating['Value'].split("%")[0])
                else:
                    rating_rt = "Nan"
                if (one_rating['Source']=="Metacritic"):
                    rating_metacritic = float(one_rating['Value'].split("/")[0])
                else:
                    rating_metacritic = "Nan"
        else:
            rating_imd = "Nan"
            rating_metacritic = "Nan"
            rating_rt = "Nan"
        if json_data['Metascore']!='N/A':
            metascore = float(json_data['Metascore'])
        else:
            metascore = "Nan"
        if json_data['imdbRating']!='N/A':
            imdb_rating = float(json_data['imdbRating'])
        else:
            imdb_rating = "Nan"
        if json_data['imdbVotes']!='N/A':
            imdbVotes = float(json_data['imdbVotes'].replace(",",""))
        else: 
            imbdVotes = "Nan"
        if json_data['imdbID']!='N/A':
            imdbID = json_data['imdbID']
        else:
            imbdID = "Nan"
        if json_data['Type']!='N/A':
            type1 = json_data['Type']
        else:
            type1 = "Nan"
        if json_data['Production']!='N/A':
            production = json_data['Production']
        else:
            production = "NaN"
        
        print(imdb_rating)

        # SQL commands
        #cur.execute('''CREATE TABLE IF NOT EXISTS MovieInfo 
        #(Title TEXT, Year INTEGER, Runtime INTEGER, Country TEXT, Metascore REAL, IMDBRating REAL)''')
        
        #cur.execute('SELECT Title FROM MovieInfo WHERE Title = ? ', (title,))
        #row = cur.fetchone()
        
        ##if row is None:
        #    cur.execute('''INSERT INTO MovieInfo (Title, Year, Runtime, Country, Metascore, IMDBRating)
         #           VALUES (?,?,?,?,?,?)''', (title,year,runtime,country,metascore,imdb_rating))
        #else:
        #    print("Record already found. No update made.")
        
        # Commits the change and close the connection to the database
        #conn.commit()
        #conn.close()

def setup_database():
    mydb = mysql.connector.connect(user=user, passwd=passwd,
        host=host, port=port, 
        database=database)

    cursor = mydb.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS movies (movieID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,title VARCHAR(100) UNIQUE, year INT, rated VARCHAR(30),released VARCHAR(50),runtime INT, genre VARCHAR(50), director VARCHAR(300), writer VARCHAR(300), plot VARCHAR(600), country VARCHAR(50), poster VARCHAR(200), rating_imd FLOAT, rating_rt INT, rating_metacritic INT, rating_metascore INT, rating_imdb FLOAT, imdbVotes INT, imdbID VARCHAR(20), production VARCHAR(100));')

    cursor.execute('CREATE TABLE IF NOT EXISTS genres (genreID INTEGER PRIMARY KEY AUTO_INCREMENT,genre_name VARCHAR(32) NOT NULL UNIQUE);')

    cursor.execute('CREATE TABLE IF NOT EXISTS actors (actorID INTEGER PRIMARY KEY AUTO_INCREMENT,forename VARCHAR(50), surname VARCHAR(50));')

    cursor.execute('CREATE TABLE IF NOT EXISTS languages (languageID INTEGER PRIMARY KEY AUTO_INCREMENT,language VARCHAR(50) UNIQUE);')

    cursor.execute('CREATE TABLE IF NOT EXISTS movies_genre( connectionID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,movieID INTEGER NOT NULL, genreID INTEGER NOT NULL, FOREIGN KEY (movieID) REFERENCES movies (movieID) ON DELETE RESTRICT ON UPDATE CASCADE,FOREIGN KEY (genreID) REFERENCES genres (genreID) ON DELETE RESTRICT ON UPDATE CASCADE);')

    cursor.execute('CREATE TABLE IF NOT EXISTS movies_language( connectionID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,movieID INTEGER NOT NULL, languageID INTEGER NOT NULL, FOREIGN KEY (movieID) REFERENCES movies (movieID) ON DELETE RESTRICT ON UPDATE CASCADE,FOREIGN KEY (languageID) REFERENCES languages (languageID) ON DELETE RESTRICT ON UPDATE CASCADE);')

    cursor.execute('CREATE TABLE IF NOT EXISTS movies_actor( connectionID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,movieID INTEGER NOT NULL, actorID INTEGER NOT NULL, FOREIGN KEY (movieID) REFERENCES movies (movieID) ON DELETE RESTRICT ON UPDATE CASCADE,FOREIGN KEY (actorID) REFERENCES actors (actorID) ON DELETE RESTRICT ON UPDATE CASCADE);')

    
    mydb.close()

def fill_movies(json_data):
    mydb = mysql.connector.connect(user=user, passwd=passwd,
        host=host, port=port, 
        database=database)

    cursor = mydb.cursor()

    if(json_data['Response']):
        title = json_data['Title']
        # Goes through the json dataset and extracts information if it is available
        if json_data['Year']!='N/A':
            try:
                year = int(json_data['Year'])
            except:
                try:
                    year = int(json_data['Year'].split("-")[0])
                except:
                    year = -1
        else:
            year = -1
        if json_data['Rated']!='N/A':
            rated = json_data['Rated']
        else:
            rated = "Nan"
        if json_data['Released']!='N/A':
            released = json_data['Released']
        else:
            released = "Nan"
        if json_data['Runtime']!='N/A':
            runtime = int(json_data['Runtime'].split()[0])
        else:
            runtime = -1
        if json_data['Genre']!='N/A':
            genre = (json_data['Genre'].split(", "))
        else:
            genre = "Nan"
        if json_data['Director']!='N/A':
            director = json_data['Director']
            director = director.replace("\"","")
        else:
            director = "Nan"
        if json_data['Writer']!='N/A':
            writer = json_data['Writer']
            writer = writer.replace("\"","")
        else:
            writer = "Nan"
        if json_data['Actors']!='N/A':
            actors = json_data['Actors'].replace("\"","")
            actors = (actors.split(", "))
        else:
            actors = "Nan"
        if json_data['Plot']!='N/A':
            plot = json_data['Plot']
            plot = plot.replace("\"","")
        else:
            plot = "Nan"
        if json_data['Language']!='N/A':
            language = (json_data['Language'].split(", ")[0])
        else:
            language = "Nan"
        if json_data['Country']!='N/A':
            country = (json_data['Country'].split(", ")[0])
        else:
            country = "Nan"
        if json_data['Awards']!='N/A':
            awards = json_data['Awards']
        else:
            awards = "Nan"
        if json_data['Poster']!='N/A':
            poster = json_data['Poster']
        else:
            poster = "Nan"
        if json_data['Ratings']:
            for one_rating in json_data['Ratings']:
                if (one_rating['Source']=="Internet Movie Database"):
                    rating_imd = float(one_rating['Value'].split("/")[0])
                else:
                    rating_imd = -1
                if (one_rating['Source']=="Rotten Tomatoes"):
                    rating_rt = float(one_rating['Value'].split("%")[0])
                else:
                    rating_rt = -1
                if (one_rating['Source']=="Metacritic"):
                    rating_metacritic = float(one_rating['Value'].split("/")[0])
                else:
                    rating_metacritic = -1
        else:
            rating_imd = -1
            rating_metacritic = -1
            rating_rt = -1
        if json_data['Metascore']!='N/A':
            rating_metascore = float(json_data['Metascore'])
        else:
            rating_metascore = -1
        if json_data['imdbRating']!='N/A':
            rating_imdb = float(json_data['imdbRating'])
        else:
            rating_imdb = -1
        if json_data['imdbVotes']!='N/A':
            imdbVotes = float(json_data['imdbVotes'].replace(",",""))
        else: 
            imdbVotes = -1
        if json_data['imdbID']!='N/A':
            imdbID = json_data['imdbID']
        else:
            imdbID = "Nan"
        if json_data['Type']!='N/A':
            type1 = json_data['Type']
        else:
            type1 = "Nan"
        try:
            production = json_data['Production']
        except:
            production = "NaN"

    #add movie to movies table
    cursor.execute(f'INSERT IGNORE INTO movies (title, year, rated, released, runtime, genre, director, writer, plot, country,awards, poster,rating_imd, rating_rt, rating_metacritic, rating_metascore, rating_imdb, imdbVotes, imdbID, type1, production) VALUES (\"{title}\", \"{year}\", \"{rated}\", \"{released}\", \"{runtime}\", \"{genre}\", \"{director}\", \"{writer}\", \"{plot}\", \"{country}\", \"{awards}\",\"{poster}\",\"{rating_imd}\", \"{rating_rt}\", \"{rating_metacritic}\",\"{rating_metascore}\",\"{rating_imdb}\",\"{imdbVotes}\",\"{imdbID}\",\"{type1}\", \"{production}\");' )   


    cursor.execute(f"SELECT EXISTS(SELECT * from movies WHERE Title=\"{title}\");")
    #cursor.execute(f"SELECT * from movies WHERE Title=\"{title}\";")
    existing_title = cursor.fetchone()[0]
    
    if not(existing_title):
        #create languages if not existing
        create_languages(cursor, language)
        #create genre if not existing
        create_genre(cursor, genre)
        #create actor if not existing
        create_actor(cursor, actors)

        mydb.commit()


        #add languages in language connectio table
        add_languages_to_movie(cursor, language, title)
        #add genre in genre connection table
        add_genre_to_movie(cursor, genre, title)
        #add actor in actor connection table
        add_actor_to_movie(cursor,actors,title)

        print("succesful parsed: ", title)
    
    mydb.commit()
    
    mydb.close()

#Connects language and movie by adding connection to the connection table
def add_languages_to_movie(cursor, language, title):
    #check if a valid language(string) is send if not it is a list of strings, because there are multible languages for this movie
    if(isinstance(language, str)):
        one_language = language
        #get the ID of the language from the language Table
        cursor.execute(f"SELECT languageID FROM languages WHERE language =\"{one_language}\";")
        languageID = cursor.fetchone()[0]
        #get the ID of the movie that will be connected to his languages
        cursor.execute(f"SELECT movieID FROM movies WHERE title =\"{title}\";")
        movieID = cursor.fetchone()[0]
        #create the connection of movieID and langaugeID if not set yet
        cursor.execute(f"INSERT IGNORE INTO movies_language (movieID,languageID) VALUES(\"{movieID}\",\"{languageID}\");")

        #print(languageID[0])
    else:
        #here is the same as above for one language, but for mulitble languages if the movie has more than one
        for one_language in language:
            cursor.execute(f"SELECT languageID FROM languages WHERE language =\"{one_language}\";")
            languageID = cursor.fetchone()[0]
            cursor.execute(f"SELECT movieID FROM movies WHERE title =\"{title}\";")
            movieID = cursor.fetchone()[0]
            cursor.execute(f"INSERT IGNORE INTO movies_language (movieID,languageID) VALUES(\"{movieID}\",\"{languageID}\");")

            #print(languageID[0])

#Connects language and movie by adding connection to the connection table
def add_genre_to_movie(cursor, genre, title):
    if(isinstance(genre, str)):
        one_genre = genre
        cursor.execute(f"SELECT genreID FROM genres WHERE genre_name =\"{one_genre}\";")
        genreID = cursor.fetchone()[0]
        cursor.execute(f"SELECT movieID FROM movies WHERE title =\"{title}\";")
        movieID = cursor.fetchone()[0]
        cursor.execute(f"INSERT IGNORE INTO movies_genre (movieID,genreID) VALUES(\"{movieID}\",\"{genreID}\");")

        #print(languageID[0])
    else:
        for one_genre in genre:
            cursor.execute(f"SELECT genreID FROM genres WHERE genre_name =\"{one_genre}\";")
            genreID = cursor.fetchone()[0]
            cursor.execute(f"SELECT movieID FROM movies WHERE title =\"{title}\";")
            movieID = cursor.fetchone()[0]
            cursor.execute(f"INSERT IGNORE INTO movies_genre (movieID,genreID) VALUES(\"{movieID}\",\"{genreID}\");")
    
#Connects language and movie by adding connection to the connection table
def add_actor_to_movie(cursor, actors, title):
    if(isinstance(actors, str)):
        this_actor_forename=actors.split(" ",1)[0]
        if(len(actors.split(" "))<2):
            this_actor_lastname = ""
        else:
            this_actor_lastname=actors.split(" ",1)[1]
        cursor.execute(f"SELECT actorID FROM actors WHERE forename=\"{this_actor_forename}\" AND surname=\"{this_actor_lastname}\";")
        actorID = cursor.fetchone()[0]
        cursor.execute(f"SELECT movieID FROM movies WHERE title =\"{title}\";")
        movieID = cursor.fetchone()[0]
        cursor.execute(f"INSERT IGNORE INTO movies_actor (movieID,actorID) VALUES(\"{movieID}\",\"{actorID}\");")

        #print(languageID[0])
    else:
        for one_actor in actors:

            this_actor_forename=one_actor.split(" ",1)[0]
            if(len(one_actor.split(" "))<2):
                this_actor_lastname = ""
            else:
                this_actor_lastname=one_actor.split(" ",1)[1]
            cursor.execute(f"SELECT actorID FROM actors WHERE forename=\"{this_actor_forename}\" AND surname=\"{this_actor_lastname}\";")
            actorID = cursor.fetchone()[0]
            cursor.execute(f"SELECT movieID FROM movies WHERE title =\"{title}\";")
            movieID = cursor.fetchone()[0]
            cursor.execute(f"INSERT IGNORE INTO movies_actor (movieID,actorID) VALUES(\"{movieID}\",\"{actorID}\");")
    

#this function checks if a language is existing in the language table and adds it if not
def create_languages(cursor, languages):
    #print(cursor.execute(f"SELECT * from languages ;"))
    if(isinstance(languages, str)):
        this_language=languages
        #check if the language is existing in the language table
        cursor.execute(f"SELECT EXISTS(SELECT * from languages WHERE language=\"{this_language}\");")
        existing_language = cursor.fetchone()[0]
        #if there is one new language add this language to the table
        if not(existing_language):
            cursor.execute(f"INSERT INTO languages (language) VALUES(\"{this_language}\");")
            print("language added: ", this_language)
    else:
        #if there are multiple languages check them independently and add the new languages to the table
        for this_language in languages:
            if not(cursor.execute(f"SELECT EXISTS(SELECT * from languages WHERE language=\"{this_language}\");")):
                cursor.execute(f"INSERT INTO languages (language) VALUES(\"{this_language}\");")
                print("language added: ", this_language)
    #another option if this is not working: INSERT INTO `table` (`value1`, `value2`) SELECT 'stuff for value1', 'stuff for value2' FROM DUAL WHERE NOT EXISTS (SELECT * FROM `table` WHERE `value1`='stuff for value1' AND `value2`='stuff for value2' LIMIT 1) 
    
#this function checks if a genre is existing in the genre table and adds it if not
def create_genre(cursor, genre):
    if(isinstance(genre, str)):
        this_genre=genre
        cursor.execute(f"SELECT EXISTS(SELECT * from genres WHERE genre_name=\"{this_genre}\");")
        existing_genre = cursor.fetchone()[0]
        if not(existing_genre):
            cursor.execute(f"INSERT INTO genres (genre_name) VALUES(\"{this_genre}\");")
            print("genre added: ", this_genre)
    else:
        for this_genre in genre:
            cursor.execute(f"SELECT EXISTS(SELECT * from genres WHERE genre_name=\"{this_genre}\");")
            existing_genre = cursor.fetchone()[0]
            if not(existing_genre):  
                cursor.execute(f"INSERT INTO genres (genre_name) VALUES(\"{this_genre}\");")
                print("genre added: ", this_genre)
    #another option if this is not working: INSERT INTO `table` (`value1`, `value2`) SELECT 'stuff for value1', 'stuff for value2' FROM DUAL WHERE NOT EXISTS (SELECT * FROM `table` WHERE `value1`='stuff for value1' AND `value2`='stuff for value2' LIMIT 1) 
    
#this function checks if a genre is existing in the genre table and adds it if not
def create_actor(cursor, actors):
    if(isinstance(actors, str)):
        this_actor_forename=actors.split(" ",1)[0]
        if(len(actors.split(" "))<2):
            this_actor_lastname = ""
        else:
            this_actor_lastname=actors.split(" ",1)[1]
        cursor.execute(f"SELECT EXISTS(SELECT * from actors WHERE forename=\"{this_actor_forename}\" AND surname=\"{this_actor_lastname}\");")
        existing_actor = cursor.fetchone()[0]
        if not(existing_actor):
            cursor.execute(f"INSERT INTO actors (forename,surname) VALUES(\"{this_actor_forename}\",\"{this_actor_lastname}\");")
            print("actor added: ", this_actor_forename, this_actor_lastname)
    else:
        for this_actor in actors:
            this_actor_forename=this_actor.split(" ",1)[0]
            if(len(this_actor.split(" "))<2):
                this_actor_lastname = ""
            else:
                this_actor_lastname=this_actor.split(" ",1)[1]
            cursor.execute(f"SELECT EXISTS(SELECT * from actors WHERE forename=\"{this_actor_forename}\" AND surname=\"{this_actor_lastname}\");")
            existing_actor = cursor.fetchone()[0]
            if not(existing_actor):
                cursor.execute(f"INSERT INTO actors (forename,surname) VALUES(\"{this_actor_forename}\",\"{this_actor_lastname}\");")
                print("actor added: ", this_actor_forename, this_actor_lastname)
    #another option if this is not working: INSERT INTO `table` (`value1`, `value2`) SELECT 'stuff for value1', 'stuff for value2' FROM DUAL WHERE NOT EXISTS (SELECT * FROM `table` WHERE `value1`='stuff for value1' AND `value2`='stuff for value2' LIMIT 1) 
    

def sql_connection():
    mydb = mysql.connector.connect(user='root', passwd='root',
        host='127.0.0.1', port=3306,
        database="movies")

    # database='movies'
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM test")

    for row in cursor.fetchall():
        print(len(row))

    mydb.close()


#This is for testing whether the script is working with an examplary Json file containing one movie
json_file_string = {"Title":"Miss Minoes","Year":"2001","Rated":"PG","Released":"06 Dec 2001","Runtime":"86 min","Genre":"Comedy, Family, Fantasy","Director":"Vincent Bal","Writer":"Annie M.G. Schmidt (novel), Tamara Bos (screenplay), Burny Bos (screenplay), Vincent Bal (screenplay)","Actors":"Theo Maassen, Carice van Houten, Sarah Bannier, Pierre Bokma","Plot":"A cat who turns into a young woman helps a journalist protect their town from a factory boss with an evil plan.","Language":"Dutch","Country":"Netherlands","Awards":"8 wins & 2 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BMTgzNDc1NjA0M15BMl5BanBnXkFtZTcwMDc0MDQxNw@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.8/10"},{"Source":"Rotten Tomatoes","Value":"64%"},{"Source":"Metacritic","Value":"50/100"}],"Metascore":"50","imdbRating":"6.8","imdbVotes":"4,611","imdbID":"tt0279231","Type":"movie","DVD":"N/A","BoxOffice":"N/A","Production":"20th Century Fox","Website":"N/A","Response":"True"}
json_file_string = json.dumps(json_file_string)
json_file_really = json.loads(json_file_string)
#print(json_file_really['Title'])
fill_movies(json_file_really)


#with open(path_movies_json) as json_file:
    #open json file
    #data = json.load(json_file)
    #get all the movie titles that are saved in the json file
    #list_of_titles = data.keys()
    
    
    
    #print(list_of_titles)
    #go through all titles and save their information in the database
    #for title in list_of_titles:
    #   print(title)
    #    fill_movies(data[title])