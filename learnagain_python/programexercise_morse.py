# input : morse code
# output : decode
# function : append, join
dic ={
    '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F',
    '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L',
    '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R',
    '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X',
    '-.--':'Y', '--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    # return result
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

# result = ['H', 'E', ' ', 'S', 'L', 'E', 'E', 'P', 'S', ' ', 'E', 'A', 'R', 'L', 'Y', ' ']
# print("-".join(result))