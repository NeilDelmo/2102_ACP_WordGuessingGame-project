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


def eventthree():
    print("""As you continue your journey, you come across a group of townsfolk gathered around a signpost.
    A local athlete is organizing a stamina race, boasting that the winner will receive a hefty reward of gold.
    The challenge is simple: run a set distance through the forest and back. 
    However, the race is known to be quite grueling, and only those with high Endurance can hope to succeed.
    """)

    action = input("Do you want to participate in the race (P) or walk away (W)? ")
    if action.upper() == 'P':
        print("You have chosen to participate in the race.")
        print("The race begins, and you push yourself to your limits!")

        # Check if the player's Endurance is high enough
        if Main.stats['Endurance'] >= 10:
            print("Your high Endurance allows you to maintain a steady pace, and you finish the race in first place!")
            Main.money += 100
            Main.stats['Endurance'] += 1
            print("You have won 100 gold and gained 1 Endurance point! Current stats:", Main.stats)
        else:
            print("You struggle to keep up with the other racers and finish in last place.")
            print("Although you didn't win, you pushed yourself hard.")
            Main.stats['Endurance'] += 1  # Increase Endurance slightly for effort
            print("You gain 1 Endurance point for your effort. Current stats:", Main.stats)

    elif action.upper() == 'W':
        print("You decided not to participate and walk away from the race.")
        Main.stats['Endurance'] += 1  # Slight increase for walking away, as it's still a decision
        print("You gain 1 Endurance point for your decision to conserve energy. Current stats:", Main.stats)

    else:
        print("Invalid action. Please select either Participate (P) or Walk Away (W).")