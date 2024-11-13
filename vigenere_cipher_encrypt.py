def vigenere_cipher_encrypt(text, key):
    encrypted_text = ""
    key_index = 0
    key = key.upper()
    
    for char in text:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        # Check if the character is a lowercase letter
        elif 'a' <= char <= 'z':
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        # If it's not a letter, add it as is (spaces, punctuation, etc.)
        else:
            encrypted_text += char
    
    return encrypted_text

# Key for the Vigenère Cipher
key = "KISWAHILI"

# Text to encrypt
text = """
Hapo zamani za kale alikuwepo mfanyabiashara ambaye aliheshimika kama mfalme wa mji. Alikuwa na wafanyakazi wa kila aina. Siku moja alipokuwa akijiandaa kwenda nchi za ng’ambo kwa ajili ya shughuli za biashara aliwaita watoto wake saba na kuwaambia; “wanangu mimi ninasafiri nakwenda katika shughuli za kibiashara, lakini ninachotaka kwenu ninyi ni kuwa na tabia nzuri ambayo haitawaudhi watu wengine, muwe na heshima na kupendana.” Hivyo kila mmoja alimpa kioo cha kujionea ambapo atakayekwenda kinyume na mambo aliyoyasema baba yao kioo chake kitafifia na hakitaonesha kitu.

Hapo mfanyabiashara yule alifunga safari na kuwaacha watoto wake pamoja na mama yao. Kawaida mfanyabiashara huyo anaposafiri huondoka na wafanyakazi wengine pamoja na makuhani yaani waganga wa kienyeji. Lakini wale watoto walisahau, na wakaanza kwenda kinyume na mambo waliyoambiwa na baba yao. Kulikuwepo na watoto sita watundu na hawasikii wanayokatazwa na wakubwa zao, isipokuwa mdogo wao wa mwisho tu ndiye ambaye alikuwa mtiifu na alisikiliza na kufuata yale waliyoambiwa na baba yao. Kadiri siku zilivyoenda wale watoto wengine walizidi kuwa wakorofi na hatimae vioo vyao vilianza kufifia na vikawa havitoi taswira yoyote isipokuwa kile kioo cha mtoto wa mwisho ambaye yeye alikuwa mtiifu.
"""

# Encrypt with Vigenère Cipher
encrypted_text = vigenere_cipher_encrypt(text, key)
print(encrypted_text)
