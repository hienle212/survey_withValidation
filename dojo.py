from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
  if len(request.form['name']) < 1:
  	flash("Name cannot be empty!")
  	return redirect('/')
  elif len(request.form['comment']) < 10:
  	flash("Comment cannot be empty!")
  	return redirect('/')
  else:
  	return redirect ('/show')
@app.route('/show')
def show_user():
  return render_template('result.html', name=session['name'], location=session['location'],language=session['language'], comment=session['comment'])

app.run(debug=True) 

