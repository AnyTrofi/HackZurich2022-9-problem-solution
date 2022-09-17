from flask import Flask, jsonify, request
from db import add_user_to_bd, log_user, check_statistic, add_user_data

app = Flask(__name__)
client = app.test_client()


# {'user_name': '###', 'user_password': '###', 'user_email': '###', 'user_adress': '###'}
# If everything went well, will return id, else -1
@app.route('/reg', methods=['POST'])
def reg():
	user_info = request.get_json()
	try:
		result = add_user_to_bd(user_info['user_name'], user_info['user_password'], user_info['user_email'], user_info['user_adress'])
		return jsonify(result)
	except:
		print('error')
		return -1

# {'user_name': '###', 'user_password': '###', 'user_email': '###'}
# If everything went well, will return id, else -1
@app.route('/log', methods=['POST'])
def log():
	user_info = request.get_json()
	try:
		result = log_user(user_info['user_email'], user_info['user_password'])
		return jsonify(result)
	except:
		print('error')
		return -1

# {'user_id': ###, 'date': ###, 'value': ###}
# return 'wrong' or 'success'
@app.route('/add', methods=['POST'])
def add():
	user_info = request.get_json()
	try:
		result = add_user_data(user_info['user_id'], user_info['date'], user_info['value'])
	except:
		print('error')
		result = 'Wrong'
	return jsonify(result)

# {'user_id': ###}
# return 'wrong' or 'success'
@app.route('/stat', methods=['POST'])
def stat():
	user_info = request.get_json()
	try:
		result = check_statistic(user_info['user_id'])
	except:
		print('error')
		result = []
	return jsonify(result)


if __name__ == '__main__':
	app.run()
