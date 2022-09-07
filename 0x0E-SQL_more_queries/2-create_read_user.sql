-- a script that creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH auth_socket BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* to 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
