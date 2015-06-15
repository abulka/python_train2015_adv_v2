from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello world'

@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello_world2(name=None):
    return 'hello world %s you attempt to do a %s on my url' % (name, request.method)

# Ps can route similar url which has differently typed url components (e.g. int vs string) to different functions e.g.
@app.route('/hello/<int:name>')
def hello_world2_int(name=None):
    res = ""
    num_times = name  # since a number was passed in
    for i in range(num_times):
        res += "hello! "
    return res

# technique 2
# To access parameters submitted in the URL (?key=value) you can use the args attribute:
@app.route('/hello3', methods=['GET'])
def hello_world3():
    who = request.args.get('who', 'stranger')  # if parameter not found
    return "hello %s" % who


# technique 3 - get the info via a POST
@app.route('/info1', methods=['POST'])
def info1():
    if request.method == 'POST':
        print request.form
    return 'Name is %s' % request.form['name']


from flask import render_template
@app.route('/template1')
def template1():
    return render_template('template1.html',
                           info='here is some info',
                           num_times=20,
                           )

from flask import render_template
@app.route('/cars')
def cars():

    class Car:
        def __init__(self, id, name, price):
            self.Id = id
            self.Name = name
            self.Price = price

    cars = [
        Car(1, 'VW', 5000),
        Car(2, 'Mercedes', 210000),
        Car(3, 'Jag', 110000) ]

    return render_template('template2.html',
                           cars=cars)



if __name__ == '__main__':
    app.run(debug=True)  # the server will automatically reload when source code changes
