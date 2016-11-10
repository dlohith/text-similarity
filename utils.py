import math
from scipy import spatial

def inverseDocumentFrequency(term, allDocuments):
  numDocumentsWithThisTerm = 0
  for doc in allDocuments:
    if term.lower() in doc.lower().split():
      numDocumentsWithThisTerm = numDocumentsWithThisTerm + 1
 
  if numDocumentsWithThisTerm > 0:
    return 1.0 + math.log(float(len(allDocuments)) / numDocumentsWithThisTerm)
  else:
    return 1.0

def termFrequency(term, document):
  normalizeDocument = document.lower().split()
  return normalizeDocument.count(term.lower()) / float(len(normalizeDocument))


def getTFIDF(document, allDocuments):
  terms = document.lower().split()
  tfidfs = []
  for term in terms:
    tf = termFrequency(term, document)
    idf = inverseDocumentFrequency(term, allDocuments)
    tfidf = tf * idf
    tfidfs.append(tfidf)
  return tfidfs

def cosineSimilarity(query,document):
  paddingLen = abs(len(query) - len(document))
  padding = [0] * paddingLen
  if(len(query) > len(document)):
    document.extend(padding)
  elif(len(document) > len(query)):
    query.extend(padding)

  return 1 - spatial.distance.cosine(query, document)


