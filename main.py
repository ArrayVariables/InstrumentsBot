import discord
import random
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print("static 2")
	await client.change_presence(game=discord.Game(name="Type }>help"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif message.content.startswith("}>coinflip"):
		choice = random.randint(1,4)
		if choice == 1:
			await client.add_reaction(message, "🍍")
		if choice == 2:
			await client.add_reaction(message, "🛫")
		if choice == 3:
			await client.add_reaction(message, "🎁")
		if choice == 4:
			await client.add_reaction(message, "🔧")
	elif message.content.startswith("}>8ball"):
		await client.send_message(message.channel, random.choice(["Yes, I agree, (or whatever)",
	                                                                                                                    "So confused, what are you trying to say?",
	                                                                                              			          "No, my mind is telling me that I disagree."]))
	elif message.content.startswith("}>help"):
		embed=discord.Embed(title="Command List", color=0x00ff00)
		embed.add_field(name="}>8ball", value="Answers inaccurately.")
		embed.add_field(name="}>ping", value="Pong!")
		embed.add_field(name="}>help", value="Shows a help list of commands.")
		embed.add_field(name="}>evalprint", value="Safe. Prints a text.")
		embed.add_field(name="}>bonzi", value="random")
		embed.add_field(name="}>coinflip", value="Flips a emoji, not a coin.")
		embed.add_field(name="}>botinfo", value="Shows a info of the bot.")
		embed.add_field(name="BOT DEVELOPER ONLY", value="`}>shutdown`, `}>eval`, `}>reboot`")
		embed.add_field(name="}>cleverbotinfo", value="Shows the CleverBot info.")
		embed.add_field(name="}>invite", value="Invite the bot!")
		await client.send_message(message.channel, embed=embed)
	elif message.content.startswith("./cmdhelp 8ball"):
		await client.add_reaction(message, "✅")
		await client.send_message(message.channel, "8ball - A fun command whenever you qgot the chance to demand the bot to answer your question! Although fun, being answered can be extremely inaccurate.")
	elif message.content.startswith("./cmdhelp ping"):
		await client.add_reaction(message, "✅")
		await client.send_message(message.channel, "./ping - A extremely inspired piece of art from other bots.")
	elif message.content.startswith("./cmdhelp coinflip"):
		await client.add_reaction(message, "✅")
		await client.send_message(message.channel, "./coinflip - Actually picks a emoji, not flip a coin, so a fun command.")
	elif message.content.startswith("./cmdhelp help"):
		await client.add_reaction(message, "✅")
		await client.send_message(message.channel, "./help - Direct messages you a help list, its actually notable for a very few mistakes observed.")
	elif message.content.startswith("./ende ende"):
		await client.send_message(message.channel, "ende ende")
	elif message.content.startswith("}>evalprint"):
		variable = message.content[len("./evalprint"):].strip()
		await client.send_message(message.channel, variable)
	elif message.content.startswith("}>bonzi"):
		await client.send_message(message.channel, "hi, i am bonzi buddy, to get started, plz type ./hell")
	elif message.content.startswith("}>hell"):
		await client.send_message(message.channel, "./bonzi and ./hell are actually a joke")
	elif message.content.startswith("}>eval"):
		message.author.id == "383561620661731329"
		await client.send_message(message.channel, eval(input)).format(python(result))
	elif message.content.startswith("<@413857586006458368> go eat shit The Pip"):
		await client.send_message(message.channel, "***throws a skittle at you***")
	elif message.content.startswith("<@413857586006458368> Hello. The Pip."):
		await client.send_message(message.channel, "Hello.")
	elif message.content.startswith("<@413857586006458368> fite me irl"):
		await client.send_message(message.channel, "Okay, fite me plez. ***throws a skittle at you***")
	elif message.content.startswith("}>botinfo"):
		embed=discord.Embed(title="Bot Info")
		embed.add_field(name="CleverBot prefix as a mention?", value="Yes.", inline=False)
		embed.add_field(name="Library used", value="discord.py", inline=False)
		embed.add_field(name="Editor used", value="Python IDLE 3.5.4+", inline=False)
		embed.add_field(name="Virtual Private Server?", value="Nope, not yet.", inline=True)
		embed.set_footer(text="Bot Version beta v1.7.98b-r")
		await client.send_message(message.channel, embed=embed)
	elif message.content.startswith("}>ping"):
		await client.send_message(message.channel, "`Pong!`")
	elif message.content.startswith("}>shutdown"):
		message.author.id == "383561620661731329"
		await client.send_message(message.channel, "Now shutting down...")
		await asyncio.sleep(3)
		await client.send_message(message.channel, "Successful!")
		await client.logout()
	elif message.content.startswith("}>invite"):
		await client.send_message(message.channel, "```You can invite the bot here, but this has no music, so no musics.``` https://discordapp.com/api/oauth2/authorize?client_id=416163484414246912&permissions=0&scope=bot")
	elif message.content.startswith("<@413857586006458368> are u homeless or alone m8"):
		await client.send_message(message.channel, "yes mate")
	elif message.content.startswith("}>cleverbotinfo"):
		embed=discord.Embed(title="CleverBot Info")
		embed.add_field(name="Coded manually?", value="Yes mate.")
		embed.add_field(name="Used CleverBot API?", value="Nope.")
		embed.add_field(name="Prefix", value="A ping.")
		embed.set_footer(text="cleverbot v1.8b and credits goes to the CleverBot library.")
		await client.send_message(message.channel, embed=embed)
	elif message.content.startswith("}>reboot"):
		message.author.id == "383561620661731329"
		await client.send_message(message.channel, "Please wait.. **Rebooting..**")
		await asyncio.sleep(3)
		await client.send_message(message.channel, "Success!")
		await client.logout()
		await client.login()
      
client.run("classified idiot")
