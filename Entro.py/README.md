# Passphrase Generator and Entropy Calculator

## Overview
This Python script generates secure passphrases based on a customizable set of parameters, such as word count, separators, capitalization options, number inclusion, and 1337 (leet) substitutions. It also calculates the entropy of the generated passphrase to provide an estimate of its security.

## Features
- **Custom Wordlist**: The script allows you to load a wordlist from a text file to select random words for the passphrase. 
- **Capitalization Options**: You can choose to capitalize either the first letter of each word or apply random capitalization.
- **1337 Substitutions**: Optionally, you can replace certain characters in the passphrase with 1337 (leet) equivalents, with a customizable substitution probability.
- **Numeric Additions**: The script allows adding random numbers to each word for extra complexity.
- **Entropy Calculation**: After generating a passphrase, the script calculates its entropy to estimate its strength. It provides an entropy score, with 80 bits of entropy recommended for strong security.

## Usage Instructions

### 1. Setup
Ensure you have a wordlist file in plain text format (one word per line). An example wordlist has been provided from the [EFF wordlist](https://www.eff.org/dice) for testing.

### 2. Running the Script
1. Load your custom wordlist file by providing its file path.
2. Configure the passphrase by inputting the number of words, separator, capitalization options, 1337 substitutions, and whether to add numbers.
3. The script will generate a passphrase based on the input settings.
4. The entropy of the passphrase will be calculated and displayed.

### 3. Example Input and Output
```bash
Enter the number of words: 4
Enter a separator (default is underscore): -
Capitalize words? (first/random/none): first
Use 1337 substitutions? (y/n): y
Enter the probability of 1337 substitutions (0-1, default is 0.5): 0.5
Add numbers to each word? (y/n): n
Generated Passphrase: Tr0ub1e-Correct-H0rse-St@pl3
Entropy: 104.3 bits
Note: 80 bits of entropy is recommended for strong security.
```

### 4. Parameters Explained
- **Wordlist**: A file containing words, one per line.
- **Number of Words**: How many words will be included in the passphrase.
- **Separator**: The character that separates words (e.g., underscore, hyphen).
- **Capitalization**:
  - `first`: Capitalizes the first letter of each word.
  - `random`: Applies random capitalization to the words.
  - `none`: No capitalization changes.
- **1337 Substitutions**: If enabled, random characters are substituted using a predefined leet dictionary.
- **Add Numbers**: If enabled, random numbers are appended to each word. You can specify the number of digits.

### 5. Entropy Calculation
Entropy is calculated based on:
- Wordlist size and the number of words in the passphrase.
- The use of 1337 substitutions.
- Capitalization.
- Numeric additions.

### 6. Wordlist Format
Your wordlist file should be a plain text file where each word is on a new line, for example:
```
apple
banana
grape
orange
```

### 7. Modifying the Script
You can adjust various aspects of the script, such as:
- The `leet_dict` dictionary for custom 1337 substitutions.
- The entropy calculation method to suit your security requirements.

## Requirements
- Python 3.x
- A wordlist file in text format

## Example Script Usage
Place the script in a Python environment and execute it. Customize the input options to generate passphrases and calculate their entropy.

```bash
$ python passphrase_generator.py
```
## Author
Created by [donnie-works] (https://github.com/donnie-works)

## License
This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](./LICENSE) file for details.


## Acknowledgments
- Inspired by the EFF Diceware method for generating secure passphrases.
- Entropy reccomendation based on standard security recommendations.

---

