from telegram_send import configure

# get user input for search parameters
state = input('What state do you want to search in? ')
city = input('What city do you want to search in? ')
bedrooms = input('How many bedrooms do you want to look for? ')
min_price = input('What is your minimum price? ')
max_price = input('What is your maximum price? ')

env_text = f'STATE="{state}"\nCITY="{city}"\nBEDROOMS={bedrooms}\nMIN_PRICE={min_price}\nMAX_PRICE={max_price}'

# write .env file
with open('.env', 'w') as f:
	f.write(env_text)

config_name = input("What should this configuration be named (don't include .config in name)? ")
config = f'{config_name}.config'
# configure telegram bot
configure(config, channel=False, group=False, fm_integration=False)

if os.path.isfile('configs.txt') == False:
	open('configs.txt', 'w').close()
with open('configs.txt', 'a') as f:
	f.write(config)
