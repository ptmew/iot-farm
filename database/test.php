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
$query = $_GET['query']; 
$result = $mysqli->query($query);

#Get the result by row and add to array called data 
$data = array();
while ($row = $result->fetch_assoc()) {
	$data[] = $row;
}   

#Change to JSON format
echo json_encode($data);     

#Free the Allocation space     
$result->free();
?>
