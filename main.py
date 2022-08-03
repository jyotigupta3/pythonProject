<<<<<<< HEAD

from selenium import webdriver
from tabulate import tabulate
import requests


def test_run():
    driver = webdriver.Chrome()
    driver.get('https://www.game.tv/')
    driver.maximize_window()

    games = driver.find_elements("xpath", "//div[@class='overlay-game-details']/div[contains(@class, 'name')]")
    games_list = []
    if len(games) != 0:
        for game in games:
            games_list.append(game.text)
    print([games_list.strip() for games_list in games_list])

    elements = driver.find_elements('xpath', "//li[contains(@class, 'game-card')]/a")
    links = [element.get_attribute('href') for element in elements]
    print(links)
    status = []
    for url in links:
        response = requests.get(url)
        status.append(response)

    print(status)
    data_list = []
    for i in range(0, len(games_list)):
        data = [i + 1, games_list[i], links[i], status[i]]
        data_list.append(data)
    table = tabulate(data_list, headers=["#", "Game name", "Page URL", "Page Status"])
    print(table)


if __name__ == "__main__":
    test_run()
=======

from selenium import webdriver
from tabulate import tabulate
import requests


def test_run():
    driver = webdriver.Chrome()
    driver.get('https://www.game.tv/')
    driver.maximize_window()

    games = driver.find_elements("xpath", "//div[@class='overlay-game-details']/div[contains(@class, 'name')]")
    games_list = []
    if len(games) != 0:
        for game in games:
            games_list.append(game.text)
    print([games_list.strip() for games_list in games_list])

    elements = driver.find_elements('xpath', "//li[contains(@class, 'game-card')]/a")
    links = [element.get_attribute('href') for element in elements]
    print(links)
    status = []
    for url in links:
        response = requests.get(url)
        status.append(response)

    print(status)
    data_list = []
    for i in range(0, len(games_list)):
        data = [i + 1, games_list[i], links[i], status[i]]
        data_list.append(data)
    table = tabulate(data_list, headers=["#", "Game name", "Page URL", "Page Status"])
    print(table)


if __name__ == "__main__":
    test_run()
>>>>>>> master
