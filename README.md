This project encrypts a Kiswahili text paragraph using multiple substitution ciphers: Caesar, Atbash, Monoalphabetic, Vigenère, Playfair, and Affine. Each encryption method uses a unique key or grid, with ciphertext provided for each type.

## Project Overview

This project demonstrates the application of classical substitution ciphers on a Kiswahili paragraph. The objective is to show how each cipher transforms the original plaintext into ciphertext using various encryption methodologies. 

## Ciphers Used

1. **Caesar Cipher**
   - **Key**: Shift of 3
   - **Methodology**: Each letter in the plaintext is shifted 3 positions forward in the alphabet.
   - **Example Output**: `Kdso cdpcql cd ndoh dlntzzhtrp phdoydmrhk dlphxvokl phdoyhvkdq...`

2. **Atbash Cipher**
   - **Methodology**: The alphabet is reversed, mapping "A" to "Z," "B" to "Y," etc.
   - **Example Output**: `Szkl znznmr az pzov zoroqvc gkzobznzrh zntszmrxv gztzolrzn...`

3. **Monoalphabetic Cipher**
   - **Key**: Custom substitution alphabet
     - Plain Alphabet: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
     - Substitution Alphabet: `QWERTYUIOPASDFGHJKLZXCVBNM`
   - **Methodology**: Each letter in the plaintext is replaced by the corresponding letter in the substitution alphabet.
   - **Example Output**: `Qdvl qlwzui ql tqvr qmokztijzp wlkvxqljvq zkczgfpc jcklzpqo...`

4. **Vigenère Cipher**
   - **Key**: "KISWAHILI"
   - **Methodology**: Each letter in the plaintext is shifted based on the position of the corresponding letter in the repeating key.
   - **Example Output**: `Lkqj yrksnk yi njwn axkcfw yhjlvcno yfznlrqp niuqzfj jnrfw...`

5. **Playfair Cipher**
   - **Grid**: 
      - Keyword: "KISWAHILI" arranged in a 5x5 grid, omitting repeated letters and merging "I" and "J" as one letter.
      - Example Grid:

      | K | I | S | W | A |
      |---|---|---|---|---|
      | H | L | B | C | D |
      | E | F | G | M | N |
      | O | P | Q | R | T |
      | U | V | X | Y | Z |

   - **Methodology**: Each pair of letters is encrypted according to the Playfair cipher rules.
   - **Example Output**: `Iykw plfbad pl dcjd zlibxuv ofxayzknjz oyce plev rds...`

6. **Affine Cipher**
   - **Key**: (5, 8)
   - **Methodology**: Each letter is transformed using the formula:  
     \[
     E(x) = (5x + 8) \mod 26
     \]
   - **Example Output**: `Lpkr qzwudl qk akub amkrwgx afuyplzgnm aqpl krzi aqobaz...`

## Usage

To encrypt text using each cipher:
1. Place the Kiswahili plaintext paragraph in a variable.
2. Apply each cipher method using the specified key or methodology.
3. Output the resulting ciphertext for each cipher.

## Project Structure

```
├── README.md                # Project documentation
├── encryption_methods.py    # Python script containing cipher implementations
└── examples                 # Folder with examples of each ciphertext
```

## Requirements

- Python 3.x
- Basic understanding of cryptography principles
- Text editor (e.g., VSCode, Sublime Text) for viewing/editing scripts

## Contributing

Contributions to improve or expand this project are welcome. Please fork the repository, make changes, and submit a pull request for review.

## License

This project is licensed under the MIT License.

--- 

This `README.md` covers the project’s purpose, instructions, and details on each cipher, allowing others to understand and potentially extend the project. Let me know if there are specific elements you'd like to add or modify!