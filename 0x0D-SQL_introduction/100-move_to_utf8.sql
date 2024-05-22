-- script that converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4;
ALTER TABLE hbtn_0c_0.second_table CONVERT TO CHARACTER SET utf8mb4;
ALTER TABLE hbtn_0c_0.second_table MODIFY name TEXT CHARACTER SET utf8mb4;
