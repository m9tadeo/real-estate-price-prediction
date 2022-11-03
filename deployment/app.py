from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/GET')
def get_method():
    return "This is a route that handles GET request"

@app.route('/POST', methods=['GET', 'POST'])
def post_method():
    return "This is a route that handles POST request"

@app.route('/<int:number>/')
def multiply(number):
    return "The number " + str(number) + " multiplied by 2 is " + str(number*2)

@app.route('/query')
def by_query():
    salary = request.args.get('salary')
    bonus = request.args.get('bonus')
    taxes = request.args.get('taxes')
    result = (int(salary)) + (int(bonus)) - (int(taxes))
    return f'"result": {result}'

@app.route('/form', methods=['GET', 'POST'])
def by_form():
    # handle the POST request
    if request.method == 'POST':
        salary = request.form.get('salary')
        bonus = request.form.get('bonus')
        taxes = request.form.get('taxes')
        result = (int(salary)) + (int(bonus)) - (int(taxes))
        return f'"result": {result}'
    # otherwise handle the GET request
    return '''
              <form method="POST">
                  <div><label>Salary: <input type="text" name="salary"></label></div>
                  <div><label>Bonus: <input type="text" name="bonus"></label></div>
                  <div><label>Taxes: <input type="text" name="taxes"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

@app.route('/json', methods=['POST'])
def by_json():
    return_data = {}
    decoded = request.data.decode()
    request_data = json.loads(decoded)
    if type(request_data['salary']) == str or type(request_data['bonus']) == str or type(request_data['taxes']) == str:
        return_data['error'] = 'expected numbers, got strings.'
    elif request_data['salary'] == None:
        return_data['error'] = '3 fields expected (salary, bonus, taxes). You forgot: salary'
    elif request_data['bonus'] == None:
        return_data['error'] = '3 fields expected (salary, bonus, taxes). You forgot: bonus'
    elif request_data['taxes'] == None:
        return_data['error'] = '3 fields expected (salary, bonus, taxes). You forgot: taxes'    
    else:
        salary = request_data['salary']
        bonus = request_data['bonus']
        taxes = request_data['taxes']
        result = salary + bonus - taxes
        return_data['result'] = result
    return return_data

if __name__ == '__main__':
    app.run(debug=True, port=105)