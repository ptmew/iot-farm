<?php
header("Access-Control-Allow-Origin: *");
#UserInfo
$username = "pawee"; 
$password = "CIEkmitl2020$";   
$host = "localhost";
$database="cie_db";

#Establish a connection    
$mysqli = new mysqli("localhost", $username, $password, $database);
if ($mysqli->connect_error) {
    die("Connection failed: " . $cmysqli->connect_error);
}

#query
$name = $_GET['name']; 
$humid = $_GET['humid'] ?: "NULL"; 
$temp = $_GET['temp'] ?: "NULL"; 
$ph = $_GET['ph'] ?: "NULL";
$ec = $_GET['ec'] ?: "NULL";
$o2 = $_GET['o2'] ?: "NULL";

$test = "INSERT INTO PLANT_STATUS (NAME, HUMID, TEMP, PH, EC, O2)
VALUES ({$name}, {$humid}, {$temp}, {$ph}, {$ec}, {$o2} )";

$result = $mysqli->query($test);

#Get the result by row and add to array called data 
if ($result === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error";
}

#Free the Allocation space     
$result->free();
$mysqli->close();
?>
