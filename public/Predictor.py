from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging

def main():
	print("hiii")
	p = Prediction("What is your recommended color? The recommended color is red. Please use it.")
	print(p.getPredictorOutput())

class Prediction:
	def __init__(self, context):
		self.context = context
		self.predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz")
		self.predictorOutput = self.predictor.predict(document=self.context)
	
	def getPredictorOutput(self):
		return self.predictorOutput
		
if __name__ == "__main__":
	main()
