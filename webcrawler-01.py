from __future__ import print_function
import sys
import pip
import praw
import csv
import os

os.chdir('C:\Users\Benjamin\Python')

reddit = praw.Reddit(client_id='cr6fA22zW_2ZqA',
                     client_secret='8cw3h11hDyCu3rfKvt4PTpaL-Q0',
                     user_agent='python:ch.memewat:v0.0.1 (by /u/boe6eod7nty')
'''
for submission in reddit.subreddit('all').hot(limit=10):
    print(submission.title[0:75], '---', submission.score)
'''

c = csv.writer(open("data.csv", "wb"))

c.writerow(["Name","Address","Telephone","Fax","E-mail","Others"])

cr = csv.reader(open("data.csv","rb"))

for row in cr:
    print(row)