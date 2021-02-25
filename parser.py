from bs4 import BeautifulSoup
import telebot
import requests
import schedule
import random
import time

#Create a sender BOT
TOKEN = '1208478917:AAGVbjzVyeXFGNZ8kGUQKJHlDIEPQX_8LQg'
bot = telebot.TeleBot(TOKEN)
group_id = 668618297
#Parser body
url = 'http://tafsir.ru'
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
titles = soup.findAll('p')

hadis = []
for x in titles:
	hadis.append(x.text.strip())



def get_hadis_today():
	bot.send_message(group_id, f' Bugunlik matn : \n << {hadis[2]} >>')

schedule.every().minute.at(':15').do(get_hadis_today)

while True:
	schedule.run_pending()
	time.sleep(1)
