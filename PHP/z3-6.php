<!DOCTYPE html>
<html>
<head>
    <title>Lab2.5</title>
</head>
<body>
    <?php
        $cust = array(
            'cnum' => 2001,
            'cname' => "Hoffman",
            'city' => "London",
            'snum' => 1001,
            'rating' => 100
        );

        print "cust: <br>";    
        foreach ($cust as $key=>$value) {
            print "$key => $value <br>";
        }

        asort($cust);
        print "<br> cust asort: <br>";    
        foreach ($cust as $key=>$value) {
            print "$key => $value <br>";
        }

        
        ksort($cust);
        print "<br> cust ksort: <br>";    
        foreach ($cust as $key=>$value) {
            print "$key => $value <br>";
        }

        sort($cust);
        print "<br> JUST SORT: <br>";    
        foreach ($cust as $key=>$value) {
            print "$key => $value <br>";
        }
    ?>
</body>
</html>