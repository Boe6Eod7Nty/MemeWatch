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
'''

