import utils
import json
from multiprocessing.pool import Pool
import uuid


#{question : tfidfs}
docTFIDFs ={}
# {question:answer}
data = {}

def updateTFIDFs(question):
	docTFIDFs={}
	docTFIDFs[question]  = utils.getTFIDF(question, questions)
	json.dump(docTFIDFs, open("./data/"+ str(uuid.uuid4()) + ".json",'w'))


with open("data.csv", "r") as ins:
  for line in ins:
        arr = line.split(",")
        data[arr[0].split('\'')[1]] = arr[1].split('\'')[1]


questions = list(data.keys())
print("number of questions : "+ str(len(questions)))
print("Calculating TFIDF and caching")


pool = Pool(10)
pool.map(updateTFIDFs, questions)
pool.close
pool.join

