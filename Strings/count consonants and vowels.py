#count consonants and vowels
def count_vowels_consonants(s):
    vowels="aeiouAEIOU"
    v_count=0
    c_count=0
    for char in s:
        if char in vowels:
            v_count+=1
        else:
            c_count+=1
    return c_count,v_count
c,v=count_vowels_consonants("hello")
print("consonants:",c)
print("vowels:",v)
