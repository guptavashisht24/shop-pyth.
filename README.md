# shop-pyth.
Before using, it would br great[read MANDATORY] to execute following commands in your mysql!
create database shop;
use shop;
create user 'virtualrahul'@'localhost' identified by 'password'
grant all privileges on shop.* to 'virtualrahul'@'localhost';
 
                           OR
tweak the database settings in shop/settings.py accordingly, but be sure to run migrate!
