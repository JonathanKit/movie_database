# movie_database

Movie Database Creation flow:
1.	FIND-MOVIE get a list of all movies produced <br />
All movies are saved in the all_movies_list, Updated until 2019
2.	SEND-TITLE Send the title of the movie into ombdapi <br />
The script movies_to_json.py uses all the movies list to extract the information of all the titles listed there
3.	EXTRACT-INFO Receive and extract the information from the JSON file  <br />
4.	SAVE-DATABASE Save the data in a Database with MySQL <br />
These two steps are implemented in the info_json_to_movies.py script

