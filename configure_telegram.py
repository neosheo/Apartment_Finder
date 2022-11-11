from telegram_send import configure
import os

# configure telegram
config_name = input("What should this configuration be named? (don't include .config in name) ")
config = f'{config_name}.config'

configure(config, channel=False, group=False, fm_integration=False)

if os.path.isfile('configs.txt') == False:
	open('configs.txt', 'w').close()
with open('configs.txt', 'a') as f:
	f.write(config)

