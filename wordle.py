import random
x=['learn','great','yearn','heard','pizza','spear','spare']
y=random.choice(x)

def enter():

    word=input('Guess ')
    if len(word)!=5:
        print('Please enter 5 letter word')
        return(0)
    if len(word)==5:
        return(word)

def check(y,word):
    l1=[]
    if y==word:
        print('Correct guess')
        return(1)
    else:
        print('wrong guess')
        s = set(word)
        r = set(y)
        d = s.intersection(r)
        print('correct letters:' + ','.join(d))
        for i in range(0, 5):
            if y[i] == word[i]:
                l1.append(y[i])
        print('The letters in order are:' + ','.join(l1))

for i in range(1,6):
    x=enter()
    if x!=0:
     z=check(y,x)
     if z==1:
        break
