from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<result>')
def success(result):
   return 'resulting permutations: %s' % result

@app.route('/test',methods = ['POST', 'GET'])
def test():
   if request.method == 'POST':
      out = request.form['sentence']
      return redirect(url_for('success',result = out))
   else:
      user = request.args.get('sentence')
      return redirect(url_for('success',result = out))

if __name__ == '__main__':
   app.run(debug = True)