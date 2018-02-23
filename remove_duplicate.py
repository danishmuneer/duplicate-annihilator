import os, sys

a=os.path.dirname(sys.argv[0])
excel03=dict()
excel07=dict()
flag=0

print "If duplicate files found, the one with .xls extension will be deleted."
print
print

for name in os.listdir(a):
    path=os.path.join(a,name)



    
    if os.path.isfile(path):
        splitting=os.path.splitext(name)
        if splitting[1]==".xls":
            excel03[splitting[0]]=None
        if splitting[1]==".xlsx":
            excel07[splitting[0]]=None

for item in excel03:
    if item in excel07:
        flag=1
        showdown=os.path.join(a,item+".xls")
        os.remove(showdown)

if flag==0:
    print "There are no duplicate files"
    raw_input()
else:
    print "Duplicate files removed"
    raw_input()