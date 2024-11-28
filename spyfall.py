import random
import os
import sys
import time

word_bank = [
    "dog", "cat", "lion", "giraffe", "whale", "bird", "fish", "elephant", "car", "plane",
    "tree", "moon", "piano", "computer", "television", "guitar", "apple", "banana", "pear",
    "orange", "tiger", "shark", "dolphin", "rabbit", "robot", "superhero", "vampire", "wizard",
    "ice cream", "pizza", "hamburger", "taco", "sushi", "spaghetti", "chicken", "cake", "cookie",
    "soda", "chocolate", "watermelon", "coffee", "milkshake", "bicycle", "scooter", "skateboard",
    "hat", "socks", "shoes", "jacket", "shirt", "pants", "gloves", "umbrella", "scarf", "sunglasses",
    "phone", "camera", "watch", "headphones", "book", "notebook", "pen", "pencil", "marker",
    "magazine", "newspaper", "table", "chair", "sofa", "lamp", "painting", "plant", "statue",
    "bookcase", "refrigerator", "oven", "microwave", "vacuum", "washing machine", "dryer", 
    "dishwasher", "computer", "laptop", "mouse", "keyboard", "printer", "monitor", "headphones",
    "mousepad", "backpack", "wallet", "camera", "tent", "sleeping bag", "mountain", "beach",
    "desert", "forest", "river", "ocean", "island", "canyon", "volcano", "snowman", "penguin",
    "squirrel", "octopus", "whale", "caterpillar", "butterfly", "dragonfly", "zebra", "camel",
    "kangaroo", "koala", "sloth", "platypus", "beetle", "ant", "spider", "scorpion", "peacock",
    "tortoise", "wolverine", "raccoon", "falcon", "eagle", "penguin", "polar bear", "buffalo",
    "bison", "yak", "alpaca", "llama", "caribou", "narwhal", "octopus", "jellyfish", "turtle",
    "crocodile", "alligator", "shark", "flamingo", "orangutan", "chimpanzee", "baboon", "gorilla",
    "zebu", "armadillo", "skunk", "anteater", "gecko", "salmon", "trout", "catfish", "goldfish",
    "crab", "lobster", "mole", "platypus", "dragon", "phoenix", "pegasus", "mermaid", "fairy",
    "unicorn", "elf", "troll", "ogre", "goblin", "gnome", "griffin", "centaur", "chimera",
    "hydra", "golem", "sphinx", "kraken", "wyvern", "djinn", "genie", "cyclops", "minotaur",
    "yeti", "bigfoot", "basilisk", "kryptonite", "time machine", "spaceship", "ufo", "asteroid",
    "mars", "pluto", "jupiter", "saturn", "neptune", "venus", "earth", "mercury", "galaxy", 
    "nebula", "black hole", "wormhole", "tardis", "zombie", "ghost", "vampire", "werewolf", 
    "witch", "warlock", "mummy", "pirate", "treasure", "mermaid", "spell", "potion", "elixir",
    "herb", "alchemist", "wizardry", "alchemy", "spellbook", "crystal ball", "tarot", "oracle",
    "magic wand", "enchanted forest", "spellcaster", "cauldron", "grimoire", "coven", "spellcraft"
]

def display_word_in_center(player_number, secret_word):
    clear_terminal_screen()
    terminal_width = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines
    center_horizontal = terminal_width // 2
    center_vertical = terminal_height // 2
    box_width = len(secret_word) + 6
    horizontal_margin = (terminal_width - box_width) // 2
    vertical_margin = (terminal_height - 5) // 2

    clear_terminal_screen()

    print("\n" * vertical_margin)
    print(" " * horizontal_margin + "+" + "-" * (box_width - 2) + "+")
    print(" " * horizontal_margin + "|  " + secret_word.upper() + "  |")
    print(" " * horizontal_margin + "+" + "-" * (box_width - 2) + "+")
    
    time.sleep(5)
    
    clear_terminal_screen()
    print(f"Alright, Player {player_number}, the word is gone now.\n")

def clear_terminal_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_impostor_guess(actual_word, player_guess):
    if actual_word == player_guess:
        print("Correct! You are the impostor!")
        return True
    else:
        print("Wrong guess. Try again!")
        return False

def start_game():
    try:
        number_of_players = int(input("How many people are playing? "))
    except ValueError:
        print("Oops! Please provide a valid number.")
        return
    
    if number_of_players < 3:
        print("At least 3 players are needed! 2 words + 1 faker = fun!")
        return

    main_word = random.choice(word_bank)
    impostor_word = random.choice([word for word in word_bank if word != main_word])
    
    player_words = [main_word] * (number_of_players - 1) + [impostor_word]
    random.shuffle(player_words)

    print(f"\nGame is starting! Everyone is getting their word now.")

    for player_num in range(1, number_of_players + 1):
        word_for_player = player_words[player_num - 1]
        display_word_in_center(player_num, word_for_player)

        if player_num != number_of_players:  
            action = input(f"Player {player_num}, press Enter to pass the device or type 'exit' to quit: ")
            if action.lower() == 'exit':
                print("Thanks for playing, see you next time!")
                break
        else:
            player_guess = input("Enter the word you received to see if you're the impostor: ").strip()
            while not validate_impostor_guess(impostor_word, player_guess):
                player_guess = input("Incorrect. Try again, what was your word?: ").strip()

    print("That's the end of the round. Better luck next time!")

if __name__ == "__main__":
    start_game()
