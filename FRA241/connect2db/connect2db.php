<?php
# FileName="Connection_php_mysql.htm"
# Type="MYSQL"
# HTTP="true"
$hostname_241 = "localhost";
$database_241 = "fra241";
$username_241 = "root";
$password_241 = "";
$FRA = mysql_pconnect($hostname_241, $username_241, $password_241) or trigger_error(mysql_error(),E_USER_ERROR);

mysql_query("SET NAMES UTF8");
?>