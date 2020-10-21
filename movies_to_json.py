#This script is for creating a database of movies 
apikey1notinuse = "21f2a1c4"
apikey1 = "be18616c"
#the movies to extract have to be in a csv list under this path with a "," as delimiter
path_movies = 'D:\Sofia_courses\Database\list_of_all_movies_edited.csv'
#the location where the json with the information will be saved, the information is saved additionally
path_json = 'D:\Sofia_courses\Database\movies_json.txt'

import json
import urllib
import urllib.request
import csv
import pickle
import sqlite3

#function to search for a title and return the JSON with the movie information
def search_movie(title):
    print('Retrieving the data of ',title,' now… ')
    if len(title) < 2 : 
        print("This is no title")
        return -1

    #create the url to search the title
    serviceurl = "http://www.omdbapi.com/?"
    url = serviceurl + urllib.parse.urlencode({'t': title})+ "&" +urllib.parse.urlencode({'apikey':apikey1})
    
    
    #print(url)
    #fetch the data
    try:
        uh = urllib.request.urlopen(url, timeout = 5)
    except:
        try:
            print("request failed, try again")
            uh = urllib.request.urlopen(url, timeout = 10)
        except:
            print("failed again try one more time without timeout")
            uh = urllib.request.urlopen(url)
    data = uh.read()
    json_data=json.loads(data)

    #check if the right data is received
    if json_data['Response']=='True':
        #print(json_data)
        return json_data
    #movie is not found
    elif json_data['Response']=='False':
        print("Error: Could not find the movie")
        return -1
    else: 
        print("Error: unknown, maybe check the received json file")
        return -1

#pickle the whole list of movies
def pickle_whole_movie_list():
    #with open('D:\Sofia_courses\Database\list_of_all_movies_edited.csv') as csv_file:
    with open(path_movies) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for movie_title_list_read in csv_reader:
            with open('D:\Sofia_courses\Database\left_movies.pkl', 'wb') as f:
                pickle.dump(movie_title_list_read, f)
            print("succesful pickeled ", len(movie_title_list_read), " movies")
    
def pickle_leftover_movie_list(leftover_movies_list):
    with open('D:\Sofia_courses\Database\left_movies.pkl', 'wb') as f:
        pickle.dump(leftover_movies_list, f)
    print("succesful pickeled ", len(leftover_movies_list), " movies")

def unpickle_leftover_movie_list():
    with open('D:\Sofia_courses\Database\left_movies.pkl', 'rb') as f:
        titles_left = pickle.load(f)
        return titles_left
     





def save_in_json(json_data):
    if(json_data != -1):
        with open('D:\Sofia_courses\Database\movies_json.txt', 'a') as file:
            movie_add_string = "\""+json_data["Title"]+ "\"" + ":"
            file.write(movie_add_string)
            file.write(json.dumps(json_data, indent=4 ))
            file.write(",")
        

def run_movie_extraction():
    
    run=1050
    runthis = 1
    while(runthis<run):
        #unpickle the leftover movies
        titles_left = unpickle_leftover_movie_list()
        runthis +=1
        #get newest first title of list
        movie_title = titles_left.pop()
        #extract its json with info
        movieInfo_json = search_movie(movie_title)
        #save in the database
        #save_in_database(movieInfo_json)
        #so far just into json
        save_in_json(movieInfo_json)
        #print(whole_json)
        #write_json(whole_json)
        print("there are >",len(titles_left),"< movies left")
        pickle_leftover_movie_list(titles_left)

#use this tho pickle all movies, never do this again!
#######pickle_whole_movie_list()
run_movie_extraction()
