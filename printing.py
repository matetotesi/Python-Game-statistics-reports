import reports
from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title

file_name = str(input('Enter your file name: '))
year = int(input('Enter the year: '))
genre = str(input('Enter the genre: '))
title = str(input('Enter the title: '))


def main():
    a = count_games(file_name)
    b = decide(file_name, year)
    c = get_latest(file_name)
    d = count_by_genre(file_name, genre)
    e = get_line_number_by_title(file_name, title)
    print('Number of games: ', a)
    print('Have game in your year: ', b)
    print('Latest game: ', c)
    print('Numbers of your selected genre: ',d)
    print('Your title in in: ', e, '. line')

if __name__ == "__main__":
    main()
# Printing functions
