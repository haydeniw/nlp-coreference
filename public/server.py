from flask import Flask, redirect, url_for, request
from Coreference import Coreference
from Predictor import Prediction

app = Flask(__name__)

@app.route('/success/<result>')
def success(result):
	return 'resulting permutations: %s' % result

@app.route('/test', methods = ['POST', 'GET'])
def test():
	if request.method == 'POST':
		#print("hello22")
		# need to move this to on page load
		# prediction = Prediction("What is your recommended color? The recommended color is red. Please use it.")
		# predictorOutput = prediction.getPredictorOutput()
		# print(predictorOutput)
		# example = Coreference("What is your recommended color? The recommended color is red. Please use it.", "Please use it.")
		# #example = Coreference("What is your recommended color? The recommended color is red. Please use it.", "Please use it.")
		# print("after creating object")
		# r = example.generateReferences()
		# print(r)
		out = request.form['sentence']
		return redirect(url_for('success',result = out))
	else:
		out = request.args.get('sentence')
		return redirect(url_for('success',result = out))

if __name__ == '__main__':
	app.run(debug = True)