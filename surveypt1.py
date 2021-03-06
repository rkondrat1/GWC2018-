
import json

#creating a list of questions to ask the user
survey=['what is your name','what is your drink','what is your entree', 'what is your side']


#list of names that will be the keys in the dictionary
#keys must be different, but values can be the same
answers=['name','drink','entree','side']

#this is an empty list that will store the multiple dictionaries of information
total=[]

#this while loop will allow me to get multiple peoples info and store it in the
#cont. total list created above
status='yes'
while status=='yes':

    #creating the dictionary to store the key and value
    des={}

    #goes through the survey list and records the user input
    for i in range(len(answers)):
        wow=input(survey[i]+':  ')
        des[answers[i]]=wow
#adds the dictionary of one users answers to a list called total
    total.append(des)
    status=input('do you want to continue?')

print (total)

#opens the file that will contain the user inputs
f=open('allanswers.json','r')
olddata=0
olddata=json.load(f)
total.extend(olddata)
f.close()

#reopen the file and write each entry into json format
f=open('allanswers.json','w')
f.write('[\n')

index=0
#put each entry into json format
for i in total:
    if(index<len(total)-1):
        json.dump(i,f)
        f.write(',\n')
    else:
        json.dump(i,f)
        f.write('\n')
    index+=1

f.write(']')
f.close()
