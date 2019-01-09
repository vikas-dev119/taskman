# TaskMan

## setup on Linux machine
* Need to install on your system:
    - Python3.6
    - Mysql5

* The First directory is taskman, go inside directory using 
    - cd taskman/

* Create virtualenv and activate via using given command
    - virtualenv -p python3.6 venv
    - source venv/bin/activate
    
* Install all necessary depandencies
    - pip install -r requirment.txt

* create new database name as "db_taskman"
* Open taskman/app/app/settings.py file and change db credentials (according to your username/password)

* Apply migrations using given Commands:
    -  python manage.py makemigrations
    -  python manage.py migrate
 
* Run application 
    - python manage.py runserver

* Hit on browser http://localhost:8000


Note: I also attach task.pdf file.


