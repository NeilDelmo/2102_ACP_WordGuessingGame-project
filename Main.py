import random
from Events import eventone

life = 5
jobname = ""
stats = {}
money = 100
def character_job(job):
    global jobname  # Declare jobname as global to modify it
    if job.upper() == 'W':
        stats = {
            "Strength": 12,
            "Dexterity": 8,
            "Endurance": 15,
            "Intelligence": 10
        }
        jobname = "Warrior"
    elif job.upper() == 'A':
        stats = {
            "Strength": 10,
            "Dexterity": 15,
            "Endurance": 10,
            "Intelligence": 12
        }
        jobname = "Archer"
    else:
        print("No such job as of now")
        return None  # Return None if job is invalid
    return stats  # Return the stats dictionary

def showstat(stats):
    print(f"Current Stats: {stats}")
    print(money)

def main_game():
    # List of events
    events = [eventone]
    random.shuffle(events)
    for event in events:
        event()



print("Welcome to the Adventure Game")
name = input("Enter the Character's name: ")
job = input("Please select between Warrior(W) or Archer(A): ")
character_stats = character_job(job)

if character_stats:  # Check if character_stats is not None
    print(f"""You always dreamed of being an adventurer. So as a kid, you trained to become a {jobname}.
    Now that you have grown up, you feel like you can explore the world.
    You decided to embark this adventure to become stronger and become legendary. 
    Will you succeed in the end though? Only time will tell.""")

else:
    print("Please restart the game and choose a valid job.")