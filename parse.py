import json
import glob
import os
import string

files = glob.glob("./tweets/data/js/tweets/*.js")

#storing files after removing the first line
if not os.path.exists("temp"):
	os.makedirs("temp")
i=0;	
for f in files:
	fdata=open(f)
	fdata.readline()
	fname="temp/temp"+str(i)
	fw = open(fname,'w')
	for line in fdata:
		fw.write(line)
	fdata.close()
	fw.close()
	i=i+1;

#parsing those files to get tweets
tweets=[]	
for i in range(0,len(files)):
	jsondata=open("temp/temp"+str(i))
	parsedData = json.load(jsondata)
	tweets.append(parsedData[0]["text"])

mydict={}	
for tweet in tweets:
	#removing punctuation
	for p in string.punctuation:
		tweet = tweet.replace(p,"")
	words = tweet.split()
	for word in words:
		if word in mydict.keys():
			mydict[word]+=1
		else:
			mydict[word]=1 


sortedDict = sorted(mydict, key=mydict.__getitem__, reverse=True)

print "Top 5 used words"
for i in range(0,5):
	print sortedDict[i]
