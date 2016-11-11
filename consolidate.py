from os import listdir
from os.path import isfile, join
import json

docTFIDFs = {}
for file in listdir("./data"):
	d = json.load(open("./data/" + file))
	docTFIDFs.update(d)
	print(d)


json.dump(docTFIDFs, open("stack-tfidf.json",'w'))