from __future__ import print_function
import sys
import os
import praw
import csv
import numpy as np

os.chdir('C:\Users\Benjamin\Documents\GitHub\MemeWatch')

reddit = praw.Reddit(client_id='cr6fA22zW_2ZqA',
                client_secret='8cw3h11hDyCu3rfKvt4PTpaL-Q0',
                user_agent='python:ch.memewat:v0.0.1 (by /u/boe6eod7nty')

memes = ['pepe','me irl','dat boi']

try:
    x=0
    postsGrabbed = list(reddit.subreddit('all').hot(limit=10))
    for eachPost in postsGrabbed[:-1]:
        saveLine = eachPost.title+','+str(eachPost.score)+'\n'
        saveFile = open('data2.csv','a')
        saveFile.write(saveLine)
        saveFile.close()
        x+=1
    saveLine = postsGrabbed[-1].title+','+str(postsGrabbed[-1].score)
    saveFile = open('data2.csv','a')
    saveFile.write(saveLine)
    saveFile.close()
    
    '''
    n=0
    title, score = np,loadtxt('data2.csv',
                              delimiter=',',
                              unpack=True,
                              dtype='str')
    for eachRow in title[:-1]:
        saveLine = eachRow+','+score[n]+'\n'
        save
    '''
except Exception, e:
    print('TypeError: ',str(e))


'''
for submission in reddit.subreddit('all').hot(limit=10):
    print(submission.title[0:75], '---', submission.score)
'''
'''
try:
    date, rate, arb = np.loadtxt('TutSheet.csv',
                                 delimiter=',',
                                 upack=True,
                                 dtype='str')
        for eachDate in date[x:-1]:
            plusVar = str((int(arb[x-1]))+(int(arb[x])))
            
            saveLine = eachDate+','+rate[x]+','+arb[x]+','+str(int(arb[x])+3)+','+plusVar+'\n'
            saveFile = open('newCSV.csv','a')
            saveFile.write(saveLine)
            saveFile.close()
            x+=1
        saveLine = date[-1]+','+rate[x]+','+arb[x]+','+str(int(arb[x])+3)+','+plusVar
        saveFile = open('newCSV.csv','a')
        saveFile.write(saveLine)
        saveFile.close()
        
    except Exception, e:
        print(str(e))
'''
