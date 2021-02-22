word = input('Write down a word: ')

if word == 'banana':
    print('All right, banana.')
if word < 'banana':
    print('Your word, '+word+', comes before banana.')
elif word > 'banana':
    print('Your word, '+word+', comes after banana.')
