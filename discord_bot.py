import re
import jaconv
import discord
from pykakasi import kakasi

TOKEN = ''

kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()

client = discord.Client()

def isAlphabet(char):
    return re.match(r"^[a-zA-Z]+$", char) is not None

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print('------')

@client.event
async def on_message(message):
    if client.user in message.mentions:
        trans = conv.do(message.content)

        #英字以外を削ぎ落とす
        for i, part in enumerate(trans):
            if part == '>':
                index = i
                break
        trans = trans[index+1:]

        trans_arr =[]
        trans = trans.lower()
        for part in trans:
            if part != ' ' and isAlphabet(part):
                trans_arr.append(part)

        #スタンプに変換
        reg_list = []
        for char in trans_arr:
            reg = ':regional_indicator_{0}:'.format(char)
            reg_list.append(reg)
        result = ' '.join(reg_list)
    try:
        await message.channel.send(result)
    except discord.errors.HTTPException:
        await message.channel.send('FUCK YOU')


client.run(TOKEN)
