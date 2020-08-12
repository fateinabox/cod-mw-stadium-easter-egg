#Python keycard gen

#Parking garage code: 1H34N678

#Concourse code: C234N678

#Executive code: CH345678

numbers = ["0","1","2","3","4","5","6","7","8","9"]
code = "HHHHHHHH"
positions = []
card = []

def bruteforce(code):
    code = code.lower()
    count = 0
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
                tcode = tcode[:positions[0]] + x + tcode[positions[0]+1:]
                
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
