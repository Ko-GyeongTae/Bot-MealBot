import discord
import datetime
import requests
import time
from ast import literal_eval

token = ""

msg = "x"
now = "X"
tommorrow = "x"

class MealBot(discord.Client):
    channel = "NULL"
    print("debug ready")

    async def on_ready(self):
        print("Start ready...")
        #Game, Streaming, CustomActivity
        game = discord.Game("!도움 요청")
        #계정상태 변경
        await client.change_presence(status=discord.Status.online, activity=game)
        print("Ready to Action...")

    async def on_message(self, message):
        # sender == bot ? None
        breakfast = "X"
        lunch = "X"
        dinner = "X"
        t_breakfast = "X"
        t_lunch = "X"
        t_dinner = "X"

        if message.author.bot:
            return None
        now = datetime.datetime.now()
        tommorrow = now + datetime.timedelta(days=1)

        date = now.strftime('%Y-%m-%d')
        t_date = tommorrow.strftime('%Y-%m-%d')

        log = str(message.author) + ' :: ' + message.content
        log += ' :: ' + str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' \
            + str(time.localtime().tm_mday)
        log += ' :: ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' \
               + str(time.localtime().tm_sec)
        url = f'https://api.dsm-dms.com/meal/{date}'
        t_url = f'https://api.dsm-dms.com/meal/{t_date}'
        html = requests.get(url).text
        t_html = requests.get(t_url).text

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

        t_meal = literal_eval(t_html)
        if "breakfast" in str(t_meal):
            t_breakfast_dic = t_meal[t_date]['breakfast']
            t_breakfast = str(t_breakfast_dic)
            t_breakfast = t_breakfast.translate({ord('['): '', ord(']'): '', ord("'"): '', ord(','): '\n'})
        if "lunch" in str(t_meal):
            t_lunch_dic = t_meal[t_date]['lunch']
            t_lunch = str(t_lunch_dic)
            t_lunch = t_lunch.translate({ord('['): '', ord(']'): '', ord("'"): '', ord(','): '\n'})
        if "dinner" in str(t_meal):
            t_dinner_dic = t_meal[t_date]['dinner']
            t_dinner = str(t_dinner_dic)
            t_dinner = t_dinner.translate({ord('['): '', ord(']'): '', ord("'"): '', ord(','): '\n'})
            print(t_dinner)
        print(log)

        if message.content == '!도움':
            channel = message.channel
            msg = "```\n!오늘급식 - 하루의 모든 급식 보여줌\n"
            msg += "!아침 - 아침밥 보여줌\n"
            msg += "!점심 - 점심밥 보여줌\n"
            msg += "!저녁 - 저녁밥 보여줌\n"
            msg += "!내일급식 - 내일급식 전체 보여줌\n```"
            await channel.send(msg)
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

        if message.content == "!아침":
            channel = message.channel
            msg = "```\n" + "####" + date + "####"
            msg += "\n\n*** 아침 ***\n" + ' ' + breakfast
            msg += "\n\n```"
            await channel.send(msg)
            return None

        if message.content == "!점심":
            channel = message.channel
            msg = "```\n" + "####" + date + "####"
            msg += "\n\n*** 점심 ***\n" + ' ' + lunch
            msg += "\n\n```"
            await channel.send(msg)
            return None

        if message.content == "!저녁":
            channel = message.channel
            msg = "```\n" + "####" + date + "####"
            msg += "\n\n*** 저녁 ***\n" + ' ' + dinner
            msg += "\n\n```"
            await channel.send(msg)
            return None

        if message.content == "!내일급식":
            channel = message.channel
            msg = "```\n" + "####" + t_date + "####"
            msg += "\n\n*** 아침 ***\n" + ' ' + t_breakfast
            msg += "\n\n*** 점심 ***\n" + ' ' + t_lunch
            msg += "\n\n*** 저녁 ***\n" + ' ' + t_dinner
            msg += "\n\n```"
            await channel.send(msg)
            return None


if __name__ == "__main__":
    client = MealBot()
    print(token)
    client.run(token)
