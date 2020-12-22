from random import randint
from os import path, remove
import mechanize
import discord
import docker
import pathlib
import json
import re

import ressources

module_name = "baleine"
__version__ = "1.0.0"

localpath = pathlib.Path().absolute()
langfile = 'lang.json'
configfile = 'config.json'

def config(filename):
	global prefix, token
	try:
		# load json file
		with open(filename) as f:
			config = json.load(f)

			prefix = config["prefix"]
			token = config["token"]

			f.close()
			return True
	except:
		return False

def lang(filename):
	global langlist, data
	try:
		# load json file
		with open(filename) as f:
			data = json.load(f)
			langlist = []

			for i in range(len(data)):
				langlist.append(data[i]["name"])

			f.close()
			return True
	except:
		return False

def run(filename, path, lang):
	filepath = {'FILE_PATH':'/usr/src/runcode/'+filename}
	name = {'NAME':'/usr/src/runcode/'+(filename.split("."))[0]}

	# load env, mount volumes
	client = docker.from_env()
	output = client.containers.run(
		image=data[lang]["image"],
		command=data[lang]["command"].format(**filepath, **name),
		volumes={str(path):{"bind": "/usr/src/runcode", "mode": "rw"}},
		working_dir="/usr/src/runcode"
	)
	return output.decode()

def paste(content):
	br = mechanize.Browser()
	# create paste
	br.open("https://ctxt.io/")
	br.select_form(nr=0)
	br["content"] = content
	br.submit()
	return br.geturl()

class MyClient(discord.Client):
	async def on_ready(self):
		print(ressources.art+"\n")
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')
		if lang(langfile):
			print('Loaded '+langfile)
		else:
			print('Unable to load '+langfile)
		print('------')
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=prefix+"help"))

	async def on_message(self, message):
		# we do not want the bot to reply to itself
		if message.author.id == self.user.id:
			return

		for i in range(len(langlist)):
			if message.content.startswith(prefix+langlist[i]+'\n```'):
				# clean message content
				csynthax = re.findall(r''+prefix+langlist[i]+'\n```(.*)\n', message.content)
				msg = message.content.replace(prefix+langlist[i]+'\n```'+csynthax[0]+'\n','')
				msg = msg.replace('\n```','')

				# define tempfile
				tempfile = str(randint(10000,99999))+"."+data[i]["ext"]

				# check if a file with the same name already exist
				while path.exists(tempfile) is True:
					tempfile = str(randint(10000,99999))+"."+data[i]["ext"]

				# write tempfile
				f = open(tempfile, "x")
				f = open(tempfile, "w")
				f.write(msg)
				f.close()

				try:
					# mount volumes and run tempfile from localpath
					await client.change_presence(activity=discord.Game(name="Currently running '"+langlist[i]+"' snippet."))
					output = run(tempfile, localpath, i)
					await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=prefix+"help"))
					remove(tempfile)

					if output != "":
						await message.channel.send('> {0.author.mention}'.format(message)+'\n```\n'+output+'\n```')

				except Exception as error:
					await message.channel.send("> {0.author.mention}".format(message)+"\n```diff\n- Error : "+str(error).replace('`', '')+"\n```")
					await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=prefix+"help"))
					remove(tempfile)

			if message.content == prefix+langlist[i]:
				# explain synthax, host example on ctxt.io
				exc = prefix+langlist[i]+'<br>```'+data[i]["ext"]+'<br>'+data[i]["hello"]+'<br>```'
				example = paste(exc)
				await message.channel.send(">>> Usage : `"+prefix+"[language]`, then write down snippet between ``` marks (with carriage return).\nExample (expire in 1 hour) : "+example)

		if message.content == prefix+'help' or message.content == prefix+'h':
			# display help and info
			await message.channel.send(">>> '"+module_name+"' usage :\n(Run code snippets from Discord)\n```ini\n"+prefix+"help, "+prefix+"h 			# display help and info\n"+prefix+"list, "+prefix+"l 			# display all languages available\n"+prefix+"[language]		   # run code snippet```")

		if message.content == prefix+'list' or message.content == prefix+'l':
			# display all languages available
			await message.channel.send("> {0.author.mention}".format(message)+"\n```ini\n"+str(langlist)+"\n```")


if config(configfile):
	client = MyClient()
	client.run(token)
else:
	print("Unable to load "+configfile)