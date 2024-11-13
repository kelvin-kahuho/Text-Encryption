def monoalphabetic_cipher_encrypt(text, plain_alphabet, cipher_alphabet):
    # Create a dictionary for the substitution cipher
    cipher_dict = {plain_alphabet[i]: cipher_alphabet[i] for i in range(len(plain_alphabet))}
    
    encrypted_text = ""
    
    for char in text:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            encrypted_text += cipher_dict[char]
        # Check if the character is a lowercase letter
        elif 'a' <= char <= 'z':
            encrypted_text += cipher_dict[char.upper()].lower()
        # If it's not a letter, add it as is (spaces, punctuation, etc.)
        else:
            encrypted_text += char
    
    return encrypted_text

# Define the plain alphabet and the cipher alphabet
plain_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher_alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'

# Text to encrypt
text = """
Hapo zamani za kale alikuwepo mfanyabiashara ambaye aliheshimika kama mfalme wa mji. Alikuwa na wafanyakazi wa kila aina. Siku moja alipokuwa akijiandaa kwenda nchi za ng’ambo kwa ajili ya shughuli za biashara aliwaita watoto wake saba na kuwaambia; “wanangu mimi ninasafiri nakwenda katika shughuli za kibiashara, lakini ninachotaka kwenu ninyi ni kuwa na tabia nzuri ambayo haitawaudhi watu wengine, muwe na heshima na kupendana.” Hivyo kila mmoja alimpa kioo cha kujionea ambapo atakayekwenda kinyume na mambo aliyoyasema baba yao kioo chake kitafifia na hakitaonesha kitu.

Hapo mfanyabiashara yule alifunga safari na kuwaacha watoto wake pamoja na mama yao. Kawaida mfanyabiashara huyo anaposafiri huondoka na wafanyakazi wengine pamoja na makuhani yaani waganga wa kienyeji. Lakini wale watoto walisahau, na wakaanza kwenda kinyume na mambo waliyoambiwa na baba yao. Kulikuwepo na watoto sita watundu na hawasikii wanayokatazwa na wakubwa zao, isipokuwa mdogo wao wa mwisho tu ndiye ambaye alikuwa mtiifu na alisikiliza na kufuata yale waliyoambiwa na baba yao. Kadiri siku zilivyoenda wale watoto wengine walizidi kuwa wakorofi na hatimae vioo vyao vilianza kufifia na vikawa havitoi taswira yoyote isipokuwa kile kioo cha mtoto wa mwisho ambaye yeye alikuwa mtiifu.
"""

# Encrypt with Monoalphabetic Cipher
encrypted_text = monoalphabetic_cipher_encrypt(text, plain_alphabet, cipher_alphabet)
print(encrypted_text)
