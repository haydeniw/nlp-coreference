from allennlp.predictors.predictor import Predictor
from Predictor import Prediction
import allennlp_models.tagging


def main():
	example = Coreference("What is your recommended color? The recommended color is red. Please use it.", "Please use it.")
	result = example.generateReferences()
	print(result)

class Coreference:
	def __init__(self, predictorOutput, currentSentence):
		self.predictorOutput = predictorOutput
		#self.context = context
		self.currentSentence = currentSentence
		self.broad_refs = ["he", "she", "this", "that", "them", "it"]
		self.coreferences = []

	def generateClusters(self):
		#function modified from: https://github.com/ananyagup/AllenNLP-Coreference-Resolution-in-Python-Readable-clusters
		#predictorOutput = predictor.predict(document="What is your recommended color? The recommended color is red. Please use it.")
		clusters = self.predictorOutput['clusters']
		document = self.predictorOutput['document']
		n = 0
		doc = {}
		for obj in document:
			doc.update({n :  obj}) #what I'm doing here is creating a dictionary of each word with its respective index, making it easier later.
			n += 1
		clus_all = []
		cluster = []
		sublist = []
		for i in range(0, len(clusters)):
			one_cl = clusters[i]
			for count in range(0, len(one_cl)):
				obj = one_cl[count]
				for num in range((obj[0]), (obj[1]+1)):
					for n in doc:
						if num == n:
							sublist.append(doc[n])
							if n == obj[1]:
								cluster.append(sublist)
								sublist = []
			clus_all.append(cluster)
			cluster = []

		#print(clus_all) #shows all coreferences
		return clus_all

		# generateReferences takes in a context (1+ previous sentences)
		# and a current sentence and replaces all broad references with  
		# coreferences and the broad reference itself
		# TODO: extend list of broad references
	def generateReferences(self):
		modified = []
		clus_all = self.generateClusters()
		for cluster in clus_all:
			newW = ""
			for word in enumerate(cluster):
				if word[0] in self.broad_refs: #only supports a broad reference that is 1 word
					for newWord in cluster:
						if len(newWord) == 1:
							if newWord not in self.broad_refs:
								modified.append(self.currentSentence.replace(word[0], newWord[0]))
						else:
							newW =  ' '.join(newWord)
							modified.append(self.currentSentence.replace(word[0], newW))
					self.coreferences = list(set(modified))
					return self.coreferences

					
					
# example: "Paul Allen was born on January 21, 1953, in Seattle, Washington, to Kenneth Sam Allen and Edna Faye Allen. Allen attended Lakeside School, a private school in Seattle, where he befriended Bill Gates, two years younger, with whom he shared an enthusiasm for computers."
#print("modified sentence: ", generateReferences("Paul Allen was born on January 21, 1953, in Seattle, Washington, to Kenneth Sam Allen and Edna Faye Allen. Allen attended Lakeside School, a private school in Seattle, where he befriended Bill Gates, two years younger, with whom he shared an enthusiasm for computers.", "with whom he shared an enthusiasm for computers."))

if __name__ == "__main__":
	main()


