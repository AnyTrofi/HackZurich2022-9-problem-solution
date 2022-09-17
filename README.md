# HackZurich2022-9-problem
The project that our team presents in issue 9 at the HackZurich hackathon

Work with backend:

Registration:

data = {'user_name': '###', 'user_password': '###', 'user_email': '###', 'user_adress': '###'}

requests.post('http://84.201.140.28:8080/reg', json=data).text

If everything went well, will return id, else -1

Login:

data = {'user_name': '###', 'user_password': '###', 'user_email': '###'}

requests.post('http://84.201.140.28:8080/log', json=data).text

If everything went well, will return id, else -1

Get statistic:

data = {'user_id': ###}

requests.post('http://84.201.140.28:8080/stat', json=data).text

return [] or full statistics

Add data:

data = {'user_id': ###, 'date': ###, 'value': ###}

requests.post('http://84.201.140.28:8080/add', json=data).text

return 'wrong' or 'success'
