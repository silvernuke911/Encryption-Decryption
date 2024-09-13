
alphabetlist_small="abcdefghijklmnopqrstuvwxyz"
alphabetlist_caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ .,-?!:;1234567890"
#alphabetlist_caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def vigenere_alphabet_func(vigenere_key):
    caps_vigenere_key=vigenere_key.upper()
    for letter in alphabetlist_caps:
        if caps_vigenere_key.count(letter)>1:
            return "Invalid Keyword, keyword must have letters appear only once"
    output_alphabet=caps_vigenere_key
    for letter in alphabetlist_caps:
        if letter not in caps_vigenere_key:
            output_alphabet=output_alphabet+letter
    return output_alphabet
    
def string_to_list_converter(string):
    outputlist=[]
    for char in string:
        outputlist.append(char)
    return outputlist

def list_to_string_converter(list_sample):
    output=""
    for item in list_sample:
        output+=str(item)
    return output

def vigenere_table_func(vigenere_alphabet_keyed):
    local_key=tuple(string_to_list_converter(vigenere_alphabet_keyed))
    def shifter(letter_list,shiftnumber):
        output=list(letter_list)
        first_chars=output[0:shiftnumber]
        for letter in first_chars:
            output.remove(letter)
            output.append(letter)
        return output
    outputlist=[]
    for i in range(len(local_key)):
        a=shifter(local_key,i)
        outputlist.append(a)
    return outputlist

def viginere_printer(vigenere_key,mode=1):
    vigenere_alph=vigenere_alphabet_func(vigenere_key)
    vigenere_table=vigenere_table_func(vigenere_alph)
    if mode==1:
        for i in range(len(vigenere_table)):
            a=list_to_string_converter(vigenere_table[i])
            print(a)
    if mode==2:
        for i in range(len(vigenere_table)):
            a=vigenere_table[i]
            print(a)

def keyword_matcher(message,keyword):
    keyword_upper=keyword.upper()
    message_upper=message.upper()
    n=len(keyword)
    m=len(message)
    q=m//n+1
    keystream=keyword_upper*q
    output=keystream[0:m]
    return [message_upper,output]

# vigenere_key="JEHOVA"
# keyword="GODISGOOD"
# message="For God so loved the world that he gave his only Son that whoever believes in him should not perish but have eternal life"
# cypher="SBJOOLIIELBUMXIIIHKVFCWHPIPVALALKVVRNCFKUUWWIZPBFKLRRHKDHANKBVKIUJQTXMVKIWEWDZAMWYWGMMXIIXLXHETHMWGKFOALKDCFIVHKIZDPUXMQK"
# vigenere_key="kryptos"
# keyword="kryptos"
# message="secretmessage"
# cypher="SFETICXEABDLJ"

# message="hello there, here is my truce to everyone in this motherfucking town, where all is and all isnt, I hope ya'll listen to me. We train tonight!. Tonight is the night of reckoning, and in plaintext we will know, and in plain text we will decypher, the thoughts and pleasures of the universe within us, of emtpy seas and dry land, of burning volcanoes and crazy riches, for tonight, we dine in hell. We were born to inherit the stars. Long live the fighters, Lisan al Gaib!"
# keyword="mahdi, ruler of arrakis."
# vigenere_key='mahdi'
# cypher=''


# message='INAPLACEFULLOFSORROWSWELAUGHBECAUSEITISTHEONLYTHINGWECANDOXSLOWLYDESPERATELYSLOWLYIMLOSINGMYDRIVETOGOONXISTHISEVENWORTHCONTINUINGXNADIASANTSUGIKAKIREIDESUNE'
# keyword='aomenjushage'
# vigenere_key='navi'

# message="Lisan al-gaib! long live the fighters! We were born to inherit the stars. Go to the coordinates, 102.4, 064.3, 123.5, and we shall go to war. Fret not, for the mahdi will be with us, and we shall not grow old. SPill the water of the infidels! The great houses shall know, the holy war has begun! Where is your faith!? Where is the land that brought you here!TO THE STARS, TO THE GREAT HOUSES, BRING THEIR WAR TO THEM. WE SHALL NOT GROW OLD, AND THEY SHALL NOT KNOW, THAT WE ARE THE ONES BORN TO INHERIT THE STARS. AND IN PLAIN TEXT WE WILL KNOW, AND IN PLAIN TEXT WE WILL DECIPHER, THAT WE ARE THE CHILDREN OF THE UNIVERSE FORGOTTEN"
# keyword="mahdi"
# vigenere_key='mahdi'

# message='IKNOWWHOYOUAREWHOEXPOSEDMYSAFESPACEIKNOWWHEREYOUAREYOUWILLPAYXFERNWHYDIDIHAVETOLEARNFROMSOMEONEELSEXWHYTHEFUCKWOULDYOUEXPOSEMEYOULITTLEFUCKX'
# keyword='iknowwhoyouare'
# vigenere_key=''

message='EGOCREDIDITEETTUMETRADISXMORSVINCITOMNIA'
message='ALL THE WORLDS A GAME, AND ALL THE WORLD IS DEATH, AND THE ALPHABET IS NOTHING BUT NILL AND NILL AND NILL'
keyword='09112003'
vigenere_key=''

def encryptor_func(message,keyword,vigenere_key):
    key_list=keyword_matcher(message,keyword)
    keyed_alphabet=vigenere_alphabet_func(vigenere_key)
    vigenere_table=vigenere_table_func(keyed_alphabet)
    message_string=key_list[0]
    keyword_string=key_list[1]
    message_list=string_to_list_converter(message_string)
    keyword_list=string_to_list_converter(keyword_string)
    print(message_string)
    print('')
    print(keyword_string)
    print('')
    output=""
    for i in range(len(message_list)):
        for j in range(len(keyed_alphabet)):
            if message_list[i]==keyed_alphabet[j]:
                a=j
            if keyword_list[i]==keyed_alphabet[j]:
                b=j
        #print(a,b,vigenere_table[a][b])
        output+=vigenere_table[a][b]
    return output
    
def decryptor_func(message,keyword,vigenere_key):
    key_list=keyword_matcher(message,keyword)
    keyed_alphabet=vigenere_alphabet_func(vigenere_key)
    vigenere_table=vigenere_table_func(keyed_alphabet)
    message_string=key_list[0]
    keyword_string=key_list[1]
    message_list=string_to_list_converter(message_string)
    keyword_list=string_to_list_converter(keyword_string)
    print(message_string)
    print('')
    # print(keyword_string)
    # print(keyed_alphabet)
    output=""
    for i in range(len(keyword_list)):
        for j in range(len(keyed_alphabet)):
            if keyword_list[i]==keyed_alphabet[j]:
                a=j
        for k in range(len(vigenere_table)):
            if vigenere_table[k][a]==message_list[i]:
                b=k
        output+=vigenere_table[0][b]
    return output


# keyword_matcher(message,keyword)
cypher=encryptor_func(message,keyword,vigenere_key)
print(cypher)
print("")
print(decryptor_func(cypher,keyword,vigenere_key))
print("")
viginere_printer(vigenere_key,1)


print(decryptor_func('QUACSSOCWCOAIIERBSTLVGCRGYJENOFDWYLWIBIWNLMBRMKQHFCMIUNMTVCOUTMSPBQHPHQNVVWRLHMZYAIRNBBAOKTSMBYECWMHJVUPOSDIWKNSCVQMKQLLNCMEDIGYHZEPAZCTOCBB','IKNOWWHOYOUARE',''))

