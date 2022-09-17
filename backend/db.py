import pymysqlfrom config import host, user, password, db_namedef add_user_to_bd(user_name, user_password, user_email, user_adress):    try:        # connect to bd        connection = pymysql.connect(            host=host,            port=3306,            user=user,            password=password,            database=db_name,            cursorclass=pymysql.cursors.DictCursor        )        try:            with connection.cursor() as cursor:                # Add user to table 'users'                insert_query = f"INSERT INTO `users` (name, password, email, adress) VALUES ('{user_name}', '{user_password}', '{user_email}', '{user_adress}');"                cursor.execute(insert_query)                connection.commit()            with connection.cursor() as cursor:                # Check last id in table                select_all_rows = "SELECT * FROM `users`"                cursor.execute(select_all_rows)                rows = cursor.fetchall()                last_index = int(rows[-1]['id'])            with connection.cursor() as cursor:                # Create user table with him data                create_table_query = f"CREATE TABLE id{last_index}(date varchar(32), value varchar(32));"                cursor.execute(create_table_query)        finally:            # close connect            connection.close()    except Exception as ex:        print("Connection refused...")        print(ex)    return last_indexdef log_user(user_email, user_password):    try:        result = -1        # connect to bd        connection = pymysql.connect(            host=host,            port=3306,            user=user,            password=password,            database=db_name,            cursorclass=pymysql.cursors.DictCursor        )        try:            with connection.cursor() as cursor:                select_all_rows = "SELECT * FROM `users`"                cursor.execute(select_all_rows)                rows = cursor.fetchall()                for row in rows:                    if row['email'] == user_email and row['password'] == user_password:                        result = row['id']        finally:            # close connect            connection.close()    except Exception as ex:        print("Connection refused...")        print(ex)    return resultdef check_statistic(user_id):    try:        rows = []        # connect to bd        connection = pymysql.connect(            host=host,            port=3306,            user=user,            password=password,            database=db_name,            cursorclass=pymysql.cursors.DictCursor        )        try:            with connection.cursor() as cursor:                select_all_rows = f"SELECT * FROM `id{user_id}`"                cursor.execute(select_all_rows)                rows = cursor.fetchall()                result = rows        finally:            # close connect            connection.close()    except Exception as ex:        print("Connection refused...")        print(ex)    return rowsdef add_user_data(user_id, date, value):    result = 'Wrong'    try:        # connect to bd        connection = pymysql.connect(            host=host,            port=3306,            user=user,            password=password,            database=db_name,            cursorclass=pymysql.cursors.DictCursor        )        try:            with connection.cursor() as cursor:                # Add user to table 'users'                insert_query = f"INSERT INTO `id{user_id}` (date, value) VALUES ('{date}', '{value}');"                cursor.execute(insert_query)                connection.commit()                result = 'Success'        finally:            # close connect            connection.close()    except Exception as ex:        print("Connection refused...")        print(ex)    return resultdef make_users_table():    try:        connection = pymysql.connect(            host=host,            port=3306,            user=user,            password=password,            database=db_name,            cursorclass=pymysql.cursors.DictCursor        )        print("successfully connected...")        print("#" * 20)        try:            with connection.cursor() as cursor:                create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \                                " name varchar(64)," \                                " password varchar(32)," \                                " email varchar(64)," \                                " adress text, PRIMARY KEY (id));"                cursor.execute(create_table_query)                print("Table created successfully")        finally:            connection.close()    except Exception as ex:        print("Connection refused...")        print(ex)