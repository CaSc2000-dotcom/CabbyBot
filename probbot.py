import praw
import re
import random
import os
import pdb
import reprlib
import sys

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

if not os.path.isfile(r"comments_replied_to.txt"):
   comments_replied_to = []
else:
   with open(r"comments_replied_to.txt", "r") as f:
      comments_replied_to = f.read()
      comments_replied_to = comments_replied_to.split("\n")
      comments_replied_to = list(filter(None, comments_replied_to))

def start():
   for comment in subreddit.stream.comments():
      if comment.id not in comments_replied_to:
         
         print ("Reading comment id:", comment.id)
         print ("\t" + repr(comment.body.encode("utf-8")))
                  
         if re.match("!cabbybothelp", comment.body, re.IGNORECASE):
            print ("Input received as HELP")
            
            reply = "Commands for CabbyBot:\n\n!RollTheDice\n\n!FlipTheCoin\n\n!RPS [rock, paper, or scissors]\n\n!CabbyBotHelp"
            print ("Response generated")
            print ("Now replying...")
            comment.reply(reply)
            print ("Reply finished!")
            
            comments_replied_to.append(comment.id)
         
         if re.match("!rollthedice", comment.body, re.IGNORECASE):
            print ("Received input as ROLLTHEDICE")
            
            result = random.randint(1, 6)
            print ("Generated number:", result)
            
            reply = "You rolled the die, and you've received the number...\n\n" + str(result)
            print ("Response generated:\n\t" + repr(reply))
            
            print ("Now replying...")
            comment.reply(reply)
            print ("Reply finished!\n")
            
            comments_replied_to.append(comment.id)
#----------------------------------------------------------------------------
         if re.match("!flipthecoin", comment.body, re.IGNORECASE):
            print("Received input as FLIPTHECOIN")
            
            ht = ['', 'heads', 'tails']
            result = random.randint(1, 2)
            print ("Generated number:", result)
            
            reply = "You flipped the coin, and you've recieved...\n\n" + ht[result]
            print ("Response generated:\n\t" + repr(reply))
            
            print ("Now replying...")
            comment.reply(reply)
            print ("Reply finished!\n")
            
            comments_replied_to.append(comment.id)
#---------------------------------------------------------------------------
         if re.match("!rps", comment.body, re.IGNORECASE):
            print ("Input received as RPS")
            
            arsenal = ['', 'rock', 'scissors', 'paper']
            
            choice = random.randint(1, 3)
            print ("Gemerated number:", choice)
            
            pChoiceNum = 0
            pChoice = ""
            
            if comment.body[5] == 'r':
               pChoice = "rock"
               pChoiceNum = 1
            elif comment.body[5] == 's':
               pChoice = "scissors"
               pChoiceNum = 2
            elif comment.body[5] == 'p':
               pChoice = "paper"
               pChoiceNum = 3
            print ("RPS input received as:", pChoice)
            
            reply = "You've chosen: " + pChoice + "\n\nAnd I chose: " + arsenal[choice]
            
            if pChoiceNum == 1:
               if choice == 2:
                  reply += "\n\nYou won!"
               elif choice == 3:
                  reply += "\n\nI win!"
               else:
                  reply += "\n\nWe tied!"
            elif pChoiceNum == 2:
               if choice == 3:
                  reply += "\n\nYou won!"
               elif choice == 1:
                  reply += "\n\nI win!"
               else:
                  reply += "\n\nWe tied!"
            else:
               if choice == 1:
                  reply += "\n\nYou won!"
               elif choice == 2:
                  reply += "\n\nI win!"
               else:
                  reply += "\n\nWe tied!"
            
            print ("Response generated:\n\t", repr(reply))
            
            print ("Now replying...")
            comment.reply(reply)
            print ("Reply finished!\n")
            
            comments_replied_to.append(comment.id)
#----------------------------------------------------------------
      with open(r"comments_replied_to.txt", "w") as f:
         for comment_id in comments_replied_to:
            f.write(comment_id + "\n")
            
#------------------------------------------------#

initialize = input("Press enter to start bot\n")
start()
