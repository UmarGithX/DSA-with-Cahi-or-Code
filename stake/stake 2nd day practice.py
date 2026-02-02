stake = []

stake.append(10)
stake.append(20)
stake.append(30)
stake.append(40)

# print(stake)

#adding new element to stake
def adding():
    stake.append(50)
    print(f"After adding the stake is : {stake}")
    print(f"Total Length of the length of the stake is {len(stake)}")

# removing from stake
def removing():
    if len(stake) == 0:
        print("stake is Already Empty")
    else:
        stake.pop()
        print(stake)

# to see what is on the stake
def see():
    if len(stake) == 0:
        print("stake is underFlow")
    else: 
        saw = stake[-1]
        print(saw)

adding()
# removing()
# see()   