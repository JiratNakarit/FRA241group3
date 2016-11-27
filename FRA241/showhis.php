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
	src: url("http://localhost/jirat/font/KRR-THAISPIRIT.ttf");
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
	font-size: 40px;
}
h3 {
	color: #3366FF;
	font-family: KRR-THAISPIRIT;
	font-size: 20px;
}
</style>
    <link href="assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="../assets/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="assets/ico/apple-touch-icon-57-precomposed.png">
    <link rel="shortcut icon" href="assets/ico/favicon.png">

<link rel="stylesheet" href="css/jquery-ui.css">
<script src="js/jquery-1.10.2.js"></script>
<script src="js/jquery-ui.js"></script>
<script>
$(function() {
    $( "#datepicker" ).datepicker({dateFormat:'dd-mm-yy'});
  });
</script>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>

<body background="images/1180422460.gif">

  <?php
 
    $date = date("d-m-Y");
    $time = date("H:i");
    ?>

<center>
<table width="100%" border="0" bgcolor="#BEBEBE">
      <tr>
    <td width="240" height="34" align="left"><img src="images/fra241_logo.png" width="300" height="72"></td>
    <td width="753" align="center"><h2>ยินดีต้อนรับสู่เว็บไซต์เครื่องจำหน่ายวงจรรวมอัตโนมัติ</h2></td>
    <td width="329" align="center"><h3>&nbsp;วัน :: เวลา : <?php echo $date."&nbsp;/&nbsp;".$time;?></h3></td>
  </tr>
</table>
    <hr/>
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
		<td align="center"><?php echo $row_MA['datasheet']; ?></td>
	</tr>
<?php } while($row_MA = mysql_fetch_assoc($MA));?>
</table>
</center>
<br>

<script src="js/bootstrap.min.js"></script>
</body>
</html>
