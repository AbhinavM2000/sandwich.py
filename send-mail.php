<?php
  $to = 'abnvm1@gmail.com,dhanusmala@gmail.com';
  $subject = 'Mailing list subscription';
  $message = 'A user has subscribed to the mailing list: ' . $_POST['email'];
  $headers = 'From: webmaster@correlationlab.com' . "\r\n" .
             'Reply-To: webmaster@correlationlab.com' . "\r\n" .
             'X-Mailer: PHP/' . phpversion();
  
  if (mail($to, $subject, $message, $headers)) {
    echo 'Email sent successfully!';
  } else {
    echo 'Error sending email';
  }
?>
