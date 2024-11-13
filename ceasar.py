def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Check if it's an uppercase letter
        if 'A' <= char <= 'Z':
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Check if it's a lowercase letter
        elif 'a' <= char <= 'z':
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        # If it's not a letter, add it as is
        else:
            encrypted_text += char
    
    return encrypted_text

# Text to encrypt
text = """
Hapo zamani za kale alikuwepo mfanyabiashara ambaye aliheshimika kama mfalme wa mji. Alikuwa na wafanyakazi wa kila aina. Siku moja alipokuwa akijiandaa kwenda nchi za ng’ambo kwa ajili ya shughuli za biashara aliwaita watoto wake saba na kuwaambia; “wanangu mimi ninasafiri nakwenda katika shughuli za kibiashara, lakini ninachotaka kwenu ninyi ni kuwa na tabia nzuri ambayo haitawaudhi watu wengine, muwe na heshima na kupendana.” Hivyo kila mmoja alimpa kioo cha kujionea ambapo atakayekwenda kinyume na mambo aliyoyasema baba yao kioo chake kitafifia na hakitaonesha kitu.

Hapo mfanyabiashara yule alifunga safari na kuwaacha watoto wake pamoja na mama yao. Kawaida mfanyabiashara huyo anaposafiri huondoka na wafanyakazi wengine pamoja na makuhani yaani waganga wa kienyeji. Lakini wale watoto walisahau, na wakaanza kwenda kinyume na mambo waliyoambiwa na baba yao. Kulikuwepo na watoto sita watundu na hawasikii wanayokatazwa na wakubwa zao, isipokuwa mdogo wao wa mwisho tu ndiye ambaye alikuwa mtiifu na alisikiliza na kufuata yale waliyoambiwa na baba yao. Kadiri siku zilivyoenda wale watoto wengine walizidi kuwa wakorofi na hatimae vioo vyao vilianza kufifia na vikawa havitoi taswira yoyote isipokuwa kile kioo cha mtoto wa mwisho ambaye yeye alikuwa mtiifu.
"""

# Encrypt with Caesar Cipher (shift = 3)
shift = 3
encrypted_text = caesar_cipher_encrypt(text, shift)
print(encrypted_text)
