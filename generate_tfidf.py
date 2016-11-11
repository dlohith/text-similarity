import utils
import json

#{question : tfidfs}
docTFIDFs ={}
# {question:answer}
data = {}

with open("data.csv", "r") as ins:
  for line in ins:
                arr = line.split(",")
                data[arr[0].split('\'')[1]] = arr[1].split('\'')[1]


questions = list(data.keys())
print("number of questions : "+ str(len(questions)))
print("Calculating TFIDF and caching")
i =0 
for question in questions:
	i = i +1
	print(i)
        docTFIDFs[question] = utils.getTFIDF(question, questions)
json.dump(docTFIDFs, open("stack-tfidf.json",'w'))
