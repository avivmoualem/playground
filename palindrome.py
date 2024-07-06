print('Palindrome checker!')
word = input('please enter word \n')


# print('is palindrome? ', word == word[::-1])
rev_word = ''
word_len = len(word)
for i in range(word_len):
    rev_word=rev_word+word[word_len-1-i]

print('Is a palindrome? ', word==rev_word )
