import discord
import datetime
import requests
import smtplib
from bs4 import BeautifulSoup
from ast import literal_eval

token = "token"

breakfast = "x"
lunch = "x"
dinner = "x"


class MealBot(discord.Client):
    async def on_ready(self):
        #Game, Streaming, CustomActivity
        game = discord.Game("요리")

        #계정상태 변경
        await client.change_presence(status=discord.Status.online, activity=game)
        print("Ready to Action...")

    async def on_message(self, message):
        # sender == bot ? None
        if message.author.bot:
            return None

        if message.content == "!오늘급식":
            channel = message.channel
            msg = "```\n" + "####" + date + "####"
            msg += "\n\n*** 아침 ***\n" + ' ' + breakfast
            msg += "\n\n*** 점심 ***\n" + ' ' + lunch
            msg += "\n\n*** 저녁 ***\n" + ' ' + dinner
            msg += "\n\n```"
            await channel.send(msg)
            return None

if __name__ == "__main__":
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    # date = '2020-08-19'

    url = f'https://api.dsm-dms.com/meal/{date}'
    html = requests.get(url).text

    # soup = BeautifulSoup(html, 'html.parser')
    meal = literal_eval(html)
    if "breakfast" in str(meal):
        breakfast_dic = meal[date]['breakfast']
        breakfast = str(breakfast_dic)
        breakfast = breakfast.translate({ord('['): '', ord(']'): '', ord("'"): '', ord(','): '\n'})
    if "lunch" in str(meal):
        lunch_dic = meal[date]['lunch']
        lunch = str(lunch_dic)
        lunch = lunch.translate({ord('['): '', ord(']'): '', ord("'"): '', ord(','): '\n'})
    if "dinner" in str(meal):
        dinner_dic = meal[date]['dinner']
        dinner = str(dinner_dic)
        dinner = dinner.translate({ord('['): '', ord(']'): '', ord("'"): '', ord(','): '\n'})
    print(meal)
    print(breakfast)
    print(lunch)
    print(dinner)
    client = MealBot()
    client.run(token)
