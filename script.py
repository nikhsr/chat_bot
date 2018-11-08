import discord
from wit import Wit
import http.cookiejar
import urllib.request
import requests
import bs4
TOKEN = 'NTA4MzgzODIzODYwNTk2NzU2.Dr-dFQ.CxGCMFAdJyDkP66eM9JSKPBzX78'
access_token = "G5X62DLGLJX6UNEWIBLYR57KMU6HUTJR"
cli = Wit(access_token = access_token)
client = discord.Client()
@client.event
async def on_message(message):
    message_text=message.content.lower()
    #await client.send_message(message.channel, message_text)
    if message.author == client.user:
        return

    if message.content.startswith('!hello') or message.content.startswith('hi') or message.content.startswith('heythere'):
        msg = 'Hello there glad to see you here. Well i am ernie the facebook recommend feed provider :) \n What can I help you with bud:{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    elif "bye" in message.content.lower():
        msg = 'Bye mate {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        await client.close()
    else:
    #message.content.startswith('show'):
        resp= cli.message(message_text)
        xx=resp['entities']['search_query'][0]['value']
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        authentication_url = "https://m.facebook.com/login.php"
        payload = {
            'email': "nikhilramsey@gmail.com",
            'pass': "nikhsrocks"
        }
        data = urllib.parse.urlencode(payload).encode('utf-8')
        req = urllib.request.Request(authentication_url, data)
        resp = urllib.request.urlopen(req)
        contents = resp.read()
        url = "https://m.facebook.com/search/str/"+str(xx)+"/keywords_blended_videos"
        data = requests.get(url, cookies=cj)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        
        for i in soup.prettify().split(" "):
            if i.__contains__("video_"):
                await client.send_message(message.channel,'https://m.facebook.com'+i[6:i.__len__()-1] )
                
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
