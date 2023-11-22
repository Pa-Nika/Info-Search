<!DOCTYPE html>
<html>
<head>
    <title>Lab2.4</title>
    <style>
        .red {
            color: red;
        }
        .blue {
            color: blue;
        }
        td, th {
            border: 1px solid black;
            padding: 5px;
            text-align: center;
        }
    </style>
</head>
<body>
    <table>
        <?php
        for ($y = 1; $y <= 10; $y++) {
            print "<tr>\n";
            for ($x = 1; $x <= 10; $x++) {
                if ($y == 1 && $x == 1) {
                    print "\t<td class=\"red\">";
                } else if ($y == 1 || $x == 1) {
                    print "\t<td class=\"blue\">";
                } else {
                    print "\t<td>";
                }
                
                if ($y == 1 && $x == 1) {
                    print"+";
                } else if ($x == 1 || $y == 1) {
                    print ($y == 1) ? ($x) : ($y);
                } else {
                    print ($x + $y);
                }
                print "</td>\n";
            }
            print "</tr>\n";
        }
        ?>
    </table>
</body>
</html>
