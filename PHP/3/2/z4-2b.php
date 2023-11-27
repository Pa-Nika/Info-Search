<!DOCTYPE html>
<html> 
    <head>
        <title> lab3.2 </title>
        <meta charset="UTF-8">
    </head> 
    <body>
        <?php
            if (!isset($_GET["align"])) {
                $align = "left";
            } else {
                $align = $_GET["align"];
            }

            if (!isset($_GET["valign"])) {
                $valign = "top";
            } else {
                $valign = $_GET["valign"];
            }

            print "<table border=\"1px\" width=\"100px\" height=\"100px\" text-align=\"$align\" align=\"center\">\n";
            print "<tr><td align=\"$align\" valign=\"$valign\">Text</td></tr></table>\n";
            print "<form action='{$_SERVER['PHP_SELF']}' method='get' align=\"center\">"
        ?>
            <p><b>Horizontal:</b></p>
            <p><input type="radio" name="align" value="left">Left</p>
            <p><input type="radio" name="align" value="center">Center</p>
            <p><input type="radio" name="align" value="right">Right</p>

            <p><b>Vertical:</b></p>
            <p><input type="checkbox" name="valign" value="top">Up</p>
            <p><input type="checkbox" name="valign" value="middle">Center</p>
            <p><input type="checkbox" name="valign" value="bottom">Down</p>
            <p><input type="submit" value="Submit"></p>
        </form>
    </body> 
</html>