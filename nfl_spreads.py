# Football Stats
# Assignment 9, Part 1
# By: Joshua Rifkin

import requests
from bs4 import BeautifulSoup


def downloadData(url):
    file = requests.get(url)
    return file.content


def parse(webpage):
    print("\n\n --- Final Week Four NFL Football Spreads: 9/26 - 9/30, 2019 --- \n\n")
    output = "Date: {0} \nFavorite: {1} \nUnderdog: {2} \nSpread: {3}"
    soup = BeautifulSoup(webpage, "html5lib")
    games = soup.find('table', attrs={'cols': '4'})
    currGames = games.find_all('tr')[1:]

    for game in currGames:
        print(output.format(game.contents[1].text, game.contents[3].text, game.contents[7].text, game.contents[5].text))
        print('\n---------------------------------------------------\n')



def main():
    link = 'http://www.footballlocks.com/nfl_point_spreads_week_4.shtml'
    webpage = downloadData(link)
    parse(webpage)


if __name__ == '__main__':
    main()
