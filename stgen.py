#Python keycard gen

#Parking garage code: 1H34N678

#Concourse code: C234N678

#Executive code: CH345678

numbers = [0,1,2,3,4,5,6,7,8,9]
nums=[]
code = "FFFFFFFF"
positions = []
card = []
numCards = 0
codelist = []

def split(word):
    return [ char for char in word ]


def china_room(numbers,list,cnt=0):
    for i in numbers:
        temp_lst_a = [lst if lst!="h" else str(i) for lst in list]

        for j in numbers:
            if j != i:
                codelist.append(int("".join([lst if lst!="n" else str(j) for lst in temp_lst_a])))
                cnt+=1

def house_room(numbers,nums,list,cnt=0):
    for i in nums:
        temp_lst_a = [lst if lst!="h" else str(i) for lst in list]
        for j in numbers:
           for k in numbers:
               if k!=j:
                   temp_lst_b = [lst if lst!="c" else str(j) for lst in temp_lst_a]
                   codelist.append(int("".join([lst if lst!="n" else str(k) for lst in temp_lst_b])))
                   cnt+=1
def nose_room(numbers,nums,list,cnt=0):
    for i in nums:
        temp_lst_a = [lst if lst!="n" else str(i) for lst in list]
        for j in numbers:
           for k in numbers:
               if k!=j:
                   temp_lst_b = [lst if lst!="c" else str(j) for lst in temp_lst_a]
                   codelist.append(int("".join([lst if lst!="h" else str(k) for lst in temp_lst_b])))
                   cnt+=1

def nBrute(code):
    lCode = split(code)

    for i in lCode:
        if i.isnumeric():
            nums.append(int(i))
    for i in nums:
        numbers.remove(i)
    if "c" not in lCode:
        china_room(numbers,lCode)
    if lCode.count("h") == 1:
        house_room(numbers,nums,lCode)
    if lCode.count("h") == 2 and lCode.count("c") == 1:
        nose_room(numbers,nums,lCode)
    
    output = list(dict.fromkeys(codelist))

    print(output)
    print(str(len(output)) + " Possibilities")
    
    
def bruteforce(code):

    code = code.lower()
    count = 0

    nBrute(code)

    return 0
    for i in range( len(code) ):
        if code[i] not in numbers:
            count = count+1
            positions.append(int(i))

    print("Solving for " + str(count) + " positions")
    count = 0

    tcode = code

    codelist = []

    if len(positions) == 2:
            for x in numbers:
                tcode = gen(position[0])
                
                for y in numbers:
                    tcode = tcode[:positions[1]] + y + tcode[positions[1]+1:]
                    codelist.append(tcode)
    else:
            for x in numbers:
                tcode = code[:positions[0]] + x + code[positions[0]+1:]
                codelist.append(tcode)

    codelist = list(dict.fromkeys(codelist))
    print(codelist)
    print("There are " + str(len(codelist)) + " possibilities")
    return 0


#Main
try:
    numCards = int(input("Number of Cards Acquired:"))
    if numCards > 3:
        numCards = 3
    if numCards < 0:
        numCards = 0
except:
    print("Please enter a numeric value")


for i in range(int(numCards)):
    c = input("Enter Card " + str(i+1) + ":")
    card.append(c)

code = card[0]

for c in card:
    for i in range( len(c) ):
        try:
            x = int(c[i],10)
        except:
            x = -1
        if x > -1:
            code = code[:i] + c[i] + code[i+1:]         
        

print("Entered " + str(numCards) + " Cards")
print(card)

if len(card) < 3:
    yn = input("You do not have all 3 cards. Bruteforce (y/n)?")
    if yn.lower() == "y":
        print("Printing Bruteforce list for code: " + code)
        bruteforce(code)
else:
    print("Final Code: " + code )
