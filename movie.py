#pylint: disable=invalid-name
#pylint: disable=consider-using-enumerate
#pylint: disable=pointless-string-statement
#pylint: disable=trailing-whitespace
#pylint: disable=syntax-error
#pylint: disable=redefined-outer-name
#pylint: disable=bad-option-value
#pylint: disable=line-too-long

import requests
import os
import dotenv
import json

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def DrStrange():
    """
    method
    """
    BASE_URL = "https://api.themoviedb.org/3/movie/453395?"
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
    query_params = {
    "api_key": os.getenv("MOVIE_KEY"), }

    response = requests.get(BASE_URL, params=query_params)
    data = (response.json())                    #full list of json items
    Dr_list1 = []                                  #variable to hold the genre names
    genres =[{'id': 14, 'name': 'Fantasy'}, {'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}]
    Dr_title = (data["title"])
    Dr_tagline = (data["tagline"])
    poster = (data["poster_path"])
    Dr_image2 = f"{IMAGE_BASE_URL}{poster}"   #image base URL and the poster size 
                                                           #concatenate the base URL for the movie poster with the poster path
    for i in range(len(genres)):                           #for loop to extract the genre names from the genres json dictionary
        Dr_list1.append(genres[i]["name"])

    return(Dr_title,Dr_tagline,Dr_list1,Dr_image2) 


def Spiderman():
    """
    method
    """
    BASE_URL = "https://api.themoviedb.org/3/movie/634649?"
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
    query_params = {
    "api_key": os.getenv("MOVIE_KEY"),}

    response = requests.get(BASE_URL, params=query_params)
    data = (response.json())
    Spider_list1 = []
    genres =[{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 878, 'name': 'Science Fiction'}]
    Spider_title = (data["title"])
    Spider_tagline = (data["tagline"])
    poster = (data["poster_path"])
    Spider_image2 = f"{IMAGE_BASE_URL}{poster}"   #image base URL and the poster size 
    

    for i in range(len(genres)):
        Spider_list1.append(genres[i]["name"])
    
    return(Spider_title,Spider_tagline,Spider_list1,Spider_image2)    
 

def KingsMan():
    """
    method
    """
    BASE_URL = "https://api.themoviedb.org/3/movie/476669?"
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
    query_params = {
    "api_key": os.getenv("MOVIE_KEY"),}

    response = requests.get(BASE_URL, params=query_params)
    data = (response.json())
    King_list1 = []
    genres =[{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}]
    King_title = (data["title"])
    King_tagline = (data["tagline"])
    poster = (data["poster_path"])
    King_image2 = f"{IMAGE_BASE_URL}{poster}"   #image base URL and the poster size 
    


    for i in range(len(genres)):
        King_list1.append(genres[i]["name"])

    return(King_title,King_tagline,King_list1,King_image2)