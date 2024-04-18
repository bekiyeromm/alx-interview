#!/usr/bin/env python3
"""
"""

import requests
import sys


def get_characters(movie_id):
    """
    finds characters from film data
    """
    film_url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(film_url)
    film_data = response.json()
    character_urls = film_data["characters"]

    characters = []
    for character_url in character_urls:
        character_data = requests.get(character_url).json()
        characters.append(character_data["name"])

    return characters


def main():
    """
    main func
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <Movie ID>")
        return

    movie_id = sys.argv[1]
    characters = get_characters(movie_id)

    for character in characters:
        print(character)


if __name__ == "__main__":
    main()
