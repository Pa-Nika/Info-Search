<!DOCTYPE html>
<html> 
<head>
    <meta charset="UTF-8">
    <title>Lab 4.3</title> 
</head> 
<body>
    <form action="ls10-5.php" method="post">
        <p>Enter your name:</p>
        <p><input type="text" name="user"></p>
        <p>What do you like to do in your free time? <br></p>
        <p><input type="checkbox" name="hobby[]" value="listen to music">Listen to music</p>
        <p><input type="checkbox" name="hobby[]" value="read a book">Read a book</p>
        <p><input type="checkbox" name="hobby[]" value="watch TV">Watch TV</p>
        <p><input type="checkbox" name="hobby[]" value="go for a walk">Go for a walk</p>
        <p><input type="submit" value="Choice made"></p>
    </form>
</body> 
</html>
