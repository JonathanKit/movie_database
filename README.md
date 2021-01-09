
# MOVIE DATABASE

**Author: Jonathan Helmond**

A movie database containing all movies from the first movie ever made in 1888 until 2019 which include 20567 movies. The Database is a MySQL Database with many-to-many relations.

[**GitHub repository**](https://github.com/JonathanKit/movie_database) **: https://github.com/JonathanKit/movie\_database**

## Movie Database Creation flow:
1.	FIND-MOVIE get a list of all movies produced <br />
All movies are saved in the all_movies_list, Updated until 2019
2.	SEND-TITLE Send the title of the movie into ombdapi <br />
The script movies_to_json.py uses all the movies list to extract the information of all the titles listed there
3.	EXTRACT-INFO Receive and extract the information from the JSON file  <br />
4.	SAVE-DATABASE Save the data in a Database with MySQL <br />
These two steps are implemented in the info_json_to_movies.py script

## Database structure:

![Structure](/database_structure.svg)


EXTRACT-INFO

The data is extracted with omdbapi([http://www.omdbapi.com/](http://www.omdbapi.com/)), the result of one request(searching for the movie Interstellar) looks like:

![](RackMultipart20210109-4-123chxa_html_d4d8cfbbd8c58a1.gif)

{&quot;Title&quot;:&quot;Interstellar&quot;,&quot;Year&quot;:&quot;2014&quot;,&quot;Rated&quot;:&quot;PG-13&quot;,&quot;Released&quot;:&quot;07 Nov 2014&quot;,&quot;Runtime&quot;:&quot;169 min&quot;,&quot;Genre&quot;:&quot;Adventure, Drama, Sci-Fi, Thriller&quot;,&quot;Director&quot;:&quot;Christopher Nolan&quot;,&quot;Writer&quot;:&quot;Jonathan Nolan, Christopher Nolan&quot;,&quot;Actors&quot;:&quot;Ellen Burstyn, Matthew McConaughey, Mackenzie Foy, John Lithgow&quot;,&quot;Plot&quot;:&quot;A team of explorers travel through a wormhole in space in an attempt to ensure humanity&#39;s survival.&quot;,&quot;Language&quot;:&quot;English&quot;,&quot;Country&quot;:&quot;USA, UK, Canada&quot;,&quot;Awards&quot;:&quot;Won 1 Oscar. Another 43 wins &amp; 148 nominations.&quot;,&quot;Poster&quot;:&quot;https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@.\_V1\_SX300.jpg&quot;,&quot;Ratings&quot;:[{&quot;Source&quot;:&quot;Internet Movie Database&quot;,&quot;Value&quot;:&quot;8.6/10&quot;},{&quot;Source&quot;:&quot;Rotten Tomatoes&quot;,&quot;Value&quot;:&quot;72%&quot;},{&quot;Source&quot;:&quot;Metacritic&quot;,&quot;Value&quot;:&quot;74/100&quot;}],&quot;Metascore&quot;:&quot;74&quot;,&quot;imdbRating&quot;:&quot;8.6&quot;,&quot;imdbVotes&quot;:&quot;1,462,266&quot;,&quot;imdbID&quot;:&quot;tt0816692&quot;,&quot;Type&quot;:&quot;movie&quot;,&quot;DVD&quot;:&quot;N/A&quot;,&quot;BoxOffice&quot;:&quot;N/A&quot;,&quot;Production&quot;:&quot;Syncopy, Lynda Obst Productions&quot;,&quot;Website&quot;:&quot;N/A&quot;,&quot;Response&quot;:&quot;True&quot;}

#### Tables:

The data is extracted with a Python script/function using the JSON library offered by Python

# Database structure

### ![](RackMultipart20210109-4-123chxa_html_8269a0c625f7b4b6.png)

| Columns | Datatype | Description |
| --- | --- | --- |
| MovieID | int | Unique, autoincrement |
| Title | Text | Unique! |
| Year | Int | |
| Rated | Text | |
| Released | Text | |
| Runtime | int | In minutes |
| Genre | Text | Just one main Genre |
| Director | Text | |
| Writer | Text | Can be multiple! |
| Plot | Text | |
| Country | Text | Can be multible |
| Poster | Text | |
| Rating\_imd | float | |
| Rating\_rt | int | |
| Rating\_metacritic | Int | |
| Rating\_metascore | Int | |
| Rating\_imdb | float | |
| Imdb\_votes | int | |
| Imdb\_ID | Text | |
| Production | Text | |

Genre Connection Table called **movies\_genre**

Connects a movie with its genres. If a movie has several genres it has multiple entries in this table

| Columns | Datatype | Description |
| --- | --- | --- |
| connectioID | int | |
| MovieId | int | |
| GenreID | int | |

Genre Table called genres

Gives each GenreID a name of genre. Each entry is a genre.

| Columns | Datatype | Description |
| --- | --- | --- |
| GenreID | int | |
| Genre\_name | Text | |

Actor connection table called **movies\_actor**

| Columns | Datatype | Description |
| --- | --- | --- |
| connectionID | int | |
| MovieId | int | |
| ActorID | int | |

Actor table called actors

| Columns | Datatype | Description |
| --- | --- | --- |
| ActorID | int | |
| forename | Text | |
| surname | Text | |
| More Info like age,oscars,.. | | There are at least 10000actors |

Language connection table called **movies\_language**

| Columns | Datatype | Description |
| --- | --- | --- |
| connectionID | int | |
| MovieId | int | |
| LanguageID | int | |

Language table called **languages**

| Columns | Datatype | Description |
| --- | --- | --- |
| languageId | int |   |
| Language | Text |   |

# Creation of the Database

For specific information look into the source code of the program creating the database on GitHub(https://github.com/JonathanKit/movie\_database).

## Creating the Tables

    cursor.execute(&#39;CREATE TABLE IF NOT EXISTS movies (movieID INTEGER PRIMARY KEY NOT NULL AUTO\_INCREMENT,title VARCHAR(100) UNIQUE, year INT, rated VARCHAR(30),released VARCHAR(50),runtime INT, genre VARCHAR(50), director VARCHAR(300), writer VARCHAR(300), plot VARCHAR(600), country VARCHAR(50), poster VARCHAR(200), rating\_imd FLOAT, rating\_rt INT, rating\_metacritic INT, rating\_metascore INT, rating\_imdb FLOAT, imdbVotes INT, imdbID VARCHAR(20), production VARCHAR(100));&#39;)

    cursor.execute(&#39;CREATE TABLE IF NOT EXISTS genres (genreID INTEGER PRIMARY KEY AUTO\_INCREMENT,genre\_name VARCHAR(32) NOT NULL UNIQUE);&#39;)

    cursor.execute(&#39;CREATE TABLE IF NOT EXISTS actors (actorID INTEGER PRIMARY KEY AUTO\_INCREMENT,forename VARCHAR(50), surname VARCHAR(50));&#39;)

    cursor.execute(&#39;CREATE TABLE IF NOT EXISTS languages (languageID INTEGER PRIMARY KEY AUTO\_INCREMENT,language VARCHAR(50) UNIQUE);&#39;)

    cursor.execute(&#39;CREATE TABLE IF NOT EXISTS movies\_genre( connectionID INTEGER PRIMARY KEY NOT NULL AUTO\_INCREMENT,movieID INTEGER NOT NULL, genreID INTEGER NOT NULL, FOREIGN KEY (movieID) REFERENCES movies (movieID) ON DELETE RESTRICT ON UPDATE CASCADE,FOREIGN KEY (genreID) REFERENCES genres (genreID) ON DELETE RESTRICT ON UPDATE CASCADE);&#39;)

    cursor.execute(&#39;CREATE TABLE IF NOT EXISTS movies\_language( connectionID INTEGER PRIMARY KEY NOT NULL AUTO\_INCREMENT,movieID INTEGER NOT NULL, languageID INTEGER NOT NULL, FOREIGN KEY (movieID) REFERENCES movies (movieID) ON DELETE RESTRICT ON UPDATE CASCADE,FOREIGN KEY (languageID) REFERENCES languages (languageID) ON DELETE RESTRICT ON UPDATE CASCADE);&#39;)

    cursor.execute(&#39;CREATE TABLE IF NOT EXISTS movies\_actor( connectionID INTEGER PRIMARY KEY NOT NULL AUTO\_INCREMENT,movieID INTEGER NOT NULL, actorID INTEGER NOT NULL, FOREIGN KEY (movieID) REFERENCES movies (movieID) ON DELETE RESTRICT ON UPDATE CASCADE,FOREIGN KEY (actorID) REFERENCES actors (actorID) ON DELETE RESTRICT ON UPDATE CASCADE);&#39;)

## Creating and adding the connection to the language/genre/… in the corresponding table if not existing

Adding non existing languages from a new movie to the languages table

![](RackMultipart20210109-4-123chxa_html_8e9d3767089f5684.gif)

#this function checks if a language is existing in the language table and adds it if not

    def create\_languages(cursor, languages):

    #print(cursor.execute(f&quot;SELECT \* from languages ;&quot;))

    if(isinstance(languages, str)):

        this\_language=languages

#check if the language is existing in the language table

        cursor.execute(f&quot;SELECT EXISTS(SELECT \* from languages WHERE language=\&quot;{this\_language}\&quot;);&quot;)

        existing\_language = cursor.fetchone()[0]

#if there is one new language add this language to the table

        if not(existing\_language):

            cursor.execute(f&quot;INSERT INTO languages (language) VALUES(\&quot;{this\_language}\&quot;);&quot;)

            print(&quot;language added: &quot;, this\_language)

    else:

#if there are multiple languages check them independently and add the new languages to the table

        for this\_language in languages:

            if not(cursor.execute(f&quot;SELECT EXISTS(SELECT \* from languages WHERE language=\&quot;{this\_language}\&quot;);&quot;)):

                cursor.execute(f&quot;INSERT INTO languages (language) VALUES(\&quot;{this\_language}\&quot;);&quot;)

                print(&quot;language added: &quot;, this\_language)

The same function is used for the other tables with multiple attributes

Creating the connection between the movie and its languages

    def add\_languages\_to\_movie(cursor, language, title):

    #check if a valid language(string) is send if not it is a list of strings, because there are multible languages for this movie

    if(isinstance(language, str)):

        one\_language = language

        #get the ID of the language from the language Table

        cursor.execute(f&quot;SELECT languageID FROM languages WHERE language =\&quot;{one\_language}\&quot;;&quot;)

        languageID = cursor.fetchone()[0]

        #get the ID of the movie that will be connected to his languages

        cursor.execute(f&quot;SELECT movieID FROM movies WHERE title =\&quot;{title}\&quot;;&quot;)

        movieID = cursor.fetchone()[0]

        #create the connection of movieID and langaugeID if not set yet

        cursor.execute(f&quot;INSERT IGNORE INTO movies\_language (movieID,languageID) VALUES(\&quot;{movieID}\&quot;,\&quot;{languageID}\&quot;);&quot;)

        #print(languageID[0])

    else:

        #here is the same as above for one language, but for mulitble languages if the movie has more than one

        for one\_language in language:

            cursor.execute(f&quot;SELECT languageID FROM languages WHERE language =\&quot;{one\_language}\&quot;;&quot;)

            languageID = cursor.fetchone()[0]

            cursor.execute(f&quot;SELECT movieID FROM movies WHERE title =\&quot;{title}\&quot;;&quot;)

            movieID = cursor.fetchone()[0]

            cursor.execute(f&quot;INSERT IGNORE INTO movies\_language (movieID,languageID) VALUES(\&quot;{movieID}\&quot;,\&quot;{languageID}\&quot;);&quot;)

            #print(languageID[0])



The same functions are used pretty similar for adding connections for other attributes.



Some problems in the program that occurred and had to be fixed:

- In given json text where elements containing \&quot; which is in sql interpreted as &quot; and causes an error
- Actor names are not always a name and surname, but can have 3 names or just 1
- The rating is stored in a list of rating. When there is no rating at all the variables for storing the non existing data are not created and referenced before assigned
- I had to add type of the movie, because some are series and should be able to classify them as series
