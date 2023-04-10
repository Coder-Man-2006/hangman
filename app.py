import pycountry
import random

#Some lists for data
countries = pycountry.countries
country_names = [country.name for country in countries]

animals = ["lion", "tiger", "bear", "elephant", "giraffe", "hippopotamus", "rhinoceros", "zebra", "kangaroo", "koala", "panda", "monkey", "gorilla", "chimpanzee", "orangutan", "sloth", "anteater", "armadillo", "otter", "beaver", "whale", "dolphin", "shark", "octopus", "jellyfish", "seahorse", "starfish", "lobster", "crab", "turtle", "crocodile", "alligator", "snake", "lizard", "frog", "toad", "turtle", "penguin", "ostrich", "flamingo", "peacock", "parrot", "owl", "eagle", "hawk", "seagull", "duck", "goose", "chicken", "cow", "sheep", "pig"]

sports = ["Football", "Basketball", "Baseball", "Soccer", "Tennis", "Golf", "Hockey", "Volleyball", "Rugby", "Cricket", "Boxing", "MMA", "Wrestling", "Table Tennis", "Badminton", "Swimming", "Track and Field", "Cycling", "Gymnastics", "Weightlifting", "Fencing", "Judo", "Taekwondo", "Karate", "Surfing", "Skateboarding", "Snowboarding", "Skiing", "Bobsleigh", "Skeleton", "Luge", "Rowing", "Canoeing", "Kayaking", "Sailing", "Equestrian"]

famous_people = ["Albert Einstein", "Nelson Mandela", "Steve Jobs", "Oprah Winfrey", "Walt Disney", "Marie Curie", "Mahatma Gandhi", "Leonardo da Vinci", "Martin Luther King Jr.", "Mother Teresa", "Elon Musk", "Neil Armstrong", "Michael Jordan", "Muhammad Ali", "Serena Williams", "Usain Bolt", "Babe Ruth", "David Bowie", "Elvis Presley", "Madonna", "Taylor Swift", "Beyoncé", "Kanye West", "Oscar Wilde", "William Shakespeare", "Virginia Woolf", "Ernest Hemingway", "Maya Angelou", "Stephen Hawking", "Charles Darwin", "Isaac Newton", "Galileo Galilei", "Pablo Picasso", "Vincent van Gogh", "Leonardo DiCaprio"]

# Define Function
def play_game():
  mode = """
  
  Options: 
  1) Countries
  2) Animals
  3) Sports
  4) Celebrities
  
  >>> """

  letter = "Enter a Letter >>> "

  is_running = True

  m = input(mode)

  # Change m in conditional to mode (change back)
  if m == '1':
    print('Countries Mode Selected!')

    word = random.choice(country_names)
    word = str(word)
    
    incorrect_guesses = 0
    progress = '_' * len(word)


  elif m == '2':
    print('Animals Mode Selected!')
    
    word = str(random.choice(animals))
    incorrect_guesses = 0
    progress = '_' * len(word)
    
  elif m == '3':
    print('Sports Mode Selected!')

    word = str(random.choice(sports))
    incorrect_guesses = 0
    progress = '_' * len(word)
    
  elif m == '4':
    print('Celebrities Mode Selected!')

    word = str(random.choice(famous_people))
    incorrect_guesses = 0
    progress = '_' * len(word)
    
  else:
    print("\nInvalid Input.")
    m = input(mode)

  # Keep playing until the player wins or loses
  while is_running == True:
    # Print the current state of the game
    print("\nWord:", progress)                              # ERROR
    print("Incorrect guesses:", incorrect_guesses)  

    guess = input(letter)

    # Check if the guess is correct
    if guess.lower() in word or guess.upper() in word:
        print("\nCorrect!")
        lst_word = []

        # Update the progress
        for i in word:
            if i.lower() == guess.lower():
                lst_word.append(i)
            else:
                lst_word.append(progress[word.index(i)])
        progress = "".join(lst_word)
        print(progress)
    else:
        print("\nIncorrect!")
        incorrect_guesses += 1
        print("Incorrect guesses:", incorrect_guesses)

    # Check if the player has lost
    if incorrect_guesses == 6:
        print("\nYou lose! The word was", word)
        
        play_again = input("Would you Like to play again? ")
    
        if play_again.upper == 'Y':
            play_game()
        elif play_again.lower == 'n':
            is_running = False
            break
        else:
            is_running = False
            break

    # Check if the player has won
    if "_" not in progress:
        print("\nYou win! The word was", word)
        
        
        play_again = input("Would you Like to play again (Y/n)")
    
        if play_again.upper == 'Y':
            play_game()
        elif play_again.lower == 'n':
            is_running = False
        else:
            is_running = False
        
play_game()