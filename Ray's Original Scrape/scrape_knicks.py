# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
from datetime import datetime
import time
import sqlite3
from sqlite3 import Error


def scrape():
    
    #--------------Knicks Players Stats------------------------
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path)

    # URL of page to be scraped
    url = 'http://www.rotoworld.com/player/nba/2382/kristaps-porzingis'
    browser.visit(url)
    # time.sleep(5)
    # Scrape page into soup
    html = browser.html

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html,'lxml')
    #     print(soup)
    
    results = soup.find_all("div", class_='playernews')
    # print(results)

    for result in results:

        title=result.find("div", class_='report')
    #     print(title)

        paragraph=result.find("div", class_="impact")
    #     print(paragraph)

        latest_news = title.text
        print(latest_news)

        latest_para = paragraph.text
        print(latest_para)

    results = soup.find("div", class_='playerphoto')
    src=[img['src'] for img in results.find_all('img')]
    picture_link=src[0]
    print(picture_link)
    
    #     table=pd.read_html(url)[0].rename(index=str, columns={"0": "Category", "1": "Fact"})
    #     html_table=table.to_html(na_rep = "",index=False)
    table=pd.read_html(url)[0]
    Team_table=table.to_html(na_rep = "",index=False)
    table=pd.read_html(url)[1]
    Player_general=table.to_html(na_rep = "",index=False)
    table=pd.read_html(url)[2]
    Season_stats=table.to_html(na_rep = "",index=False)
    table=pd.read_html(url)[3]
    Career_averages=table.to_html(na_rep = "",index=False)
    table=pd.read_html(url)[4]
    Career_stats=table.to_html(na_rep = "",index=False)

    knicks_player_results={
        "latestnews":latest_news,
        "newsparagraph":latest_para,
        "headshot":picture_link,
        "KnicksTeam":Team_table,
        "GeneralPlayerInfo":Player_general,
        "SeasonStats":Season_stats,
        "CareerAverages":Career_averages,
        "Career":Career_stats
    }
    
    return knicks_player_results


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
