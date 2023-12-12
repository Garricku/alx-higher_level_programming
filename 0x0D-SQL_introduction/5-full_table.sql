-- prints the full description of the table first_table from database hbtn_0c_0
mysql -u Ricki -p -e "USE hbtn_0c_0; SELECT COLUMN_NAME, DATA_TYPE,
IS_NULLABLE, COLUMN_DEFAULT FROM INFORMATION_SCHEMA.COLUMNS WHERE
TABLE_NAME = 'first_table';"
