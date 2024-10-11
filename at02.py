
def count_vowel(s):
    vowel = {'а','о','е','и','у','я','ё','э','ы','ю'}
    count = 0
    for i in s:
        if i in vowel:
            count +=1

    return count
