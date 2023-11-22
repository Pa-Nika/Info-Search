<!DOCTYPE html>
<html> <head>
<title> Lab2.2 </title> </head> <body> 

<?php 
    $lang = isset($_GET['lang']) ? $_GET['lang'] : '';

    if ($lang == "ru") {
        print "Russian";
    } elseif ($lang == "en") {
        print "English";
    } elseif ($lang == "fr") {
        print "French";
    } elseif ($lang == "de") {
        print "Deutch";
    } else {
        print "Yooops! I don't know!";
    }

?>
</body> </html>