# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:11:48 2017

@author: ZHENGHAN ZHANG
"""








'''
Author: Harry Zhenghan Zhang
This program is a game
It is an interactive nonogram puzzle solver called the Pythonogram
You should enter the coordinates of the space where you think there should be an '*'
The patterns of distribution of '*' would be shown to you
Have fun!
'''
 
import layout
import random
import datetime

#ESTABLISH THE TIMER PARAMETERS
starttime=datetime.datetime.now()

#first, generate both the master-list and the scratch-list
#usable variables: layout.rows,  layout.columns,layout.marker.empty and layout.marker.full
#generate the master-board list first

masterList=[]

for i in range(layout.rows):
    sublist=[]
    for j in range(layout.columns):
        randomizer=random.randint(0,1)
        if randomizer==0:
            sublist.append(layout.marker.empty)
        else:
            sublist.append(layout.marker.full)
    masterList.append(sublist)
#test the masterList
#print(masterList)

#establish the scratch list: all with empty values
scratchList=[]
for i in range(layout.rows):
    sublist=[]
    for j in range(layout.columns):
        sublist.append(layout.marker.empty)
    scratchList.append(sublist)
#print(scratchList)

#tomography in a list---two dimensional
#starting with the rows
row_tomo=[]
#list out a single row----test it with a single list first
#establish a test list
'''
testList1=[1,0,0,1,1,1,0,1,1]
testList2=[1,0,0,0,1,1,0,1,0]
testList3=[0,0,1,0,1,1,0,1,1]
tomo=[]
m=0
for i in range(len(testList3)):
    if testList3[i]==1:
        m+=1
    else:
        if m==0:
            continue
        else:
            tomo.append(m)
            m=0
if m!=0:
    tomo.append(m)
print(tomo)

'''
#here we have the skeleton code for the single-row

#perform the all-row integration:
for i in range(layout.rows):
    tomo=[]
    m=0
    for j in range(layout.columns):
        if masterList[i][j]==layout.marker.full:
            m+=1
        else:
            if m==0:
                continue
            else:
                tomo.append(m)
                m=0
    if m!=0:
        tomo.append(m)
    row_tomo.append(tomo)
#print(row_tomo)

#switch into all-column integration:
column_tomo=[]    
for i in range(layout.columns):
    tomo=[]
    m=0
    for j in range(layout.rows):
        if masterList[j][i]==layout.marker.full:
            m+=1
        else:
            if m==0:
                continue
            else:
                tomo.append(m)
                m=0
    if m!=0:
        tomo.append(m)
    column_tomo.append(tomo)
#print(column_tomo)


#USER INTERFACE:OUTSIDE LOOP
#set the parameters
a=0#total attempts
b=0#sucessful attempts
while True:  
    a+=1  
#print the scratch board for the user:
    for i in range(layout.rows):    
        print((layout.board.corner + layout.board.top)*layout.columns + layout.board.corner)
        m=''
        for j in range(layout.columns):
            m+=layout.board.side
            m+=scratchList[i][j]
        m+=layout.board.side
        for k in range(len(row_tomo[i])):
            m+=str(row_tomo[i][k])
            m+=' '
        print(m)
    print((layout.board.corner + layout.board.top)*layout.columns + layout.board.corner)



#find the longest sublist of column_tomo
#ASK THE PROFESSOR ABOUT IF THIS WOULD AFFECT THE LISTS
    x=column_tomo[-1]
    for i in range(layout.columns):
        if len(column_tomo[i])>=len(x):
            x=column_tomo[i]
    k=len(x)

#print out the column numbers
    for i in range(k):
        m=''
        for j in range(layout.columns):
            m+=' '
            if i<len(column_tomo[j]):
                m+=str(column_tomo[j][i])
            else:
                m+=' '
        print(m)
            
        
#start with user interface   
    guess=input('Please enter your guess (row, col): ').split(',')
    x=int(guess[0])-1
    y=int(guess[1])-1
    if masterList[x][y]==layout.marker.full and scratchList[x][y]!=layout.marker.full:
        scratchList[x][y]=layout.marker.full
        b+=1
    if masterList==scratchList:
        break

    


#print original list
print('You have completed the game!','Here is the correct answer',sep='\n')
for i in range(layout.rows):    
    print((layout.board.corner + layout.board.top)*layout.columns + layout.board.corner)
    m=''
    for j in range(layout.columns):
        m+=layout.board.side
        m+=masterList[i][j]
    m+=layout.board.side
    print(m)
print((layout.board.corner + layout.board.top)*layout.columns + layout.board.corner)

#print the accuracy
accuracy=(b/a)*100
print('You made',a,'guesses')
print(b,'of which are correct!')
print('The total accuracy of your guesses is: ',accuracy,'%',sep='')

#print the timer
finishtime=datetime.datetime.now()
z=finishtime-starttime
print('The time taken to complete the task is:',z,sep='')
#finally!