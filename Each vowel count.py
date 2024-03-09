my_str = input("Enter your string: ")
my_str = my_str.lower()


vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

for char in my_str:
    if char in vowels:
        vowels[char] += 1

print(f"Count of Vowels in given string: {vowels}")
