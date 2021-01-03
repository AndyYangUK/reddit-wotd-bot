#!/usr/bin/python3
import praw
import re
import datetime

reddit = praw.Reddit(client_id="reddit client id",
                     client_secret="reddit secret",
                     password="account password",
                     user_agent="WOTD bot v1 by andyyanguk",
                     username="account username")

subreddit = reddit.subreddit("askreddit")

# Get list of comments responded to...
with open("output/responded_to.txt", "r") as f:
    responded_to = f.read()
    responded_to = responded_to.split("\n")
    responded_to = list(filter(None, responded_to))

# open the WOTD file scraped from dictionary.com
with open("output/scraped_wotd.txt", "r") as f:
    wotd = f.read()
    print('Word of the day is',wotd)

# Loops through comments continuously
for top_level_comment in subreddit.stream.comments():
    # Then check if word of the day is in the comments
    if re.search(wotd, top_level_comment.body, re.IGNORECASE) \
            and top_level_comment.id not in responded_to \
            and top_level_comment.author != 'bot_word_of_the_day':

        #Response
        bot_reply = f"""**Fun fact:** [{wotd}](https://www.dictionary.com/e/word-of-the-day/) 
        is the word of the day! \n\n ^------------------- \n\n*I'm just a lowly bot. Beep boop.*"""

        top_level_comment.reply(bot_reply)

        # **** Storing outputs ****

        # Get current time and write to output.
        now = str(datetime.datetime.now())
        print(now, "Responded to", top_level_comment.author, "on comment", top_level_comment.id)
        with open("logs/wotd-bot.txt", "a") as f:
            f.write(now + "\n" + "Responded to " + str(top_level_comment.author) + " on comment " + top_level_comment.id + "\n")

        # Keep a record of comments that have been responded to, and add to external file.
        responded_to.append(top_level_comment.id)
        with open("output/responded_to.txt", "w") as response:
            for top_level_comment in responded_to:
                response.write(top_level_comment + "\n")
