fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lstline = line.split()
    lst = lst + lstline
lst.sort()
print(lst)
