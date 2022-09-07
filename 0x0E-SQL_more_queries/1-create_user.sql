-- creates MySQL server user 'user_0d_1'
-- user should have all the privileges
-- password should be set to 'user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH auth_socket BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
