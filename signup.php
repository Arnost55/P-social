<?php
// FILEPATH: /C:/Users/Lívia Beniánová/Desktop/web P/P-social/signup.php

// Database connection details
$servername = "87.197.120.146";
$username = "psocial";
$password = "arnika123123";
$dbname = "p";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get user input from form
$name = $_POST['name'];
$email = $_POST['email'];
$password = $_POST['password'];

// Prepare and execute SQL statement
$stmt = $conn->prepare("INSERT INTO users (name, email, password) VALUES (?, ?, ?)");
$stmt->bind_param("sss", $name, $email, $password);
$stmt->execute();

// Check if the insertion was successful
if ($stmt->affected_rows > 0) {
    echo "Signup successful!";
} else {
    echo "Error: " . $stmt->error;
}

// Close statement and connection
$stmt->close();
$conn->close();
?>
