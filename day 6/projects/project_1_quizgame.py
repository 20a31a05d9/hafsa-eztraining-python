q1=''' a.what is the hightest mountain in the world?
       1. himalaya
       2. Mount Arvon.
       3.Backbone Mountain.
       4.Baldy Mountain.
'''  
q2=''' b.when can we vote?
       1.16
       2.18
       3.30
       4.50
'''
q3=''' c.where is taj mahal?
       1.paris
       2.korea
       3.india
       4.new zealand
'''
q4=''' c.who is mahatma gandhi?
       1.actor
       2.dancer
       3.singer
       4.freedom fighter
'''
q5=''' c.which is in red color?
       1.ocean
       2.blood
       3.sky
       4.water
'''

dict={ q1:1,q2:2,q3:3,q4:4,q5:2}
name= input("enter your name:")
print('hi',name,"welcome to quiz")
z=input("can we start the quiz?(yes/no)")
score=0
if z =="yes":
 for i in dict:
    print(i)
    ans=int(input("enter your choice:"))
    if ans==dict[i]:
        score=score+1
        print("yeah your answer is correct")
        print("your current score is",score)
    else:
        score=score-1
        print("wrong answer")
        print("your current score is",score)

    flag =input("do you want to continue?(yes/no)")
    if flag=="yes":        #list(dict)[-1]
       continue
    else:
        print("thank you")
        break
else:
    print("thank you")
    
