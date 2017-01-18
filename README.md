# shop-pyth.
This is for a shop management system with inventory and sales management
features in-built and carries an analytics platform.

### Setup
```SQL
create database shop;
use shop;
create user 'virtualrahul'@'localhost' identified by 'password'
grant all privileges on shop.* to 'virtualrahul'@'localhost';
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable
python manage.py runserver
```

#### Errors
* You might get error in createcachetable.
    * Comment out code in front/__init__py and re-run, then remove comments and
runserver

### Bug
* db_cache is used to maintain counters for ID generation in tables. The incr()
    method for cached value sale resets timer.

### TODO
* Make a landing page
* Beautify bill generation
* Make page for analytics purpose
