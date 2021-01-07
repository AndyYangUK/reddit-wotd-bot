# Reddit Word of the Day Bot
A simple Reddit bot that monitors subreddit comments to see if they have used the word of the day from dictionary.com, and responds to the commentor to let them know that they have used the word of the day.

## File structure:
* **wotd.py**: a script that scrapes the word of the day from dictionary.com and writes 2 output files.
    * **logs/scrape_wotd.txt**: contains a log of all the script runs
    * **output/scraped_wotd.txt**: contains the current word of the day
* **wotd-search-and-reply.py**: the actual reddit bot, it will continuously monitor comments on a specific subreddit, and creates 2 output files.
    * **logs/wotd-bot.txt**: a log of when the bot has successfully responded to comments.
    * **output/responded_to.txt**: a list of comment IDs that the bot has responded to, to prevent responding to the same comments multiple times.
* **EXAMPLE - cron-setup.txt**: an example crontab file to run the bot autonomously.
