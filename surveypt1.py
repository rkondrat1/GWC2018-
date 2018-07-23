
survey=['what is your name','what is your drink','what is your entree', 'what is your side']

des={}

answers=['name','drink','entree','side']

total=[]
status='yes'
while status=='yes':
    for i in range(len(answers)):
        wow=input(survey[i]+':  ')
        des[answers[i]]=wow

    total.append(des)
    status=input('do you want to continue?')

print (total)
