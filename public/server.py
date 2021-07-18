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
		# What is your recommended color? The recommended color is red. Please use it.
		prediction = Prediction(request.form['fullSentence'])
		predictorOutput = prediction.getPredictorOutput()
		print(predictorOutput)
		example = Coreference(predictorOutput, request.form['broadReference'])
		print("after creating object")
		r = example.generateReferences()
		print(r)
		
		print("before return")
		# return redirect(url_for('success',result = out))
		return r
	#else:
		#out = request.args.get('fullSentence')
		# return redirect(url_for('success',result = out))

if __name__ == '__main__':
	print("before run")
	func_out = app.run(debug = True)
	print("after run")
	print("func_out: ", func_out)
