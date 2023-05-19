import requests

'''
PARAMETERS
- 5 letters long
- contains 4/5 of the letters in "lucas"
- starts with "l"
'''

def site_exists(name): # https://www.behindthename.com/names/letter/l
    response = requests.get('https://www.behindthename.com/name/' + str(name).lower())
    if response.status_code == 200:
        return True #name exists
    else:
        return False #name does not exist

ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
known = ['a', 'c', 'l', 's', 'u']
start = 'l'
words = []
valid = []
final = []

print("generate names")

for i in range(0, 25): #choose the index for the non-known letter
    for j in range(0, 25):
        for m in range(0, 25):
            for n in range(0, 25):
                word = start + ab[i] + ab[j] + ab[m] + ab[n]
                words.append(word)

print("check validitity")
for name in words:
    count = 0
    if known[0] in name:
        count += 1
    if known[1] in name:
        count += 1
    if known[2] in name:
        count += 1
    if known[3] in name:
        count += 1
    if known[4] in name:
        count += 1

    if count >= 4:
        valid.append(name)

print("check name")

remain = len(valid)

for name in valid:
    remain -= 1
    if site_exists(name):
        final.append(name)
    print("word " + str(remain))

print("print final names")

for name in final:
    print(name)

print("done")

'''
lacus
laeus
lagus
laius
lamus
larus
laurs
laust
lavus
laxus
leuca
louca
lucan
lucas
lucay
lucca
lucea
lucha
lucia
lucja
lucka
lucoa
lucra
lucus
lucya
luisa
lukas
luksa
lumas
lusea
lusha
lusia
lusja
luska
lussa
lusya
lycus
'''


