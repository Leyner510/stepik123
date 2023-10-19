import requests
from fake_headers import Headers
from bs4 import BeautifulSoup

def get_headers():
    return Headers(browser='Yandex', os='win').generate()
main_stepik_https = requests.get('https://zazloo.ru/category/stepik/stepik-pokolenie-python/',headers=get_headers()).text
main_stepik_soup = BeautifulSoup(main_stepik_https,'lxml')


def page_1():
    main_stepik_theme = main_stepik_soup.find_all('div',class_='entry-title')
    for i in main_stepik_theme:
        url = i.select_one('a').get('href')
        question = input('Нужны ли вам темы с 15.6 по 13.2?(Номер темы смотрите в ссылке которая вам выводится!):  ')
        if 'да' in question:
            print(url)
        elif 'нет' in question:
            break


page_1()

main_stepik_https_1 = requests.get('https://zazloo.ru/category/stepik/stepik-pokolenie-python/page/2/',headers=get_headers()).text
main_stepik_soup_1 = BeautifulSoup(main_stepik_https_1,'lxml')
def page_2():
    main_stepik_theme_1 = main_stepik_soup_1.find_all('div',class_='entry-title')
    for i in main_stepik_theme_1:
        url = i.select_one('a').get('href')
        question = input('Нужны ли вам темы с 13.1 по 11.2?(Номер темы смотрите в ссылке которая вам выводится!):  ')
        if 'да' in question:
            print(url)
        elif 'нет' in question:
            break
page_2()

main_stepik_https_2 = requests.get('https://zazloo.ru/category/stepik/stepik-pokolenie-python/page/3/',headers=get_headers()).text
main_stepik_soup_2 = BeautifulSoup(main_stepik_https_2,'lxml')
def page_3():
    main_stepik_theme_2 = main_stepik_soup_2.find_all('div',class_='entry-title')
    for i in main_stepik_theme_2:
        url = i.select_one('a').get('href')
        question = input('Нужны ли вам темы с 11.1 по 8?(Номер темы смотрите в ссылке которая вам выводится!):  ')
        if 'да' in question:
            print(url)
        elif 'нет' in question:
            break
page_3()

main_stepik_https_3 = requests.get('https://zazloo.ru/category/stepik/stepik-pokolenie-python/page/4/',headers=get_headers()).text
main_stepik_soup_3 = BeautifulSoup(main_stepik_https_3,'lxml')
def page_4():
    main_stepik_theme_3 = main_stepik_soup_3.find_all('div',class_='entry-title')
    for i in main_stepik_theme_3:
        url = i.select_one('a').get('href')
        question = input('Нужны ли вам темы с 7.9 по 6.2?(Номер темы смотрите в ссылке которая вам выводится!):  ')
        if 'да' in question:
            print(url)
        elif 'нет' in question:
            break
page_4()

main_stepik_https_4 = requests.get('https://zazloo.ru/category/stepik/stepik-pokolenie-python/page/5/',headers=get_headers()).text
main_stepik_soup_4 = BeautifulSoup(main_stepik_https_4,'lxml')
def page_5():
    main_stepik_theme_4 = main_stepik_soup_4.find_all('div',class_='entry-title')
    for i in main_stepik_theme_4:
        url = i.select_one('a').get('href')
        question = input('Нужны ли вам темы с 6.3 по 2.3?(Номер темы смотрите в ссылке которая вам выводится!):  ')
        if 'да' in question:
            print(url)
        elif 'нет' in question:
            break
page_5()

main_stepik_https_5 = requests.get('https://zazloo.ru/category/stepik/stepik-pokolenie-python/page/6/',headers=get_headers()).text
main_stepik_soup_5 = BeautifulSoup(main_stepik_https_5,'lxml')
def page_6():
    main_stepik_theme_5 = main_stepik_soup_5.find_all('div',class_='entry-title')
    for i in main_stepik_theme_5:
        url = i.select_one('a').get('href')
        question = input('Нужна ли вам тема 2.2?(Номер темы смотрите в ссылке которая вам выводится!):  ')
        if 'да' in question:
            print(url)
        elif 'нет' in question:
            break
page_6()
