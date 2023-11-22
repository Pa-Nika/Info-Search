<!DOCTYPE html>
<html>
<head>
    <title>Lab2.5</title>
</head>
<body>

<?php

    function Ru($color) {
        print "<p style=\"color: $color;\">Здравствуйте!</p>";
    }

    function En($color) {
        print "<p style=\"color: $color;\">Hello!</p>";
    }

    function Fr($color) {
        print "<p style=\"color: $color;\">Bonjour!</p>";
    }

    function De($color) {
        print "<p style=\"color: $color;\">Guten Tag!</p>";
    }

    $lang = isset($_GET['lang']) ? $_GET['lang'] : 'Fr';
    $color = isset($_GET['color']) ? $_GET['color'] : 'black';

    if ($lang === 'Ru') {
        Ru($color);
    } elseif ($lang === 'En') {
        En($color);
    } elseif ($lang === 'Fr') {
        Fr($color);
    } elseif ($lang === 'De') {
        De($color);
    } else {
        echo "<p style=\"color: red;\">Yoooops!</p>";
    }

?>
</body>
</html>
<!-- z3-3.php?lang=De&color=red -->
<!-- z3-3.php?lang=Fr&color=green -->
