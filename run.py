import utils

#{question : tfidfs}
docTFIDFs ={}
# {question:answer}
data = {}

with open("data.csv", "r") as ins:
  for line in ins:
 		arr = line.split(",")
 		data[arr[0].split('\'')[1]] = arr[1].split('\'')[1]


questions = list(data.keys())
print("Calculating TFIDF and caching")
for question in questions:
	docTFIDFs[question] = utils.getTFIDF(question, questions)


while(1):
	query = input("Please enter question: ")
	maxSimilarity = -1
	bestQuestion = ""
	for question in questions:
		similarity = utils.cosineSimilarity(utils.getTFIDF(query, questions),docTFIDFs[question])
		if similarity > maxSimilarity:
			maxSimilarity = similarity
			bestQuestion = question
	print("best answer : " + data[bestQuestion])


