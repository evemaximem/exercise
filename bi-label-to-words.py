import sys

def read_instance(fp):
    file1=open(fp,'r')
    sentence=file1.read().splitlines()
    sour=[]
    for i in sentence:
        i=i.split()
        if i!=[]:
            sour.append(i)
    return sour;

def bi2words(chars):
    for i in len(chars):
        if chars[i][1]=='B' and chars[i+1][1]=='B':
            file2=open('sol.txt', 'a')
            file2.write(chars[i])
            file2.write(' ')
        if chars[i][1] == 'B' and chars[i + 1][1] == 'i':
            file2.write(chars[i])

    if chars[1]=='B':
        file2 = open('sol.txt', 'a')
        file2.write(chars[0])
    else:
        file2 = open('sol.txt', 'a')
        file2.write(chars[0])


for i in read_instance('data.txt'):
    bi2words(i)
