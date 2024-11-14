import Main  # Import the main module to access its variables

shop_items = {
    "Health Potion": 100,
    "Sword": 150,
    "Shield": 75
}

def eventone():
    print("""You are walking in the town and are on the way to complete a quest that has a time limit.
    You need to reach it in 30 minutes or you won't complete the quest.
    It was then that you see a little girl crying on the ground.     
    You ask her why she is crying.     
    She said she lost her pet lizard and she can't find her pet now.     
    If you decided to help her find and catch her pet lizard you won't""")
    action = input("Do you want to ignore the little girl or help her? Select between Ignore(I)/Help(H): ")
    if action.upper() == 'I':
        print("You have decided to ignore her and go on your own way.")
        Main.stats['Endurance'] += 2
        Main.money += 50
        print("Your Endurance has increased. Current stats:", Main.stats)
    elif action.upper() == 'H':
        print("You decided to help the little girl.")
        Main.stats['Dexterity'] += 1
        Main.money +=  80
        print("Your Dexterity has increased. Current stats:", Main.stats)
    else:
        print("Invalid action. Please select either Ignore(I) or Help(H).")

def eventtwo():
    print("""'HELP!! SOMEONE PLEASE HELP!!!'
    You hear a woman screaming in the distance. You rush over to find a broken down carriage and a woman 
    on her knees surrounded by armed bandits. You can decide if you want to help her or not.
    """)
    action = input("Do you want to rescue her or run? Rescue(R)/Run(E): ")
    if action.upper() == 'R':
        print("You have decided to rescue the woman. The bandits take out their weapons.")
        print("'You should have minded your own business!'")
        if Main.stats['Strength'] and Main.stats['Dexterity'] < 10:
            Main.life -= 1
            print("You were overpowered by the bandits! You lost 1 life.")
            print(Main.status())
            if Main.life <= 0:
                print("You have no lives left. Game Over.")
                return
        elif Main.stats['Strength'] and Main.stats['Dexterity'] >= 10:
            print("You have defeated the bandits and have save the woman")
            Main.money += 50
            print(f"The woman has given you {Main.money} gold as a reward.")
            Main.stats['Strength'] += 1
            print("You have become stronger fighting those bandits and become stronger.")
            print("You have gained 1 strength")
            print(Main.status)
    elif action.upper() == 'E':
        print("You chose to run away and avoid the confrontation.")
    else:
        print("Invalid action. Please select either Rescue(R) or Run(E).")