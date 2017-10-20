from flask import Flask, redirect, url_for, request, render_template, jsonify

import os
app = Flask(__name__)
app.debug = True

# serving static files from 'static folder'
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route("/")
def index():
  return render_template('index.html')


@app.route("/hello/<name>")
def hello(name):
  return '<h1>Hello, World! %s </h1>' % name

# handle success login
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

# handle login post , get
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


# handle form submit
@app.route('/result', methods=['POST'])
def postResult():
      # render the result in the html page
      return render_template('successResult.html', result = request.form)
 


# carry forward query params to the new url (hello.html from form submit)
@app.route('/result', methods=['GET'])
def getFormData():
      return app.send_static_file('hello.html')

# return json result
@app.route('/users', methods=['GET'])
def getUsersList():
      return jsonify([{'name':'arvind','age':2}]);
          


# return json result
def getStudentsList():
      return jsonify([{'studentname':'arvind','age':2}]);
          
#maps to the url /students
app.add_url_rule('/students','getStudentsList', getStudentsList);         



if __name__ == "__main__":
  app.run()


