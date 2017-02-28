li=[]
sm=0
d=0
print "to stop putting clues to the list press at the input , out"
while True:
    a=raw_input()
    li.append(a)
    print li,a
    d=d+1
    if a=="out":
        li.remove("out")
        break
d=d-1
for i in range(d):
    if li[i] == "0" :
        sm=sm+1
print d,sm
for i in range (sm):
    li.remove("0")
    li.append("0")
