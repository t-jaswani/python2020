#bin() for integer
#Python bytes()
#Python compile()
#dir([object])
#Python filter()
#_name_ or _main_ *specail variable
#Python exec()

alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(x):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(x in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)


print(type(filteredVowels))

print('The filtered vowels are:')
for y in filteredVowels:
    print(y)