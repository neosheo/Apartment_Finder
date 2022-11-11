# Apartment_Finder

This python script will search the website apartmentfinder.com for apartments that meet your search criteria and sends you links to the apartments on Telegram.

# Installation

Clone the repo and install dependencies with pip.

    git clone https://github.com/neosheo/Apartment_Finder.git
    cd Apartment_Finder
    pip install -r requirements.txt
    
If the pip command doesn't work try replacing "pip" with "pip3".

# Telegram set up

Set up a telegram bot (https://learn.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0#create-a-new-telegram-bot-with-botfather)
Make sure to run the command /token in a chat with @BotFather to get your bot's access token.

# Configuring

Run configure.py

    python configure.py
    
Here you can set your search parameters and paste your bot's access token. You will get a code when it is complete, add the bot on telegram and send it the code to finish.
If the python command doesn't work try replacing "python" with "python3"

# Usage

Once all is set up just run with:

    python apartment_finder.py
    
If the python command doesn't work try replacing "python" with "python3"
