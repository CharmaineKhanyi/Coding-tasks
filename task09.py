def vowel(text):

    vowels = "aeiuoAEIOU"
    
    print([letter for letter in text if letter in vowels])
    
    
vowel('MyVowelString')