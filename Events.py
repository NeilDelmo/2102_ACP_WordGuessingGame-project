import Main

def eventone():
    print("""You are walking in the town and is on the way to complete a quest that has time limit.
    You need to reach it in 30 minutes or you wont complete the quest.
    It was then that you see a little girl crying in the ground.     
    You ask her why she is crying.     
    She said she lost her pet lizard and she cant find her pet now.     
    If you decided to help her find and catch her pet lizard you won't""")
    action = input("Do want to ignore the little girl or help her? Select between Ignore(I)/Help(H)")
    if action.upper() == 'I':
        print("You have decided to ignore her and go on your own way.")
        Main.stats['Endurance'] += 2
        Main.money += 50
        print("Your Endurance has increased. Current stats:", Main.stats)
    elif action.upper() == 'H':
        print("You decided to help the little girl.")
        Main.stats['Dexterity'] += 1
        Main.money += 80
        print("Your Strength has increased. Current stats:", Main.stats)
    else:
        print("Invalid action. Please select either Ignore(I) or Help(H).")


def eventtwo():
    print("""You are walking in a jungle """)
