<?php
  $email = $_POST['email'];
  $file = 'emails.txt';
  
  // Open the file in append mode
  $handle = fopen($file, 'a');
  
  // Append the email address to the file
  fwrite($handle, $email . "\n");
  
  // Close the file
  fclose($handle);
  
  echo 'Email address saved successfully!';
?>
