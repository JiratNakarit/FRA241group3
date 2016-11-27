<?php require_once('connect2db/connect2db.php'); ?>
<?php
if (!isset($_SESSION)) {
  session_start();
}

$maxRows_MA = 10;
$pageNum_MA = 0;
if (isset($_GET['pageNum_MA'])) {
  $pageNum_MA = $_GET['pageNum_MA'];
}
$startRow_MA = $pageNum_MA * $maxRows_MA;

mysql_select_db($database_241, $FRA);
$query_MA = "SELECT * FROM history WHERE stid LIKE '%".$_SESSION['MM_stid']."%'";
$query_limit_MA = sprintf("%s LIMIT %d, %d", $query_MA, $startRow_MA, $maxRows_MA);
$MA = mysql_query($query_limit_MA, $FRA) or die(mysql_error());
$row_MA = mysql_fetch_assoc($MA);

?>
<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="utf-8">
    <title>FRA241 :: Group 3</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="assets/css/bootstrap.css" rel="stylesheet">
<style type="text/css">
/* Sticky footer styles
      -------------------------------------------------- */

      html,  body {
	height: 100%;/* The html and body elements cannot have any padding or margin. */
      }
/* Wrapper for page content to push down footer */
      #wrap {
	min-height: 100%;
	height: auto !important;
	height: 100%;
	/* Negative indent footer by it's height */
        margin: 0 auto -60px;
}
/* Set the fixed height of the footer here */
      #push,  #footer {
	height: 60px;
}
#footer {
	background-color: #f5f5f5;
}

      /* Lastly, apply responsive CSS fixes as necessary */
      @media (max-width: 767px) {
 #footer {
 margin-left: -20px;
 margin-right: -20px;
 padding-left: 20px;
 padding-right: 20px;
}
}
/* Custom page CSS
      -------------------------------------------------- */
      /* Not required for template or sticky footer method. */

      #wrap > .container {
	padding-top: 60px;
}
@font-face {
	font-family: KRR-THAISPIRIT;
	src: url("font/KRR-THAISPIRIT.ttf") format("truetype");
}
.container .credit {
	margin: 20px 0;
}
code {
	font-size: 100%;
}
table {
    border-collapse: collapse;
    width: 1000
}

th, td {
    text-align: center;
	font-family: KRR-THAISPIRIT;
    padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

td {
	font-size: 18px;
}
th {
    background-color: #3366FF;
    color: white;
	font-size: 30px;
}
h2 {
	color: #3366FF;
	font-family: KRR-THAISPIRIT;
	font-size: 35px;
}
h3 {
	color: #3366FF;
	font-family: KRR-THAISPIRIT;
	font-size: 20px;
}
input[type=text], input[type=submit]{
	padding: 5px 10px;
	box-sizing: border-box;
	border-radius: 4px;
	border: 2px solid #3366ff;
	font-size: 16px;
	text-align: center;
	font-family: KRR-THAISPIRIT;
}
input[type=submit]{
	padding: 5px 10px;
	font-size: 25px;
}
</style>
    <link href="assets/css/bootstrap-responsive.css" rel="stylesheet">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="assets/ico/apple-touch-icon-57-precomposed.png">
    <link rel="shortcut icon" href="assets/ico/favicon.png">
	<link rel="stylesheet" href="css/jquery-ui.css">
	<script src="js/jquery-1.10.2.js"></script>
	<script src="js/jquery-ui.js"></script>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>

<body background="images/1180422460.gif">
<center>
<table width="100%" border="1" bgcolor="#BEBEBE" bordercolor="white">
	<tr>
		<td width="200" height="34" align="left"><a href="index.php"><img src="images/logo.png" width="100%"></a></td>
		<td width="600" align="center"><h2>ยินดีต้อนรับสู่เว็บไซต์เครื่องจำหน่ายวงจรรวมอัตโนมัติ</h2></td>
		<td width="200" align="center"><a href="history.php"><img src="images/his.png" width="100%" height="72"></a></td>
	</tr>
</table>
<p>&nbsp;</p>
<table width = "1000" border = "0">
	<tr>
		<th width="30%" align="center"><strong>รหัสนักศึกษา</strong></th>
		<th width="30%" align="center"><strong>รหัส IC</strong></th>
		<th width="20%" align="center"><strong>จำนวน</strong></th>
		<th width="20%" align="center"><strong>วันที่/เวลา</strong></th>
	</tr>
<?php do{?>
	<tr>
		<td align="center"><?php echo $row_MA['stid']; ?></td>
		<td align="center"><?php echo $row_MA['icid']; ?></td>
		<td align="center"><?php echo $row_MA['num']; ?></td>
		<td align="center"><?php echo $row_MA['date']; ?></td>
	</tr>
<?php } while($row_MA = mysql_fetch_assoc($MA));?>
</table>
</center>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
