#Mattias Rannamäe
#IT-20
#13.01.2021
#python turtle

import turtle
import random
import math

aken = turtle.Screen()
aken.setup(1000,1000)


sein = turtle.Turtle()
uks = turtle.Turtle()
katus = turtle.Turtle()
k = turtle.Turtle()
S = turtle.Turtle()
tagasi = 500

#1

# def pluss():
#     kylg = 185
#     lkylg = 130
#     nurk = 90
#     
#     S.penup()
#     S.back(tagasi)
#     S.pendown()
#     for i in range(1):
#         S.fd(lkylg)
#         S.lt(nurk)
#         S.fd(kylg)
#         S.rt(nurk)
#         S.fd(kylg)
#         
#         S.lt(nurk)
#         S.fd(lkylg)
#         S.lt(nurk)
#         S.fd(kylg)
#         S.rt(nurk)
#         S.fd(kylg)
#         
#         
#         S.lt(nurk)
#         S.fd(lkylg)
#         S.lt(nurk)
#         S.fd(kylg)
#         S.rt(nurk)
#         S.fd(kylg)
#         
#         
#         S.lt(nurk)
#         S.fd(lkylg)
#         S.lt(nurk)
#         S.fd(kylg)
#         S.rt(nurk)
#         S.fd(kylg)



#13

def midagi():
      
    kylg = 200
    nurk = 100
    k.pensize(5)
    k.speed(0)
    for i in range(1):
        k.penup()
        k.rt(90)
        k.fd(math.sqrt(200*200-100*100)/2)
        k.lt(90)
        k.pendown()
        k.fd(100)
        k.lt(120)
        k.fd(200)
        k.lt(120)
        k.fd(200)
        k.lt(120)
        k.fd(100)
        k.lt(90)
        k.fd(math.sqrt(200*200-100*100)/2)
        k.lt(180)
        k.fd(87)
        k.lt(90)
            
    #vasak
    for i in range(1):
        k.lt(68)
        k.fd(100)
        k.lt(120)
        k.fd(200)
        k.lt(120)
        k.fd(200)
        k.lt(120)
        k.fd(100)
        k.lt(90)
        k.fd(math.sqrt(200*200-100*100)/2)
        k.lt(180)
        k.fd(87)
            
    #parem
    for i in range(1):
        k.lt(135)
        k.fd(100)
        k.rt(120)
        k.fd(200)
        k.rt(120)
        k.fd(200)
        k.rt(120)
        k.fd(100)
        k.rt(90)
        k.fd(math.sqrt(200*200-100*100)/2)
        k.rt(180)
            
    #parem alumine
    for i in range(1):      
        k.fd(187)
        k.lt(120)
        k.fd(200)
        k.lt(120)
        k.fd(200)
        k.lt(120)
        k.fd(100)
        k.lt(90)
        k.fd(math.sqrt(200*200-100*100)/2)
        k.lt(180)
           
        #vasak alumine
        k.fd(87)
        k.lt(90)
        k.rt(50)
        k.fd(100)
        k.lt(120)
        k.fd(200)
        k.lt(120)
        k.fd(200)
        k.lt(120)
        k.fd(100)
        k.lt(90)
        k.fd(math.sqrt(200*200-100*100)/2)
        k.lt(180)
    
       

        

        


#18
# def maja():
#     maja = 6
#     sein.penup()
#     sein.back(tagasi)
#     sein.pendown()
# 
# 
#     #maja ruut
#     sein.pensize(2)
#     kylg = random.randint(150, 200)
#     nurk = 90
#     sein.speed(60)
#     
#     uks.penup()
#     uks.back(tagasi)
#     uks.pendown()
#     #uks
#     uks.pensize(2)
#     uks.speed(60)
#     uks.color("blue")
#     uks.penup()
#     uks.fd(20)
#     uks.pendown()
#     uksekylg = random.randint(50, 70)
#     uksenurk = 90
#     
#     katus.penup()
#     katus.back(tagasi)
#     katus.pendown()
#     #katus
#     katus.pensize(2)
#     katus.speed(60)
#     katus.color("green")
#     katus.penup()
#     katus.lt(90)
#     katus.fd(90)
#     katus.rt(90)
#     katus.pendown()
#     kylg = 90
# 
# 
# 
#     for n in range(maja):
#             sein.penup()
#             sein.fd(220)
#             sein.pendown()
#             for i in range(4):
#                 sein.fd(kylg)
#                 sein.lt(90)
# 
# 
#     for n in range(maja):
#             uks.penup()
#             uks.fd(220)
#             uks.pendown()
#             for i in range(4):
#                 uks.fd(uksekylg)
#                 uks.lt(uksenurk)
#             
#     for n in range(maja):        
#             katus.penup()
#             katus.fd(220)
#             katus.pendown()
#             for i in range(3):
#                 katus.fd(kylg)
#                 katus.lt(120)

    
midagi()
#maja()
#pluss()