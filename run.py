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
docTFIDFs = json.load(open("stack-tfidf.json"))

while(1):
	query = raw_input("Please enter question: ")
	print("\n")
	maxSimilarity = -1
	bestQuestion = ""
	print("-----------------------")
	print("Calculating tfidf for the query with all questions as reference ...")
	queryTFIDF = utils.getTFIDF(query, questions)
	print("Calling cosine similarity between all the questions to find best match ...")
	for i in range(len(questions)):
		question = questions[i]
		similarity = utils.cosineSimilarity(queryTFIDF,docTFIDFs[question])
		if similarity > maxSimilarity:
			print(similarity)
			maxSimilarity = similarity
			bestQuestion = question
	print("Best question match : " + bestQuestion)
	print("Max similarity score : " + str(maxSimilarity))
	print("Best answer : " + data[bestQuestion])


