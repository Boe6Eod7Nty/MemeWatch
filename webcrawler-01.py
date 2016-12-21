from __future__ import print_function
import sys
import os
import praw
import csv
import numpy as np
import time

os.chdir('/Users/andersonbe/MemeWatch')

reddit = praw.Reddit(client_id='cr6fA22zW_2ZqA',
                client_secret='8cw3h11hDyCu3rfKvt4PTpaL-Q0',
                user_agent='python:ch.memewat:v0.0.1 (by /u/boe6eod7nty')

memes = [['pepe'],['me_irl','me irl','meirl'],['dat_boi','dat boi']]

try:
    reddit.subreddit('worldnews').title
except Exception, e:
    print('TypeError: ',str(e),', Unable to connect to /r/worldnews subreddit')
else:
    try:
        #empties data2.csv for new writing
        f = open('data2.csv','w')
        f.truncate()
        f.close()
        
        #Writes top X posts in /r/all into data2.csv as title & score
        x=0
        postsGrabbed = list(reddit.subreddit('all').hot(limit=10))
        for eachPost in postsGrabbed[:-1]:
            saveLine = '\"'+eachPost.title+'\",'+str(eachPost.score)+'\n'
            saveFile = open('data2.csv','a')
            saveFile.write(saveLine)
            saveFile.close()
            x+=1
        saveLine = postsGrabbed[-1].title+','+str(postsGrabbed[-1].score)
        saveFile = open('data2.csv','a')
        saveFile.write(saveLine)
        saveFile.close()
        
    except Exception, e:
        print('TypeError: ',str(e))

try:
    #creates/re-writes to DAY-HH-MM.csv file, records 
    
    currTime = ('records/'
                +time.strftime('%a-%H-')
                +str(int(time.strftime('%M'))
                    -(int(time.strftime('%M'))%5)))
    
    #currTime = 'records/temp1'
    n=0
    fileDate = open('%s.csv' % currTime, 'w+')
    title, score = np.genfromtxt('data2.csv',
                              delimiter=',',
                              unpack=True,
                              dtype='str',
                              usecols=np.arange(0,1))
    for eachRow in title[:-1]:
        for meme in memes:
            for spelling in meme:
                if spelling in title.decode('utf-8').lower():
                    try:
                        title.index(meme)
                    except Exception, e:
                        saveLine = '\"'+meme[0]+'\",'+title[1]+'\n'
                        saveFile = open('%s.csv' % currTime,'a')
                        saveFile.write(saveLine)
                        saveFile.close()
                    else:
                        pass
    
except Exception, e:
    print('TypeError: ',str(e))

'''
for submission in reddit.subreddit('all').hot(limit=10):
    print(submission.title[0:75], '---', submission.score)
'''
