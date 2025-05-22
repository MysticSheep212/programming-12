#
# Chapter 10 Practice
# Dylan Le Voguer
#

def invert_dictionary(dictionary):
    inverted_dictionary = {}
    for key in dictionary:
        value = dictionary[key]
        inverted_dictionary[value] = key
    return inverted_dictionary


d = {'spring': 1, 'summer': 4, 'fall': 7}
print(invert_dictionary(d))