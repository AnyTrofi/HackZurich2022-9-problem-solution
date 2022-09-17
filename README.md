# HackZurich2022-9-problem
The project that our team presents in issue 9 at the HackZurich hackathon



BackEnd Part:

-First you need to download MySql

-Second you need create data base in terminal: mysql -u root -h -p

-Next you need to create a table in the database using the 'make_users_table' function from db.py

-And then you can run app.py and use the API

Work with backend:

Registration:

  data = {'user_name': '###', 'user_password': '###', 'user_email': '###', 'user_adress': '###'}
  
  requests.post('http://127.0.0.1:5000/reg', json=data).text 
  
  If everything went well, will return id, else -1
  
Login:

  data = {'user_name': '###', 'user_password': '###', 'user_email': '###'}
  
  requests.post('http://127.0.0.1:5000/log', json=data).text 
  
  If everything went well, will return id, else -1
 
Get statistic:
  
  data = {'user_id': ###}
  
  requests.post('http://127.0.0.1:5000/stat', json=data).text 
  
  return [] or full statistics
  
Add data:
  
  data = {'user_id': ###, 'date': ###, 'value': ###}
  
  requests.post('http://127.0.0.1:5000/add', json=data).text 
  
  return 'wrong' or 'success'
 
