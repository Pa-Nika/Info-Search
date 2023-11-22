<!DOCTYPE html>
<html> <head>
<title> Lab2.3 </title>
</head> <body>

<?php
    $color = "gray";
    print "<table border=1 cellpadding=5px>\n";
    for ($y=1;  $y <= 10;  $y++)
        {
            print "<tr>\n";
        for ($x=1;  $x <= 10;  $x++)
            {
                if ($x == $y) {
                    print "\t<td bgcolor=\"$color\">";
                } else {
                    print "\t<td>";
                } 
                print ($x*$y);
                print "</td>\n";
            }
        print "</tr>\n";
        }
    print "</table>";

?>
</body> </html>