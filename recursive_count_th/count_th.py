'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    target = 'th'
    # recursion requires a base case
    if len(word) <= 1:
        return 0
    elif target not in word:
        return 0
    # to find a way to get multiple instances of 'th' in a word
    # as of now, it only sees the first one
    elif target in word:
        sub_index = word.find(target) + 2
        sub_string = word[sub_index:]
        count +=1
        return count + count_th(sub_string)


print(count_th('thethethethet'))