# Mad Libs Generator


play_again = input("Start Game - yes/no:  ").lower()
while play_again == "yes":
    print("Welcome to Mad Libs Game!")
    # Bats are so cool (Simple mad lib story)
    color     = input("Enter color: ")
    adjective = input("Enter adjective: ")
    time      = input("Enter time: ")
    adjective1 = input("Enter adjective: ")
    place     = input("Enter place: ")
    food      = input("Enter food: ")
    food1     = input("Enter food: ")
    verb      = input("Enter verb: ")
    noun      = input("Enter noun: ")
    number    = input("Enter number: ")
    print()
    print("\n ======= Here's your Mad Libs Story ========\n")
    print(f"Bats are so cool! They are {color}, {adjective} animals with wings.\n" 
          f"They like to fly around at {time}, which makes some people scared of them.\n" 
          f"But bats are {adjective1}, and they don’t want to hurt people.\n"
          f"I have a pet bat that lives in a {place}. I like to feed him {food} and {food1}.\n" 
          f"He likes to {verb}.I am his favorite person, but he also likes his {noun}.\n" 
          f"I want to convince my parents to get me {number} more bats.")
    print()
    play_again = input("play again - yes/no: ").lower()
