# Football Stats
# Assignment 9, Part 1
# By: Joshua Rifkin

import requests
from bs4 import BeautifulSoup


def downloadData(url):
    file = requests.get(url)
    return file.content


def parse(webpage):
    print("Top 20 Players NFL")
    output = "#{0} | Player: {1} | Position: {2} | Team: {3} | Touchdowns: {4}"
    soup = BeautifulSoup(webpage, "html5lib")
    topPlayers = soup.find_all('tr', class_={"row1", "row2"})
    i = 1
    for player in topPlayers:
        print(output.format(i, player.contents[0].text, player.contents[1].text, player.contents[2].text,
                            player.contents[6].text))
        i += 1
        if i > 20:
            break


def main():
    link = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns'
    webpage = downloadData(link)
    parse(webpage)


if __name__ == '__main__':
    main()