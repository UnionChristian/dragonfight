import tools.dice as dice
import player.hero as hero
import enemies.dragon.dragon as dragon
import json
import time


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def gameover():
    print(color.RED + "YOU LOSE! YOU'RE A LOSING LOSER THAT LOSES!" + color.END)
    exit()
    
def youwin():
    print(color.GREEN + "YOU WIN! Congrats, now get a job!" + color.END)
    exit()

hero_dictionary = hero.hero_data
dragon_dictionary = dragon.dragon_data

print("You are the great " + hero_dictionary["class"] + ", " + color.BOLD + hero_dictionary["name"] + color.END)
time.sleep(2)
print("You must face the evil " + dragon_dictionary["species"] + ", " + color.RED + dragon_dictionary["name"] + color.END);
time.sleep(2)
for i, val in enumerate(hero_dictionary["weapons"]):
  print("\t" + color.GREEN + str(i+1) + color.END + ": " + color.BOLD + val["name"] + color.END) 
  print("\t\t" + "Strength: " + str(val["strength"]) + " | " + "Speed: " + str(val["speed"])) 
# print(color.GREEN + "1: " + color.END + hero_dictionary["weapons"][0])
weapon_choice = int(input("Chooser your weapon wisely..."))
weapon = hero_dictionary["weapons"][weapon_choice - 1]
print("You have chosen " + weapon["name"])
print("You are surrounded by sheer cliffs on all sides.")
print("You now face the great " + dragon_dictionary["species"])
print("He is inspecting you, trying to decide to eat you or simply kill you...")
time.sleep(2)
print("The " + dragon_dictionary["species"] + " runs at you closing the distance in seconds.")
print("What do you do?")
print("\t" + color.GREEN + "1: " + color.END + " Run away")
print("\t" + color.GREEN + "2: " + color.END + " Stand and Fight!")
print("\t" + color.GREEN + "3: " + color.END + " Reason with him")
action1 = input();


match action1:
    case "1":
        print("You are able to slip through a crack in the wall behind you!")
        time.sleep(2)
        print("You survive, but as you are running, the wolves smell your wet pants.")
        print("You die a coward's death eaten by wolves while cryng for your mother.")
        gameover()
        
    case "2":
        print("you attack the beast...")
        roll = dice.roll(hero_dictionary["attack"])
        
        if (roll >= 7):
            print("Direct Hit to the beast's neck!")
            damage = (int(hero_dictionary["attack"]) + int(weapon["strength"])) - (int(dragon_dictionary["armor"])/10)
            if(damage < 0):
                damage = 2
            dragonHP = int(dragon_dictionary["hitpoints"]) - int(damage)
            print("The beast's health is now down to " + str(dragonHP))
            if(dragonHP < 1):
                print("You have slayed the beast!!")
                youwin()
            else:
                print("The dragon strikes back, crushing you with his tail")
                gameover()
        elif (roll > 4 & roll < 7):
            print("Your " + weapon["action"] + " hits the beasts flank, causing some damage...")
            damage = (int(hero_dictionary["attack"]) + int(weapon["strength"])) - int(dragon_dictionary["armor"])
            if(damage < 0):
                damage = 1
            dragonHP = int(dragon_dictionary["hitpoints"]) - int(damage)
            print("The beast's health is now down to " + str(dragonHP))
            if(dragonHP < 1):
                print("You have slayed the beast!!")
                youwin()
            else:
                print("The dragon strikes back, slicing you in half with his claws")
                gameover()
            
            
        else:
            print("Your weapon glances off the dragons hide without effect...")
            print("The beast burns you to death with his flame")
            gameover()
    case "3":
        print("You try talking to him...")
        roll = dice.roll(hero_dictionary["inteligence"])
        print(roll)
        if(roll > dragon_dictionary["inteligence"]):
            print("He looks at you curiously and waits for you to speak.")
            print("what do you say?")
            print("\t" + color.GREEN + "1: " + color.END + " Sup cutie, you lookin' fine today!")
            print("\t" + color.GREEN + "2: " + color.END + " Such a great and powerful creature should not concern yourself with an ant like me.")
            print("\t" + color.GREEN + "3: " + color.END + " If you let me go, I can bring you more food than you can eat.")
            choice = input()
            
            if(choice == "1"):
                roll = dice.roll(hero_dictionary["charisma"])
                if(roll >= dragon_dictionary["inteligence"]):
                    print("You two live together for ever after. Pretty sure this isn't winning, but your live...")
                else:
                    print("He is disgusted by your advances. He stomps you into the ground and burns your body to ash")
                    gameover()
                    
            if(choice == "2"):
                roll = dice.roll(hero_dictionary["charisma"])
                if(roll > dragon_dictionary["inteligence"]):
                    print("You convince him to leave you alone. He flys off to kill another village.");
                    youwin()
                else:
                    print("The dragon sees through your flattery and burns you alive.")
                    gameover()
            if(choice == "3"):
                roll = dice.roll(hero_dictionary["charisma"])
                if(roll > dragon_dictionary["inteligence"]):
                    print("He agrees and waits for you to return with food.");
                    print("You live, at least until the he finds you again.")
                    youwin()
                else:
                    print("The dragon does not trust your taste in food. He decides to eat you intead.")
                    gameover()
        elif(roll == dragon_dictionary["inteligence"]):
            print("The dragon is confused, so he decides to bite your head off.")
            gameover()
        else:
            print("The dragon doesn't care for your stupid words. He eats you legs first to increase the pain.")
            gameover()
        