from encodings import search_function
from instabot import *


bot = Bot()

users_to_follow = ["colin.skinner", "ava.franchi"]

# bot.follow_users(users_to_follow)
user_input = ""

# Code for what the bot should do
while(not user_input == "quit"):

    user_input = input("What should I do?")
    
    # Follows a user
    if user_input == "follow":
        to_follow = input("Who should I follow?")
        bot.follow(to_follow)
    
    # Unfollows a user
    if user_input == "unfollow":
        to_unfollow = input("Who should I follow?")
        bot.unfollow(to_unfollow)

    # Messages someone
    if user_input == "message":
        recipient = input("Who should I message?")
        message = input("What should I say?")
        bot.send_message(message, recipient)
    
    if user_input == "count followers":
        recipient = input("Which account?")
        followers = bot.get_user_followers(recipient)
        print("Total number of followers:")
        print(len(followers))

    # if user_input == "count following":
    #     recipient = input("Which account?")
    #     followers = bot.get_user_followers(recipient)
    #     print("Total number of followers:")
    #     print(len(followers))
    
    if user_input == "search followers":
        acc = input("Which account?")
        followers = bot.get_user_followers(acc)
        print("Search for who?")
        search = input("Which account?")
        if search in followers:
            print(f"{search} is following {acc}")
        else:
            print(f"{search} isn't following {acc}")

    

