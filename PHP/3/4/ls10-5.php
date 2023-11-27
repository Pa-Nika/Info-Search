<!DOCTYPE html>
<html> 
<head>
    <meta charset="UTF-8">
    <title>lab</title> 
</head> 
<body>
    <?php
        foreach ($_POST as $key=>$value) {
            print "$key = $value<br>\n";
        }
    ?>
 </body> 
 </html>