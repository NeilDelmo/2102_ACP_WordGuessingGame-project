import random
from Events import eventone, eventtwo

# Player's life
life = 5
# Player's job and stats initialization
jobname = ""
stats = {}
money = 100
inventory = []

def status():
    lives_display = " ".join(["(@)" for _ in range(life)])  # Create a string of "(@)" for each life
    print(f"Remaining Lives: {lives_display}")
    print(f"Current Stats: {stats}")
    print(f"Money: {money}")


def character_job(job):
    global jobname, stats  # Declare jobname and stats as global to modify them
    if job.upper() == 'W':
        stats = {
            "Strength": 12,
            "Dexterity": 8,
            "Endurance": 10,
        }
        jobname = "Warrior"
    elif job.upper() == 'A':
        stats = {
            "Strength": 8,
            "Dexterity": 12,
            "Endurance": 10,
        }
        jobname = "Archer"
    else:
        print("No such job as of now")
        return None  # Return None if job is invalid
    return stats  # Return the stats dictionary

def main_game():
    global life
    while life > 0:
        # List of events
        events = [eventone, eventtwo]
        random.shuffle(events)
        for event in events:
            event()  # Call the event function
            if life <= 0:  # Check if life is 0 after each event
                print("You have no lives left. Returning to the main menu...")
                return  # Exit the main game loop

while True:
    print("Welcome to the Adventure Game")
    name = input("Enter the Character's name: ")
    job = input("Please select between Warrior(W) or Archer(A): ")
    character_stats = character_job(job)

    if character_stats:  # Check if character_stats is not None
        print(f"""You always dreamed of being an adventurer. So as a kid, you trained to become a {jobname}.
        Now that you have grown up, you feel like you can explore the world.
        You decided to embark on this adventure to become stronger and become legendary. 
        Will you succeed in the end though? Only time will tell.""")

        main_game()  # Start the game
    else:
        print("Please restart the game and choose a valid job.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thank you for playing! Goodbye!")
        break  # Exit the game loop