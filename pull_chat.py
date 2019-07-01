import socket
import pandas as pd
import csv
import os

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'gimme_data'
token ='REDACTED'
if not os.path.exists('twitch_chat.csv'):
	with open('twitch_chat.csv', 'w') as f:
		writer = csv.DictWriter(f, fieldnames = ["Channel", "Username", "Message"])
		writer.writeheader()

def find_info(text):
	if '\r\n:' in text:
		username = text.split('!')[0]
		find_channel = text.split('PRIVMSG #')[1]
		channel = find_channel.split(' :')[0]
		raw_message = find_channel.split(' :')[1]
		message = raw_message.split('\r\n:')[0]
		remove = text.split('\r\n:')[0] + '\r\n:'
		next_block = text[len(remove):]
		if not username.lower().endswith('bot') and message != '':
			with open('twitch_chat.csv', 'a') as f:
				writer = csv.writer(f)
				writer.writerow([channel, username, message])
		find_info(next_block)
	else:
		username = text.split('!')[0]
		find_channel = text.split('PRIVMSG #')[1]
		channel = find_channel.split(' :')[0]
		remove = text[1:].split(':')[0]
		message = text[1:].replace(remove, '')[1:]
		if '\r\n' in message:
			message = message.replace('\r\n', '')
		if not username.lower().endswith('bot') and message != '':
			with open('twitch_chat.csv', 'a') as f:
				writer = csv.writer(f)
				writer.writerow([channel, username, message])

def scrape_chat(channel_name):
	channel = '#' + channel_name
	sock = socket.socket()
	sock.connect((server, port))
	sock.send(f"PASS {token}\n".encode('utf-8'))
	sock.send(f"NICK {nickname}\n".encode('utf-8'))
	sock.send(f"JOIN {channel}\n".encode('utf-8'))
	while True:
		response = sock.recv(2048).decode('utf-8')
		if 'PRIVMSG #' in response:
			break
	while True:
		response = sock.recv(2048).decode('utf-8')
		print(response)
		if response.startswith('PING'):
			sock.send("PONG\n".encode('utf-8'))
			print('Pinged Server!')
		else:
			response = response[1:]
			find_info(response)

scrape_chat('disguisedtoast')