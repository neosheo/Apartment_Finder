from telegram_send import configure
import sys

def validate_answer(answer):
	if answer != 'y' and answer != 'n':
		print(f'Your answer: {answer}')
		print('Invalid answer')
		sys.exit()

# get user input for search parameters
state = input('What state do you want to search in? ')
city = input('What city do you want to search in? ')
bedrooms = input('How many bedrooms do you want to look for? (0 for any) ')
bathrooms = input('How many bathrooms do you want to look for? (0 for any) ')
hm_type = input('Type? (a for apartment, c for condo, h for house, t for townhouse) ')
if hm_type != 'a' and hm_type != 'c' and hm_type != 'h' and hm_type != 't':
	print('Invalid answer.')
	sys.exit()
min_price = input('What is your minimum price? ')
max_price = input('What is your maximum price? ')
dogs = input('Do you have dogs? (y or n) ')
validate_answer(dogs)
cats = input('Do you have cats? (y or n) ')
validate_answer(cats)
print('Please select all the additional filters you want to apply.')
laun_in = input('Laundry in the unit? (y or n) ')
validate_answer(laun_in)
laun_hk = input('Laundry hookups? (y or n) ')
validate_answer(laun_hk)
laun_os = input('Laundry on site? (y or n) ')
validate_answer(laun_os)
ac = input('A/C? (y or n) ')
validate_answer(ac)
elev = input('Elevator? (y or n) ')
validate_answer(elev)
garage = input('Garage? (y or n) ')
validate_answer(garage)
pool = input('Pool? (y or n) ')
validate_answer(pool)
loft = input('Loft? (y or n) ')
validate_answer(loft)
balc = input('Balcony? (y or n) ')
validate_answer(balc)
fire = input('Fireplace? (y or n) ')
validate_answer(fire)
gate = input('Gated? (y or n) ')
validate_answer(gate)
wc_acc = input('Wheelchair accessible? (y or n) ')
validate_answer(wc_acc)
furn = input('Furnished? (y or n) ')
validate_answer(furn)
dish = input('Dishwasher? (y or n) ')
validate_answer(dish)
fit = input('Fitness Center? (y or n) ')
validate_answer(fit)
park = input('Parking Available? (y or n) ')
validate_answer(park)
ut_inc = input('Utilities included? (y or n) ')
validate_answer(ut_inc)
inc_res = input('Income restricted? (y or n) ')
validate_answer(inc_res)
senior = input('Senior living? (y or n) ')
validate_answer(senior)
stud = input('Student living? (y or n) ')
validate_answer(stud)
lux = input('Luxury living? (y or n) ')
validate_answer(lux)
mil = input('Military living? (y or n) ')
validate_answer(mil)
short = input('Short-term? (y or n) ')
validate_answer(short)
cheap = input('Cheap? (y or n) ')
validate_answer(cheap)
min_rate_ask = input('Do you want a minimum rating? (y or n) ')
validate_answer(min_rate_ask)
if min_rate_ask == 'y':
	min_rate = input('4 or 5 stars? ')
	if min_rate != '4' and min_rate != '5':
		print('Invalid answer.')
		sys.exit()
else:
	min_rate = 0
keywords = input('Please enter any additional keywords, separated by commas.\n' )

if hm_type == 'a':
	home_type = 'Apartments'
if hm_type == 'c':
	home_type = 'Condos'
if hm_type == 'h':
	home_type = 'Houses'
if hm_type == 't':
	home_type = 'Townhouses'

if dogs == 'y' and cats == 'y':
	pets = 3
elif dogs == 'y' and cats == 'n':
	pets = 1
elif dogs == 'n' and cats == 'y':
	pets = 2
elif dogs == 'n' and cats == 'n':
	pets = 0

filters = 0
if laun_in == 'y':
	filters += 2
if laun_hk == 'y':
	filters += 1048576
if laun_os == 'y':
	filters += 2097152
if ac == 'y':
	filters += 16
if elev == 'y':
	filters += 524288
if garage == 'y':
	filters += 8388608
if pool == 'y':
	filters += 512
if loft == 'y':
	filters += 33554432
if balc == 'y':
	filters += 32
if fire == 'y':
	filters += 64
if gate == 'y':
	filters += 4194304
if wc_acc == 'y':
	filters += 131072
if furn == 'y':
	filters += 128
if dish == 'y':
	filters += 4
if fit == 'y':
	filters += 256
if park == 'y':
	filters += 65536
if ut_inc == 'y':
	filters += 16777216

spec = 0
if inc_res == 'y':
	spec += 32
if senior == 'y':
	spec += 1
if stud == 'y':
	spec += 4
if lux == 'y':
	spec += 512
if mil == 'y':
	spec += 2
if short == 'y':
	spec += 16
if cheap == 'y':
	spec += 256

rating = 0
if min_rate == '4':
	rating += 24
if min_rate == '5':
	rating += 16	

env_text = f'STATE="{state}"\nCITY="{city}"\nTYPE={home_type}\nBEDROOMS={bedrooms}\nBATHROOMS={bathrooms}\nMIN_PRICE={min_price}\nMAX_PRICE={max_price}\nPETS={pets}\nFILTERS={filters}\nSPECIALTIES={spec}\nMIN_RATING={rating}\nKEYWORDS="{keywords}"'

# write .env file
with open('.env', 'w') as f:
	f.write(env_text)

# create configs.txt
config_name = input("What should this configuration be named (don't include .config in name)? ")
config = f'{config_name}.config'
# configure telegram bot
configure(config, channel=False, group=False, fm_integration=False)

if os.path.isfile('configs.txt') == False:
	open('configs.txt', 'w').close()
with open('configs.txt', 'a') as f:
	f.write(config)

