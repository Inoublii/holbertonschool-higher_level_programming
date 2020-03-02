--  converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- You need to convert all of the following to UTF8:

ALTER DATABASE hbtn_0c_0 SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table FROM hbtn_0c_0 SET utf8mb4 COLLATE utf8mb4_unicode_ci;
