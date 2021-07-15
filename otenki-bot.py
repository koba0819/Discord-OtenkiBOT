import discord
import requests
import json
import settings

json_file = open('citycode.json', encoding='utf-8' )
citycode = json.load(json_file)

token = settings.key
client = discord.Client()

@client.event
async def on_ready():
    print('-------------')
    print('logged in')
    print('BOT Name:', client.user.name)
    print('BOT ID:', client.user.id)
    print('-------------')

@client.event
async def on_message(message):

    if message.author.bot:  #BOTのメッセージを無視
        return

    if citycode[message.content] != message.content: #メッセージがjsonに記述されたものと一致
        code = citycode[message.content]["code"]
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%code
        d = requests.get(url).json()

        for i in range(3):

            max_temp = d['forecasts'][i]['temperature']['max']
            min_temp = d['forecasts'][i]['temperature']['min']

            if max_temp is not None and min_temp is not None:

                embed = discord.Embed(title=d['forecasts'][i]['dateLabel'] + ", " + d['forecasts'][i]['date'] + ' ' + d['location']['city'] + "の天気") 
                embed.add_field(name="天候", value=d['forecasts'][i]['telop'])
                embed.add_field(name="気温", value="最高" + max_temp['celsius'] + "度 最低" + min_temp['celsius'] + "度")
                embed.set_thumbnail(url=d['forecasts'][i]['image']['url'])
                await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title=d['forecasts'][i]['dateLabel'] + ", " + d['forecasts'][i]['date'] + ' ' + d['location']['city'] + "の天気") 
                embed.add_field(name="天候", value=d['forecasts'][i]['telop'])
                embed.add_field(name="気温", value="気温は不明です")
                embed.set_thumbnail(url=d['forecasts'][i]['image']['url'])
                await message.channel.send(embed=embed)

client.run(token)