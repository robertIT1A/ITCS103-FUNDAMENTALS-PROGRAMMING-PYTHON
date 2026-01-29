word = input("Enter a word: ")
length = len(word)
num_length = []
for i in range(length):
    num = int(input(f"Enter a number {i+1}: "))
    num_length.append(num)
    
def average():
    avg = sum(num_length)/length
    print(f"The average of the number is {avg}")

def compares():
    avg = sum(num_length)/length
    if length == avg:
        print(f"The length of the word '{word}' is equal the average")
    elif length >= avg:
        print(f"The length of the word '{word}' is greater than the average")
    elif length <= avg:
        print(f"The length of the word '{word}' is less than the average")
    else:
        print("not")

print(num_length)
print(f"The length of the word is {length}")
average()
compares()

