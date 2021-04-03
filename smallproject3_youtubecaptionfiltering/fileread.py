# ---------------------reference---------------------
# https://stackoverflow.com/questions/2081836/how-to-read-specific-lines-from-a-file-by-line-number
# https://opentutorials.org/module/2980/17644

import sys
sys.stdout=open('smallproject3_youtubecaptionfiltering/Conan_English.txt', 'w', encoding='UTF8')
f = open('smallproject3_youtubecaptionfiltering\Conan Stars In North Korea’s First Late Night Talk Show (en).srt', 'r', encoding='UTF8')
# ----------print all-------------
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)

# for i, line in enumerate(f):
#     print(line)
    

lines = f.readlines()
numbers = [4*n+2 for n in range(200)]
for n in numbers:
    print(lines[n])

f.close()
