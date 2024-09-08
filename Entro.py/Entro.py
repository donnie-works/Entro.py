import secrets
import string

def calculate_entropy_from_passphrase(passphrase, wordlist, use_1337, num_words, capitalize_option, add_numbers, num_digits):
    # Initialize entropy
    entropy = 0
    
    # Calculate entropy from words
    wordlist_size = len(wordlist)
    word_entropy = num_words * (wordlist_size.bit_length())
    entropy += word_entropy
    
    # Calculate entropy from 1337 substitutions
    if use_1337:
        leet_substitution_count = sum(1 for char in passphrase if char in ''.join([val for sublist in leet_dict.values() for val in sublist]))
        entropy += leet_substitution_count * 2  # Estimate 2 bits of entropy per 1337 substitution
    
    # Calculate entropy from capitalization
    if capitalize_option == 'first':
        entropy += num_words  # 1 bit per word for first letter capitalization
    elif capitalize_option == 'random':
        capitalized_count = sum(1 for char in passphrase if char.isupper())
        entropy += capitalized_count  # 1 bit per capitalized character
    
    # Calculate entropy from numbers
    if add_numbers:
        number_count = sum(1 for char in passphrase if char.isdigit())
        entropy += number_count * 3.3  # 3.3 bits per digit
    
    return entropy

# More robust 1337 dictionary
leet_dict = {
    'a': ['4', '@'],
    'b': ['8'],
    'c': ['<'],
    'e': ['3'],
    'g': ['6', '9'],
    'h': ['#'],
    'i': ['1', '!'],
    'l': ['1', '|'],
    'o': ['0'],
    's': ['5', '$'],
    't': ['7', '+'],
    'z': ['2']
}

def leet_substitution(word, substitution_chance=0.5):
    """
    Applies 1337 substitution to a word based on a probability.

    :param word: The word to apply 1337 substitution to.
    :param substitution_chance: The probability (0-1) that a character will be substituted.
    :return: The word with random 1337 substitutions applied.
    """
    return ''.join([secrets.choice(leet_dict[char]) if char in leet_dict and secrets.randbelow(100) < (substitution_chance * 100) else char for char in word])

def random_capitalize(word):
    return ''.join([char.upper() if secrets.choice([True, False]) else char for char in word])

def generate_passphrase(wordlist, num_words=4, separator='_', capitalize_option='none', add_numbers=False, num_digits=0, use_1337=False, substitution_chance=0.5):
    """
    Generate a passphrase with user input.

    wordlist: List of words from provided or custom wordlist.
    num_words: Number of words to include in the passphrase. Default is 4.
    separator: The character(s) used to separate the words in the passphrase. Default is an underscore.
    capitalize_option: 'first' for capitalizing the first letter of each word, 'random' for random capitalization.
    add_numbers: If True, add random numbers to each word in the passphrase.
    num_digits: Number of digits to add to each word.
    use_1337: If True, apply 1337 substitutions to the words.
    substitution_chance: The probability that a character will be substituted with 1337 (default is 0.5).
    :return: A string containing the generated passphrase.
    """
    selected_words = [secrets.choice(wordlist) for _ in range(num_words)]
    
    if use_1337:
        selected_words = [leet_substitution(word, substitution_chance) for word in selected_words]
    
    if capitalize_option == 'first':
        selected_words = [word.capitalize() for word in selected_words]
    elif capitalize_option == 'random':
        selected_words = [random_capitalize(word) for word in selected_words]
    
    if add_numbers and num_digits > 0:
        selected_words = [word + str(secrets.randbelow(10**num_digits - 10**(num_digits-1)) + 10**(num_digits-1)) for word in selected_words]
    
    passphrase = separator.join(selected_words)
    
    return passphrase

def load_wordlist(filepath):
    """
    Load a wordlist from a text file of your choice.

    filepath: Local path to your saved word list. 
    """
    with open(filepath, 'r') as file:
        wordlist = file.read().splitlines()
    return wordlist

# Example usage
if __name__ == "__main__":
    wordlist_path = r"Path\To\Your\Wordlist.txt"  # Replace with your local path to either the provided wordlist or a custom wordlist
    wordlist = load_wordlist(wordlist_path)

    # Gather user input in the desired order
    num_words = int(input("Enter the number of words: "))
    separator = input("Enter a separator (default is underscore): ") or '_'
    capitalize_option = input("Capitalize words? (first/random/none): ").lower()
    use_1337 = input("Use 1337 substitutions? (y/n): ").lower() == 'y'
    substitution_chance = 0.5
    if use_1337:
        substitution_chance = float(input("Enter the probability of 1337 substitutions (0-1, default is 0.5): ") or 0.5)
    add_numbers = input("Add numbers to each word? (y/n): ").lower() == 'y'
    num_digits = 0
    if add_numbers:
        num_digits = int(input("How many digits to add to each word?: "))
    
    # Generate the passphrase
    passphrase = generate_passphrase(wordlist, num_words, separator, capitalize_option, add_numbers, num_digits, use_1337, substitution_chance)
    
    # Calculate the entropy of the generated passphrase
    entropy = calculate_entropy_from_passphrase(passphrase, wordlist, use_1337, num_words, capitalize_option, add_numbers, num_digits)
    
    # Output the passphrase and its entropy
    print(f"Generated Passphrase: {passphrase}")
    print(f"Entropy: {entropy:.1f} bits")
    print("Note: 80 bits of entropy is recommended for strong security.")
