<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $filename = $_POST['file'];
  $filename = str_replace('../', '', $filename);
  $filepath = 'payments/' . $filename;
  
  if (file_exists($filepath)) {
    echo '<pre>';
    include($filepath);
    echo '</pre>';
  } else {
	echo "File does not exist";
  }
}
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Компани худалдаж авах</title>

<style>
  body{
    background-color: black;
    color: #1affff;
    margin-top: 300px;
    text-align:center;
    font-size:20px;
    font-style:bold;
  }
</style>
</head>
<body>
  <form method="POST">
    <label for="payments.php">Payment code:</label><br><br>
    <input type="text" id="file" name="file">
    <input type="submit" value="Show">
  </form>
</body>
</html>
