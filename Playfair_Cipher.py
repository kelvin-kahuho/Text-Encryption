def prepare_text(text):
    # Replace 'J' with 'I' for Playfair cipher and ensure text is in uppercase for matrix creation
    text = text.upper().replace("J", "I")  # Replace 'J' with 'I'
    prepared_text = []
    i = 0
    
    while i < len(text):
        if text[i].isalpha():  # Process alphabetic characters
            # If two consecutive letters are the same, insert 'X'
            if i + 1 < len(text) and text[i] == text[i + 1]:
                prepared_text.append(text[i] + 'X')  # Insert 'X' if same character repeats
                i += 1
            else:
                prepared_text.append(text[i] + (text[i + 1] if i + 1 < len(text) else 'X'))  # Add 'X' if odd length
                i += 2
        else:  # Directly add non-alphabetic characters (spaces, punctuation) to the prepared_text
            prepared_text.append(text[i])
            i += 1
    
    return prepared_text

def create_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates, keep order
    key = key.upper().replace("J", "I")  # Replace J with I
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Playfair uses 25 letters (I/J = same letter)
    
    matrix = []
    used_letters = set()
    
    for char in key:
        if char not in used_letters:
            matrix.append(char)
            used_letters.add(char)
    
    for char in alphabet:
        if char not in used_letters:
            matrix.append(char)
            used_letters.add(char)
    
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char.upper():  # Handle both uppercase and lowercase
                return row, col
    return None

def playfair_encrypt(text, key):
    matrix = create_playfair_matrix(key)
    prepared_text = prepare_text(text)
    encrypted_text = []
    
    for digraph in prepared_text:
        if len(digraph) == 2 and digraph[0].isalpha() and digraph[1].isalpha():  # Only encrypt digraphs of letters
            first_char, second_char = digraph
            position1 = find_position(matrix, first_char)
            position2 = find_position(matrix, second_char)
            
            if not position1 or not position2:
                print(f"Error: Character(s) '{first_char}' or '{second_char}' not found in the matrix.")
                return None
            
            row1, col1 = position1
            row2, col2 = position2
            
            # Encrypt by Playfair cipher rules
            if row1 == row2:  # Same row: shift right
                encrypted_text.append(matrix[row1][(col1 + 1) % 5])
                encrypted_text.append(matrix[row2][(col2 + 1) % 5])
            elif col1 == col2:  # Same column: shift down
                encrypted_text.append(matrix[(row1 + 1) % 5][col1])
                encrypted_text.append(matrix[(row2 + 1) % 5][col2])
            else:  # Rectangle case: swap corners
                encrypted_text.append(matrix[row1][col2])
                encrypted_text.append(matrix[row2][col1])
        else:
            # Directly append non-alphabetic characters (spaces, punctuation) to the result
            encrypted_text.append(digraph)
    
    # Preserve the letter case in the result
    return ''.join([ch.upper() if ch.isupper() else ch.lower() for ch in encrypted_text])

# Key for Playfair Cipher
key = "KISWAHILI"

# Text to encrypt
text = """
Hapo zamani za kale alikuwepo mfanyabiashara ambaye aliheshimika kama mfalme wa mji. Alikuwa na wafanyakazi wa kila aina. Siku moja alipokuwa akijiandaa kwenda nchi za ng’ambo kwa ajili ya shughuli za biashara aliwaita watoto wake saba na kuwaambia; “wanangu mimi ninasafiri nakwenda katika shughuli za kibiashara, lakini ninachotaka kwenu ninyi ni kuwa na tabia nzuri ambayo haitawaudhi watu wengine, muwe na heshima na kupendana.” Hivyo kila mmoja alimpa kioo cha kujionea ambapo atakayekwenda kinyume na mambo aliyoyasema baba yao kioo chake kitafifia na hakitaonesha kitu.

Hapo mfanyabiashara yule alifunga safari na kuwaacha watoto wake pamoja na mama yao. Kawaida mfanyabiashara huyo anaposafiri huondoka na wafanyakazi wengine pamoja na makuhani yaani waganga wa kienyeji. Lakini wale watoto walisahau, na wakaanza kwenda kinyume na mambo waliyoambiwa na baba yao. Kulikuwepo na watoto sita watundu na hawasikii wanayokatazwa na wakubwa zao, isipokuwa mdogo wao wa mwisho tu ndiye ambaye alikuwa mtiifu na alisikiliza na kufuata yale waliyoambiwa na baba yao. Kadiri siku zilivyoenda wale watoto wengine walizidi kuwa wakorofi na hatimae vioo vyao vilianza kufifia na vikawa havitoi taswira yoyote isipokuwa kile kioo cha mtoto wa mwisho ambaye yeye alikuwa mtiifu.
"""

# Encrypt with Playfair Cipher
encrypted_text = playfair_encrypt(text, key)

# Check if encryption was successful
if encrypted_text:
    print(encrypted_text)
