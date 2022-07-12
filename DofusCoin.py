from cmath import e
from email import message
from fileinput import filename
from glob import glob
from http import server
from urllib import response
from attr import mutable
import discord
import os
import requests 


#Global variables
client = discord.Client()
client.twitchUserG = ""
client.imageUser = ""
client.money = ""
client.roles = ""
client.emoji3 = ""


@client.event
async def on_ready():
    print("Le bot est prêt !")


@client.event
async def on_message(message):
    if message.channel == client.get_channel(981154130859024394):
        nick_member = message.author.nick
        if nick_member != None:
            #Le découpage du pseudo
            tblMemberSplit = nick_member.split("|")
            twitchUser = tblMemberSplit[1]
            twitchUser = twitchUser.replace(" ", "")

            
            #global variable
            client.twitchUserG = twitchUser

            #Ici on recupere le type de l'image
            messagePhotoUser = message.attachments[0].content_type
            client.imageUser = message.attachments[0].url

            #Condition sur les types d'images
            if messagePhotoUser == 'image/png' or messagePhotoUser == 'image/jpeg' or messagePhotoUser == 'image/jpg' or messagePhotoUser == 'image/webp':
                #Local variable 
                emoji = '1️⃣'
                emoji1 = '2️⃣'
                emoji2 = '3️⃣'
                client.emoji3 = '<:as:856290964145176616>'

                #Add reaction to the message
                await message.add_reaction(emoji)
                await message.add_reaction(emoji1)
                await message.add_reaction(emoji2) 
                await message.add_reaction(client.emoji3) 
            else:
                print("Erreur: Le format de l'image est incorrect !")
        elif nick_member == None:
            print(" ")

@client.event
async def on_reaction_add(reaction, user):
    #Le channel de facture
    channelAdmin = client.get_channel(981154130859024394)

    userRoles = user.roles
    for i in range(len(userRoles)):
        if userRoles[1].name != "DofusCoin":
            if userRoles[-1].name == "Modo" or userRoles[-1].name == "Dev":
                await channelAdmin.send("Oui")
                client.roles = userRoles[-1].name
                break 
            else:
                await reaction.remove(user)
    
    
    rolesRequire = "Dev"
    userTwitch = str(reaction.message.author.nick)
    userlink = reaction.message.attachments[0].url


    #Lien de l'api
    api_url = "https://wapi.wizebot.tv/api/currency/f731be14aa5946b9affedf141b823f6c/action/add/"+client.twitchUserG+"/"

    #Condition pour l'emoji choisi
    if str(reaction.emoji) == client.emoji3 and user != client.user and client.roles != "null":
        print(client.roles)
        if client.roles == rolesRequire:            
            #Local variable
            money = "10"
            client.money = money

            #Api
            api_url += money
            response = requests.get(api_url)
            response.json()

            #Embed le message de la facture
            embed=discord.Embed(title="Sai-bot | Facture", url=client.imageUser, description="Facture pour les points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-bot", icon_url="https://media.discordapp.net/attachments/980752522010587146/980806634228039700/unknown.png?width=825&height=825")
            embed.set_thumbnail(url=userlink)
            embed.add_field(name="Pseudo", value=userTwitch, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-bot v.1 | Facture")

            #envoie de l'embed sur le channel
            await channelAdmin.send(embed=embed)
            msg = reaction.message
            await reaction.message.clear_reactions()
            client.roles = ""
        else:
            await channelAdmin.send("Erreur vous etes:" + client.roles)
            await channelAdmin.send("Il vous faut le roles" + rolesRequire)
        
    elif reaction.emoji == '2️⃣' and user != client.user:
        if client.roles == rolesRequire:
            #Local variable
            money = "25"
            client.money = money

            #Api
            api_url += money
            response = requests.get(api_url)
            response.json()

            #Embed le message de la facture
            embed=discord.Embed(title="Sai-bot | Facture", url=client.imageUser, description="Facture pour les points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-bot", icon_url="https://media.discordapp.net/attachments/980752522010587146/980806634228039700/unknown.png?width=825&height=825")
            embed.set_thumbnail(url=client.imageUser)
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-bot v.1 | Facture")

            #envoie de l'embed sur le channel
            await channelAdmin.send(embed=embed)
            msg = reaction.message
            await reaction.message.clear_reactions()
            client.roles = ""
        else:
            await channelAdmin.send("Erreur vous etes:" + client.roles)
            await channelAdmin.send("Il vous faut le roles" + rolesRequire)

    elif reaction.emoji == '3️⃣' and user != client.user:
        money = "30"
        api_url += money
        client.money = money
        response = requests.get(api_url)
        response.json()

client.run("OTgwNzg2Nzc5OTI4MDE0OTE4.GAuL6M.eHQmvSGtLEmdwuG_kf7HI1ETpKaJmojayIirhE")
