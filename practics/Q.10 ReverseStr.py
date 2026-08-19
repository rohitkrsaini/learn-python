str = "i love my country"
print(str)
rev = " ".join(str.split()[::-1])
print(rev)

# world revese
wRev = str.split()
reverse = []
for i in range(len(wRev)):
   reverse.append(wRev[i][::-1])

final = " ".join(reverse)
print(final)

#