<?php require_once('connect2db/connect2db.php'); ?>
<?php
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
  $MM_redirectLoginFailed = "history.php";
  $MM_redirecttoReferrer = false;
  mysql_select_db($database_241, $FRA);
  
  $search_query=sprintf("SELECT stid FROM history WHERE stid=%s",
    GetSQLValueString($studentID, "text")); 
   
  $search_RS = mysql_query($search_query, $FRA) or die(mysql_error());
  $FoundUser = mysql_num_rows($search_RS);
  if ($FoundUser) {
	if (PHP_VERSION >= 5.1) {session_regenerate_id(true);} else {session_regenerate_id();}
    $_SESSION['MM_stid'] = $studentID;	      
	
	if (isset($_SESSION['PrevUrl']) && false) {
      $MM_redirectLoginSuccess = $_SESSION['PrevUrl'];	
    }
	
    header("Location: " . $MM_redirectLoginSuccess );
  }
  else {
	  echo '<script type="text/javascript">if (window.confirm("ผู้ใช้งานดังกล่าวยังไม่ได้ใช้งานเครื่อง หรือ ไม่พบผู้ใช้งานดังกล่าวค่ะ"))
{location.href="history.php";}else{location.href="index.php";}</script>';
	  //echo '<script type="text/javascript">alert("ผู้ใช้งานดังกล่าวยังไม่ได้ใช้งานเครื่อง หรือ ไม่พบผู้ใช้งานดังกล่าวค่ะ");</script>';
      //header("Location: ". $MM_redirectLoginFailed );
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
<script>
function checkSubmit(){
	if(document.searchbox.stid.value == ""){
		alert('กรุณากรอกรหัสนักศึกษาของผู้ที่ต้องการเช็คประวัติการใช้งานด้วยครับ/ค่ะ');
		document.searchbox.stid.focus();
		return false;
	}
	document.searchbox.submit();
}
</script>
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

<form name="searchbox" method="POST" action="<?php echo $FormAction; ?>" onsubmit="JavaScript:return checkSubmit()">
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
<script src="js/bootstrap.min.js"></script>
</body>
</html>
