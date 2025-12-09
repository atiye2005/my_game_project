my_sentence = input("enter your sentence : ")

nums = []

for  char in my_sentence:
    nums.append(str(ord(char)+12))

    

print(','.join(nums))
