# The AirBnB clone

![Screenshot 2023-06-29 at 1 46 26 PM](https://github.com/Natiman58/my_airbnb_v4/assets/99422296/942d1d64-dd18-44d6-968c-b462d2915446)
# [Demo video](https://drive.google.com/file/d/1K0qgJUdL03IgYvXO5Yu-CX7JthJYwTZb/view?usp=sharing)

Step-1: Clone the repo
      
      run the scripts on different terminals:
            
            terminal-1 ./101-hbnb_script.sh  # starts the front-end on route /101-hbnb
            terminal-2 ./api-run_script.sh   # starts the api-server
      
Step-2: then go to the [link](http://127.0.0.1:5000/101-hbnb) to see the page

Setp-3: you can test the apis on http://127.0.0.1:5001/api/v1/users and the other endpoints mentioned below; RESTFul API section

then you are all set 👍.

# About the console

* The shell works in an interactive mode:


      $ ./console.py
      (hbnb) help
      
      Documented commands (type help <topic>):
      ========================================
      EOF  help  quit
      
      (hbnb) 
      (hbnb) 
      (hbnb) quit
      $
* and also in non-interactive mode

       $ echo "help" | ./console.py
      (hbnb)
      
      Documented commands (type help <topic>):
      ========================================
      EOF  help  quit
      (hbnb) 
      $
      $ cat test_help
      help
      $
      $ cat test_help | ./console.py
      (hbnb)
      
      Documented commands (type help <topic>):
      ========================================
      EOF  help  quit
      (hbnb) 
      $

* Built commands

      bash-3.2$ ./console.py
      (hbnb) help
      
      Documented commands (type help <topic>):
      ========================================
      Amenity  EOF    Review  User  create   help  show  
      City     Place  State   all   destroy  quit  update

* Usage:

      (hbnb) all State:
      [[State] (6e5a3591-ecc6-4fec-a4f7-2f5c4a4e4957) {'id': '6e5a3591-ecc6-4fec-a4f7-2f5c4a4e4957', 'created_at':
      datetime.datetime(2023, 6, 10, 16, 50, 45), 'updated_at': datetime.datetime(2023, 6, 10, 16, 50, 45)}]

      (hbnb) create User
      cf2b4aac-da77-40e8-b541-d668ffc0930f

      (hbnb) all User
      [[User] (cf2b4aac-da77-40e8-b541-d668ffc0930f) {'id': 'cf2b4aac-da77-40e8-b541-d668ffc0930f', 'created_at':
      datetime.datetime(2023, 6, 29, 13, 58, 14), 'updated_at': datetime.datetime(2023, 6, 29, 13, 58, 14)}]

      (hbnb) show User:
  
      ** instance id missing **

      (hbnb) create User:
  
      8444f7b2-6356-4972-9e1c-bf6766e1177f

      (hbnb) all User:
  
      [[User] (cf2b4aac-da77-40e8-b541-d668ffc0930f) {'id': 'cf2b4aac-da77-40e8-b541-d668ffc0930f', 'created_at':
      datetime.datetime(2023, 6, 29, 13, 58, 14), 'updated_at': datetime.datetime(2023, 6, 29, 13, 58, 14)}, [User] (8444f7b2-
      6356-4972-9e1c-bf6766e1177f) {'id': '8444f7b2-6356-4972-9e1c-bf6766e1177f', 'created_at': datetime.datetime(2023, 6, 29,
      14, 0, 26), 'updated_at': datetime.datetime(2023, 6, 29, 14, 0, 26)}]
      (hbnb)

      (hbnb) show User 8444f7b2-6356-4972-9e1c-bf6766e1177f
      [User] (8444f7b2-6356-4972-9e1c-bf6766e1177f) {'id': '8444f7b2-6356-4972-9e1c-bf6766e1177f', 'created_at':
      datetime.datetime(2023, 6, 29, 14, 0, 26,
      929221), 'updated_at': datetime.datetime(2023, 6, 29, 14, 0, 26, 929281), 'password': '74be16979710d4c4e7c6647856088456'}
  
      (hbnb) all
      [[State] (6e5a3591-ecc6-4fec-a4f7-2f5c4a4e4957) {'id': '6e5a3591-ecc6-4fec-a4f7-2f5c4a4e4957', 'created_at':
      datetime.datetime(2023, 6, 10, 16, 50, 45), 'updated_at': datetime.datetime(2023, 6, 10, 16, 50, 45)}, [Review]
      (ae20e2d2-ad77-440e-9945-57efc9bca531) {'id': 'ae20e2d2-ad77-440e-9945-57efc9bca531', 'created_at':
      datetime.datetime(2023, 6, 10, 16, 50, 49), 'updated_at': datetime.datetime(2023, 6, 10, 16, 50, 49)}, [Place] (a7c32fc5-
      bfe6-44cc-9d28-a274bc59b544) {'id': 'a7c32fc5-bfe6-44cc-9d28-a274bc59b544', 'created_at': datetime.datetime(2023, 6, 19, 12, 40, 15),
      'updated_at': datetime.datetime(2023, 6, 19, 12, 40, 15)}, [User] (cf2b4aac-da77-40e8-b541-d668ffc0930f) {'id': 'cf2b4aac-da77-40e8-b541-d668ffc0930f',
      'created_at': datetime.datetime(2023, 6, 29, 13, 58, 14), 'updated_at': datetime.datetime(2023, 6, 29, 13, 58, 14)},
      [User] (8444f7b2-6356-4972-9e1c-bf6766e1177f) {'id': '8444f7b2-6356-4972-9e1c-bf6766e1177f', 'created_at': datetime.datetime(2023, 6, 29, 14, 0, 26),
      'updated_at': datetime.datetime(2023, 6, 29, 14, 0, 26)}]

      (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
      [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at':
      datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291),
      'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-
      57a17f1e4f88'}
      (hbnb)

      Update from strings

      (hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
             User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)

      (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
      [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at':
      datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055),
      'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-
      57a17f1e4f88'}
      (hbnb) 

      Update from dictionary:

      User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})

      (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
      [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at':
      datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143),
      'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
      (hbnb) 

 * Mysql interaction:

       State creation:
       (hbnb) echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost
       HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py

        (hbnb) echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost
       HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
        (hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 'id': '95a5abab-aa65-4861-9bc6-
       1da4a36069aa', 'updated_at': datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10,
       0, 49, 54)}]
        (hbnb)

       (hbnb) echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
        Enter password: 
        *************************** 1. row ***************************
                id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
        created_at: 2017-11-10 00:49:54
        updated_at: 2017-11-10 00:49:54
              name: California

       City creation:
       (hbnb) echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"'
       |HBNB_MYSQL_USER=hbnb_dev
       HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
       (hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b

       (hbnb) echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost
       HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
       (hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'updated_at':
       datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'name': 'San 
       Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)]
       (hbnb)

       (hbnb) echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
        Enter password: 
        *************************** 1. row ***************************
                id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
        created_at: 2017-11-10 00:52:53
        updated_at: 2017-11-10 00:52:53
              name: San Francisco
          state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
        *************************** 2. row ***************************
                id: a7db3cdc-30e0-4d80-ad8c-679fe45343ba
        created_at: 2017-11-10 00:53:19
        updated_at: 2017-11-10 00:53:19
              name: San Jose
          state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa

        echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost
       HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 

        (hbnb) [[User] (4f3f4b42-a4c3-4c20-a492-efff10d00c0b) {'updated_at': datetime.datetime(2017, 11, 10, 1, 17, 26),
        'id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'last_name': 'Snow', 'first_name': 'Guillaume', 'email': 'gui@hbtn.io',         'created_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'password': 'f4ce007d8e84e0910fbdd7a06fa1692d'}]
        (hbnb)

        (hbnb) echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
        Enter password: 
        *************************** 1. row ***************************
                id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
        created_at: 2017-11-10 01:17:26
        updated_at: 2017-11-10 01:17:26
             email: gui@hbtn.io
          password: guipwd
        first_name: Guillaume
         last_name: Snow

       (hbnb)echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
        Enter password: 
        *************************** 1. row ***************************
                      id: ed72aa02-3286-4891-acbc-9d9fc80a1103
              created_at: 2017-11-10 01:22:30
              updated_at: 2017-11-10 01:22:30
                 city_id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
                 user_id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
                    name: "Lovely place"
             description: NULL
            number_rooms: 3
        number_bathrooms: 1
               max_guest: 6
          price_by_night: 120
                latitude: 37.774
               longitude: -122.431

       (hbnb) echo 'SELECT * FROM reviews\G' | mysql -uhbnb_dev -p hbnb_dev_db
        Enter password: 
        *************************** 1. row ***************************
                id: f2616ff2-f723-4d67-85dc-f050a38e0f2f
        created_at: 2017-11-10 04:06:25
        updated_at: 2017-11-10 04:06:25
              text: Amazing place, huge kitchen
          place_id: ed72aa02-3286-4891-acbc-9d9fc80a1103
           user_id: d93638d9-8233-4124-8f4e-17786592908b

         (hbnb) echo 'SELECT * FROM amenities\G' | mysql -uhbnb_dev -p hbnb_dev_db
         *************************** 2676. row ***************************
        place_id: 598218ba-5069-450d-afe1-1e3212c378d4
        amenity_id: f7c854a4-f565-4aa5-8542-c4e17c498ef1
        *************************** 2677. row ***************************
          place_id: 60b77ea7-04c9-4b8a-b835-dc92c6aa196b
        amenity_id: f7c854a4-f565-4aa5-8542-c4e17c498ef1

* RESTFul API:

        * To check the status:
        -> Terminal 1 start the api server
        (hbnb) HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db
        HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app

        -> Terminal 2
        curl -X GET http://0.0.0.0:5000/api/v1/status
        {
          "status": "OK"
        }

        * Endpoints:
  
            For User Obj:
               curl -X GET http://0.0.0.0:5000/api/v1/users
               curl -X GET http://0.0.0.0:5000/api/v1/users/<user_id>
               curl -X DELETE http://0.0.0.0:5000/api/v1/users/<user_id>
               curl -X PUT http://0.0.0.0:5000/api/v1/users/<user_id>
               curl -X POST http://0.0.0.0:5000/api/v1/users
    
            For State Obj:
              curl -X GET http://0.0.0.0:5000/api/v1/states
              curl -X GET http://0.0.0.0:5000/api/v1/states/state_id
              curl -X DELETE http://0.0.0.0:5000/api/v1/states/state_id
              curl -X POST http://0.0.0.0:5000/api/v1/states
              curl -X PUT http://0.0.0.0:5000/api/v1/states/state_id
    
            For Place Obj:
              curl -X GET http://0.0.0.0:5000/api/v1/cities/city_id/places
              curl -X GET http://0.0.0.0:5000/api/v1/places/place_id
              curl -X POST http://0.0.0.0:5000/api/v1/places_search
              curl -X DELETE http://0.0.0.0:5000/api/v1/places/place_id
              curl -X POST http://0.0.0.0:5000/api/v1/cities/city_id/places
              curl -X PUT http://0.0.0.0:5000/api/v1/places/place_id
    
            For places_reviews obj:
              curl -X GET http://0.0.0.0:5000/api/v1/places/place_id/reviews
              curl -X GET http://0.0.0.0:5000/api/v1/reviews/review_id
              curl -X DELETE http://0.0.0.0:5000/api/v1/reviews/review_id
              curl -X POST http://0.0.0.0:5000/api/v1/places/place_id/reviews
              curl -X PUT http://0.0.0.0:5000/api/v1/reviews/review_id
    
            For places_amenities Obj:
              curl -X GET http://0.0.0.0:5000/api/v1/places/place_id/amenities
              curl -X DELETE http://0.0.0.0:5000/api/v1/places/place_id/amenities/amenity_id
              curl -X POST http://0.0.0.0:5000/api/v1/places/place_id/amenities/amenity_id

            For City Obj:
              curl -X GET http://0.0.0.0:5000/api/v1/states/state_id/cities
              curl -X GET http://0.0.0.0:5000/api/v1/cities/city_id
              curl -X DELETE http://0.0.0.0:5000/api/v1/cities/city_id
              curl -X POST http://0.0.0.0:5000/api/v1/states/state_id/cities
              curl -X PUT http://0.0.0.0:5000/api/v1/cities/city_id

            For Amenity Obj:
              curl -X GET http://0.0.0.0:5000/api/v1/amenities
              curl -X GET http://0.0.0.0:5000/api/v1/amenities/amenity_id
              curl -X DELETE http://0.0.0.0:5000/api/v1/amenities/amenity_id
              curl -X POST http://0.0.0.0:5000/api/v1/amenities
              curl -X PUT http://0.0.0.0:5000/api/v1/amenities/amenity_id


# Enjoy 🧑‍💻🎉
