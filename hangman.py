import random

stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

word_list = ["above", "abroad", "access", "accomplish", "achieve", "achievement", "acknowledgement", "add",
             "additional", "adjust", "admiring", "after", "air", "alluring", "alone", "and", "another", "animal",
             "answer", "around", "art", "ask", "attach", "at", "attain", "auspicious", "away", "avoid", "baby", "back",
             "balance", "banana", "bark", "basket", "beach", "beat", "beautiful", "because", "bed", "before", "belated",
             "believe", "belong", "below", "benefit", "best", "better", "bill", "billion", "birth", "blood", "bloom",
             "body", "book", "bore", "both", "bottle", "boy", "branches", "breed", "brother", "bucket", "building",
             "built", "but", "buy", "cap", "capital", "captain", "captivate", "capture", "car", "cardiac", "careless",
             "carnival", "carry", "cash", "casual", "catastrophe", "catch", "categories", "ceremony", "certain",
             "challenge", "chart", "chief", "child", "children", "church", "circle", "city", "clap", "class", "clouds",
             "coat", "cold", "colour", "column", "come", "commit", "communicate", "complete", "concentrate", "conclude",
             "concrete", "confuse", "congested", "congratulate", "cook", "cordial", "country", "cover", "cow", "craft",
             "cravings", "create", "crop", "crowd", "crush", "cry", "cunning", "cup", "current", "cut", "challenge",
             "chart", "chief", "child", "children", "church", "circle", "city", "clap", "class", "clouds", "coat",
             "cold", "colour", "column", "come", "commit", "communicate", "complete", "concentrate", "conclude",
             "concrete", "confuse", "congested", "congratulate", "cook", "cordial", "country", "cover", "cow", "craft",
             "cravings", "create", "crop", "crowd", "crush", "cry", "cunning", "cup", "current", "cut", "dance", "dark",
             "day", "death", "decide", "deep", "defeat", "detail", "determined", "different", "disappear", "divide",
             "draw", "dream", "dry", "during", "each", "east", "eat", "effect", "encounter", "energy", "entertainment",
             "evening", "ever", "every", "everyone", "everything", "except", "expect", "experience", "fabulous", "face",
             "fact", "fake", "family", "fan", "fantastic", "far", "farm", "farmers", "fast", "fasten", "father", "feel",
             "feet", "fever", "figure", "fill", "film", "fine", "finish", "fire", "first", "fish", "flowers", "fly",
             "follow", "food", "force", "forgive", "formal", "forward", "free", "freedom", "frequent", "fresh",
             "friendly", "friends", "from", "fruits", "fun", "funny", "gain", "game", "gas", "genuine", "girl", "glory",
             "go", "good", "government", "great", "greet", "ground", "group", "growth", "guess", "guest", "hang",
             "happy", "harsh", "have", "he", "head", "health", "her", "him", "hot", "how", "however", "hurry", "idea",
             "ignore", "illuminate", "import", "important", "impossible", "incident", "industry", "inferior",
             "infrastructure", "inside", "insight", "instant", "interest", "interior", "interval", "intimidating",
             "island", "kick", "kid", "kitchen", "land", "language", "large", "last", "laugh", "launch", "lavish",
             "leader", "lean", "learn", "leave", "leaves", "led", "left", "level", "life", "light", "line", "listen",
             "little", "locate", "loss", "loud", "love", "low", "luck", "machines", "made", "magnificent", "main",
             "map", "march", "marine", "mark", "marry", "masculine", "master", "match", "materials", "matter",
             "measure", "medicine", "meet", "might", "mine", "money", "moon", "morning", "mother", "movies", "murmur",
             "name", "near", "need", "never", "night", "no", "noon", "north", "not", "nothing", "object", "office",
             "office", "official", "often", "old", "oxygen", "paint", "pair", "pamper", "paragraph", "park", "patty",
             "peace", "pen", "penetrate", "people", "perhaps", "permit", "person", "phrase", "piece", "pillow", "place",
             "plant", "plural", "poem", "polite", "pollute", "poor", "possible", "power", "prefix", "present",
             "probably", "problem", "produce", "profit", "protection", "punch", "push", "pull", "rack", "raft", "rain",
             "range", "rat", "ray", "reach", "realise", "reflection", "regain", "reflection", "rhythm", "river", "rose",
             "row", "rule", "run", "sad", "safe", "sail", "sand", "saw", "say", "scare", "school", "scientist",
             "screen", "sea", "seat", "secure", "security", "sentence", "set", "settle", "shade", "shadow", "shape",
             "share", "sharp", "she", "shine", "ship", "show", "sight", "silent", "similar", "single", "sister", "sit",
             "size", "skill", "sky", "sleep", "slow", "small", "smile", "smooth", "soap", "soil", "solid", "something",
             "song", "soon", "sound", "south", "space", "special", "speed", "sports", "spot", "stars", "steal", "steel",
             "story", "street", "strong", "sudden", "suffix", "sun", "sunlight", "super", "supply", "sure", "surrender",
             "swim", "table", "tackle", "talent", "talk", "task", "teach", "team", "teenage", "television", "tell",
             "tendency", "tender", "them", "they", "thick", "through", "time", "today", "together", "tomorrow", "too",
             "tools", "track", "transport", "treat", "tree", "up", "us", "usually", "value", "vanish", "various",
             "vegetables", "vehicle", "victory", "voice", "walk", "wander", "wanted", "warm", "watch", "water", "waves",
             "way", "we", "west", "wet", "wheels", "when", "where", "white", "who", "whoever", "will", "win", "wings",
             "winner", "wish", "with", "wonder", "wood", "word", "work", "worst", "worst", "yawn", "yes", "yesterday",
             "you", "aardvark", "baboon", "camel"]

logo = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    '''

print(logo)

#choosing the position of the word in the list
chosen_word = random.choice(word_list)

#applying dashes in the duplicate word
duplicate_word = '-' * len(chosen_word)

#print(chosen_word)
print(f"\nThe word need to be guess has {len(chosen_word)} letters\n" + duplicate_word)

word_length_count = len(chosen_word)
hangman_count = len(stages)

check_letters = ['']


#to check whether the letter is already guessed by the user
def already_list():
    return guessed_letter in check_letters


#fill the letters removing the dashed lines
def fill_letter():
    global duplicate_word
    new_string = ''
    word_length = len(chosen_word)
    no_of_correct_char = 0  #number of dashes filled with the correct letters
    for i in range(word_length):
        if already_list():
            no_of_correct_char = 100
        elif chosen_word[i] == guessed_letter:
            new_string += guessed_letter
            no_of_correct_char += 1
        else:
            new_string += duplicate_word[i]

    if not already_list():
        check_letters.append(guessed_letter)

    duplicate_word = new_string
    return no_of_correct_char


while hangman_count > 0 and word_length_count > 0:
    guessed_letter = input("\nEnter a letter: ").lower()
    n = fill_letter()
    if n == 100:
        print(f"Letter \'{guessed_letter}\' already tried. Try another letter to find the correct word.")
    elif n > 0:
        word_length_count -= n
    else:
        hangman_count -= 1
        print(f"Guessed the wrong letter. \nHangman Count: {7 - hangman_count}/7")
        print(stages[hangman_count])
    print(duplicate_word)

if (word_length_count == 0):
    print(f"\nCongratulations! You guessed the word right. The word is {chosen_word}.")
else:
    print(f"\nOut of Attempts! The correct word is {chosen_word}.")
