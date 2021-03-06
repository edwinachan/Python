#What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

#'abba' & 'baab' == true

#'abba' & 'bbaa' == true

#'abba' & 'abbba' == false

#'abba' & 'abca' == false
#Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

#anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

#anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

#anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):

    newList = []
    
    for anagram in words:
        count = 0
        for letter in anagram:
            if anagram.count(letter) == word.count(letter):
                count += 1
        if count == len(word) and set(word) == set(anagram):
            newList.append(anagram)
    return newList

#Or more simply

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
