# Function to calculate modular inverse of a number 'a' under modulo 'm'
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Affine Cipher Encryption Function
def affine_encrypt(text, a, b):
    m = 26  # Length of the alphabet
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            # Convert the letter to a number (A = 0, B = 1, ..., Z = 25)
            char_num = ord(char.upper()) - ord('A')
            # Apply the encryption formula
            encrypted_char_num = (a * char_num + b) % m
            # Convert the encrypted number back to a character
            encrypted_char = chr(encrypted_char_num + ord('A'))
            # Keep the letter case intact
            if char.islower():
                encrypted_text += encrypted_char.lower()
            else:
                encrypted_text += encrypted_char
        else:
            # Directly append non-alphabetic characters
            encrypted_text += char
    
    return encrypted_text

# Key for Affine Cipher (a and b)
a = 5
b = 8

# Text to encrypt
text = """
Hapo zamani za kale alikuwepo mfanyabiashara ambaye aliheshimika kama mfalme wa mji. Alikuwa na wafanyakazi wa kila aina. Siku moja alipokuwa akijiandaa kwenda nchi za ng’ambo kwa ajili ya shughuli za biashara aliwaita watoto wake saba na kuwaambia; “wanangu mimi ninasafiri nakwenda katika shughuli za kibiashara, lakini ninachotaka kwenu ninyi ni kuwa na tabia nzuri ambayo haitawaudhi watu wengine, muwe na heshima na kupendana.” Hivyo kila mmoja alimpa kioo cha kujionea ambapo atakayekwenda kinyume na mambo aliyoyasema baba yao kioo chake kitafifia na hakitaonesha kitu.

Hapo mfanyabiashara yule alifunga safari na kuwaacha watoto wake pamoja na mama yao. Kawaida mfanyabiashara huyo anaposafiri huondoka na wafanyakazi wengine pamoja na makuhani yaani waganga wa kienyeji. Lakini wale watoto walisahau, na wakaanza kwenda kinyume na mambo waliyoambiwa na baba yao. Kulikuwepo na watoto sita watundu na hawasikii wanayokatazwa na wakubwa zao, isipokuwa mdogo wao wa mwisho tu ndiye ambaye alikuwa mtiifu na alisikiliza na kufuata yale waliyoambiwa na baba yao. Kadiri siku zilivyoenda wale watoto wengine walizidi kuwa wakorofi na hatimae vioo vyao vilianza kufifia na vikawa havitoi taswira yoyote isipokuwa kile kioo cha mtoto wa mwisho ambaye yeye alikuwa mtiifu.
"""

# Encrypt the text using Affine Cipher
encrypted_text = affine_encrypt(text, a, b)

# Print the encrypted text
print(f"Encrypted Text: {encrypted_text}")
