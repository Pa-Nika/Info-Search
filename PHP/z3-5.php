<!DOCTYPE html>
<html>
<head>
    <title>Lab2.5</title>
</head>
<body>
    <?php
        function print_arr($array) {
            foreach($array as $ind) {
                print "$ind  ";
            }
        }
        
        print("Treug: <br>");
        $treug = array();
        for ($n = 1; $n <= 10; $n++) {
            $treug[] = ($n * ($n + 1) / 2);
        }
        print_arr($treug);

        print" <br> Kvd: <br>";
        $kvd = array();
        for ($n = 1; $n <= 10; ++$n) {
            $kvd[] = $n * $n;
        }
        print_arr($kvd);

        print" <br> Rez: <br>";
        $rez = array_merge($treug, $kvd);
        print_arr($rez);

        print" <br> Rsort Rez: <br>";
        rsort($rez);
        print_arr($rez);

        print" <br> Shift Rez: <br>";
        array_shift($rez);
        print_arr($rez);

        print" <br> Unique Rez: <br>";
        $rez1 = array_unique($rez);
        print_arr($rez1);

    ?>
</body>
</html>