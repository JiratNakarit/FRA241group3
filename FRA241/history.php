<?php require_once('connect2db/connect2db.php'); ?>
<?php
// *** Validate request to login to this site.
if (!isset($_SESSION)) {
  session_start();
}

if (!function_exists("GetSQLValueString")) {
	function GetSQLValueString($theValue, $theType, $theDefinedValue = "", $theNotDefinedValue = "") {
		if (PHP_VERSION < 6) {
			$theValue = get_magic_quotes_gpc() ? stripslashes($theValue) : $theValue;
		}
		$theValue = function_exists("mysql_real_escape_string") ? mysql_real_escape_string($theValue) : mysql_escape_string($theValue);
		switch ($theType) {
			case "text":
				$theValue = ($theValue != "") ? "'" . $theValue . "'" : "NULL";
				break;    
			case "long":
			case "int":
				$theValue = ($theValue != "") ? intval($theValue) : "NULL";
			break;
			case "double":
				$theValue = ($theValue != "") ? doubleval($theValue) : "NULL";
				break;
			case "date":
				$theValue = ($theValue != "") ? "'" . $theValue . "'" : "NULL";
				break;
			case "defined":
				$theValue = ($theValue != "") ? $theDefinedValue : $theNotDefinedValue;
				break;
		}
		return $theValue;
	}
}

$FormAction = $_SERVER['PHP_SELF'];
if (isset($_GET['accesscheck'])) {
  $_SESSION['PrevUrl'] = $_GET['accesscheck'];
}

if (isset($_POST['stid'])) {
  $studentID=$_POST['stid'];
  $MM_redirectLoginSuccess = "showhis.php";
  $MM_redirectLoginFailed = "index.php";
  $MM_redirecttoReferrer = false;
  mysql_select_db($database_241, $FRA);
  
  $search_query=sprintf("SELECT stid FROM history WHERE stid=%s",
    GetSQLValueString($studentID, "text")); 
   
  $search_RS = mysql_query($search_query, $FRA) or die(mysql_error());
  $FoundUser = mysql_num_rows($search_RS);
  if ($FoundUser) {
	if (PHP_VERSION >= 5.1) {session_regenerate_id(true);} else {session_regenerate_id();}
    //declare two session variables and assign them
    $_SESSION['MM_stid'] = $studentID;	      
	
	if (isset($_SESSION['PrevUrl']) && false) {
      $MM_redirectLoginSuccess = $_SESSION['PrevUrl'];	
    }
	
    header("Location: " . $MM_redirectLoginSuccess );
  }
  else {
    header("Location: ". $MM_redirectLoginFailed );
  }
}
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

<form name="searchbox" method="POST" ACTION="<?php echo $FormAction; ?>">
	<table width="1000" border="0">
		<tr>
			<th align="center">กรุณาระบุรหัสนักศึกษา</th>
		</tr>
		<tr>
			<td><input name="stid" type="text" id="stid"></td>
		</tr>
		<tr>
			<td><input type="submit" value="ค้นหา"></td>
		</tr>
	</table>
</form>
</center>
<br>

<script src="js/bootstrap.min.js"></script>
</body>
</html>
