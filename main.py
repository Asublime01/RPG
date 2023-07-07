from random import randint, choice
import time
from shopItems import *

health_potion = HealthPotion("Health Potion", 25)
normal_bait = NormalBait("Normal Bait", 50, 10)



player_default_health = 100
player_health = 100
wallet = 0
run = True
current_lvl = 1
exp = 0
monsters_killed = 0
bait = 6
fish_caught = 0


welcome_banner = f"""

        Welcome to Just An Average RPG!

           Controls
        --------------
        Type: 'fight' to attack different mobs

        Type: 'fish' (for obvious reasons)

        Type: 'bag', 'inv', or 'inventory' to view your health, wallet and LVL info

        Type: 'Shop' (also for obvious reasons)

        GOOD LUCK AND DON'T DIE!



\n"""

class Fish:
    def __init__(self, name, sell_value, rarity):
        self.name = name
        self.sell_value = sell_value
        self.rarity = rarity


def slime(player_health, wallet, exp, monsters_killed):
    slime_health = 20
    slime_xp = randint(15, 25)
    while slime_health > 0:
        player_dmg = randint(8, 16)
        print(f"You slice the slime for {player_dmg} DMG!\n")
        slime_health -= player_dmg
        time.sleep(1.2)
        slime_dmg = randint(1, 5)
        print(f"The slime attacks you for {slime_dmg} DMG.\n")
        player_health -= slime_dmg
        time.sleep(1.2)
    

    if player_health <= 0:
        return player_health, wallet, exp, monsters_killed
    
    coins = randint(5, 10)
    print(f"You vanquished the Slime!")
    print(f"You picked up {coins} coins.\n")
    wallet += coins
    exp += slime_xp
    monsters_killed += 1
    return player_health, wallet, exp, monsters_killed


def bandit(player_health, wallet, exp, monsters_killed):
    bandit_health = 30
    bandit_xp = randint(25, 34)
    while bandit_health > 0:
        player_dmg = randint(6, 18)
        print(f"You stab the bandit for {player_dmg} DMG!\n")
        bandit_health -= player_dmg
        time.sleep(1.2)
        bandit_dmg = randint(5, 13)
        print(f"The bandit shoots you with his slingshot for {bandit_dmg} DMG.\n")
        player_health -= bandit_dmg
        time.sleep(1.2)
    
    if player_health <= 0:
        return player_health, wallet, exp, monsters_killed

    print("You defeated the bandit!")
    monsters_killed += 1
    exp += bandit_xp
    bandit_chance = randint(1, 20)
    coins = randint(8, 16)
    if bandit_chance == 20:
        print("The Bandit had a secret stash! +30 Coins")
        wallet += 30
    else:
        print(f"You picked up {coins} Coins")
        wallet += coins
    return player_health, wallet, exp, monsters_killed

def evil_mage(player_health, wallet, exp, monsters_killed):
    mage_health = 35
    mage_xp = randint(35, 50)
    while mage_health > 0:
        player_dmg = randint(6, 18)
        print(f"You strike the mage with your dagger for {player_dmg} DMG!\n")
        mage_health -= player_dmg
        time.sleep(1.2)
        mage_dmg = randint(3, 12)
        print(f"The mage casts a spell on you for {mage_dmg} DMG!\n")
        player_health -= mage_dmg
        time.sleep(1.2)

    if player_health <= 0:
        return player_health, wallet, exp, monsters_killed
    
    print("You destroyed the Evil Mage!")
    monsters_killed += 1
    exp += mage_xp
    coins = randint(12, 20)
    print(f"You picked up {coins} Coins")
    wallet += coins
    return player_health, wallet, exp, monsters_killed


def shop(wallet, player_health, bait):
    print(f"""
╔═══════════════════════════════════════════╗
║               SHOP / INFIRMARY             ║
╟─────────────────────────────────────────────╢
║              ITEM    |    PRICE     |  QTY  ║
╟─────────────────────────────────────────────╢
║  [1]  Health Potion  |  25 Coins    |   1   ║
║                                             ║
║  [2]  Normal Bait    |  50 Coins    |  10   ║
║                                             ║
║  [0] Exit                                  ║
╚═══════════════════════════════════════════╝

                                """)
    while True:
        try:
            purchase_choice = int(input(f"Enter # to purchase or exit| Wallet Balance: {wallet} /> "))
            if purchase_choice == "":
                print("Please enter a valid option.")
                continue
            elif purchase_choice == 0:
                print("Leaving the shop...")
                break
            elif purchase_choice == 1:
                if wallet - health_potion.item_amount < 0:
                    print("You can't afford this item.")
                    continue
                elif wallet - health_potion.item_amount >= 0:
                    print("You bought a Health Potion!")
                    wallet -= health_potion.item_amount
                    input("Press 'enter' drink your potion.")
                    print("Your health has been restored!")
                    player_health = player_default_health
                    continue
            elif purchase_choice == 2:
                if wallet - normal_bait.item_amount < 0:
                    print("You can't afford this item.")
                    continue
                elif wallet - normal_bait.item_amount >= 0:
                    print("You bought 10 Normal Bait!")
                    wallet -= normal_bait.item_amount
                    print("Your fishing supplies have been added to your tackle box.")
                    bait += normal_bait.item_qty
                    continue 
            else:
                print(f"{purchase_choice}, is invalid.")
                continue
        except ValueError:
            print("Please enter a valid option.")
            continue

    return wallet, player_health, bait
                

class Fish:
    def __init__(self, name, sell_value, exp):
        self.name = name
        self.sell_value = sell_value
        self.exp = exp

def fish(bait, wallet, exp, fish_caught):
    print("Type 'cast' to cast your line, type 'exit' to go back home")
    fish_list = [
        Fish("Finara", 5, 10),
        Fish("Aquilia", 8, 16),
        Fish("Nixor", 11, 18),
        Fish("Marix", 14, 23),
        Fish("Sirel", 17, 30),
        Fish("Tritus", 20, 35),
        Fish("Azura", 23, 41),
        Fish("Coralix", 26, 44),
        Fish("Lumos", 29, 51),
        Fish("Seraphish", 35, 60)
    ]

    while True:
        fishing_input = input(f"\nBait: {bait} Wallet: {wallet} Coins > ")
        if fishing_input.lower() == "exit":
            return bait, wallet, exp, fish_caught
        elif fishing_input.lower() == "cast":
            pass
        else:
            print("Please type one of the 2 options.")
            continue
        
        if bait <= 0:
            print("You don't have any bait.")
            continue

        print("You cast out your line...\n")
        time.sleep(1)
        catch_chance = randint(0, 1)
        if 0 <= catch_chance <= 0.2:
            print("A fish stole your bait!\n")
            bait -= 1
            continue
        elif 0.2 < catch_chance <= 1:
            random_fish = choice(fish_list)
            if random_fish.name[0].lower() == "a":
                print(f"You caught an {random_fish.name}!\n")
                print(f"The {random_fish.name} drops {random_fish.sell_value} Coins and returns to the water\n")
                wallet += random_fish.sell_value
                bait -= 1
                exp += random_fish.exp
                fish_caught += 1
            else:
                print(f"You caught a {random_fish.name}!\n")
                print(f"The {random_fish.name} drops {random_fish.sell_value} Coins and returns to the water.\n")
                wallet += random_fish.sell_value
                bait -= 1
                exp += random_fish.exp
                fish_caught += 1
                
                
print(welcome_banner)


while run and player_health > 0:
    user_choice = input(f"({current_lvl})> ").lower()
    if user_choice == "fight":
        spawn_chance = randint(1, 3)
        if spawn_chance == 1:
            print("You find yourself toe to toe with a SLIME!!!")
            player_health, wallet, exp, monsters_killed = slime(player_health, wallet, exp, monsters_killed)

            if exp >= 150:
                current_lvl += 1
                exp = 0
                print(f"Congrats Player! You are Level {current_lvl}!")
                continue
                
        elif spawn_chance == 2:
            print("You found a BANDIT lurking in the bushes!!!")
            player_health, wallet, exp, monsters_killed = bandit(player_health, wallet, exp, monsters_killed)

            if exp >= 150:
                current_lvl += 1
                exp = 0
                print(f"Congrats Player! You are Level {current_lvl}!")
                continue

        elif spawn_chance == 3:
            print("You are cornered by an Evil Mage!")
            player_health, wallet, exp, monsters_killed = evil_mage(player_health, wallet, exp, monsters_killed)

            if exp >= 150:
                current_lvl += 1
                exp = 0
                print(f"Congrats Player! You are Level {current_lvl}!")
                continue

        else:
            print("Error")
    elif user_choice == "inv" or user_choice == "inventory" or user_choice == "bag":
        print(f"""
              
              Wallet: {wallet} Coins                Health: {player_health}

              Current LVL: {current_lvl}            EXP/Next LVL: {exp}/150

              """)
    elif user_choice == "shop":
        print("Entering the shop...")
        time.sleep(1.5)
        wallet, player_health, bait = shop(wallet, player_health, bait)
    elif user_choice == "fish":
        print("Traveling to the Lake...")
        time.sleep(1.5)
        bait, wallet, exp, fish_caught = fish(bait, wallet, exp, fish_caught)

        if exp >= 150:
            current_lvl += 1
            exp = 0
            print(f"Congrats Player! You are Level {current_lvl}!")
            continue







if player_health <= 0:
    print(f"""

   _____          __  __ ______     ______      ________ _____  
  / ____|   /\   |  \/  |  ____|   / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__     | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|    | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____   | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|   \____/   \/   |______|_|  \_|
          
                    IT LOOKS LIKE YOU DIED :(
          MAYBE YOU SHOULD USE A HEALTH POTION NEXT TIME :P
                            
                --------------STATS---------------
          
                MONSTERS KILLED: {monsters_killed}
                COINS COLLECTED: {wallet}
                HIGHEST LVL: {current_lvl}
                FISH CAUGHT: {fish_caught}
                                                                                                                                                                                       

    
    """)

