'''
Your function should take in a single parameter (a string `word`)
Your function should return a count_num of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    count_num = 0

    # TBC
    # if the word is empty/blank, return 0
    if len(word) < 2:
        return 0

    # checking to see if th are next?
    if word[:2] == 'th':
        count_num = 1

    # count_num goes up
    if count_num == 1:
        word = word[2:]
    # if count_num doesnt go up
    else:
        word = word[1:]

    return count_th(word) + count_num
