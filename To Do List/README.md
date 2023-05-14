This project involved creating a simple to do list.

You can view the [project demonstration video](https://www.youtube.com/watch?v=0W6AUUagnMU&list=PLBlf9mIHOKqO5mws-3M7DXh0nsVOzxP9S) to get an idea of how it works or follow the steps below to run it on your own computer.

## Steps to Run

1. Download the files from my repository and place them in a single folder:

2. Install "virtualenv":
```
pip install virtualenv
```

3. Open a terminal in the root directory and run:
```
virtualenv env
```

4. If on windows run this command in the terminal:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

5. Run this command:
```
env\Scripts\activate
```

6. Install the dependencies:
```
pip install -r requirements.txt
```

7. Create the database
```
python
from app import app, db
app.app_context().push()
db.create_all()
```

8. Run app.py

9. View the program at "http://127.0.0.1:5000/"



