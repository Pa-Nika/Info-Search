<!DOCTYPE html>
<html> 
    <head>
        <title>Listing 10-1. Simple HTML Form</title>
        <meta charset="UTF-8">
    </head> 
    <body>
        <?php
            function get_right_answers_num($correctAnswers, $userAnswers) {
                $result = 0;
                for ($i = 0; $i < 9; ++$i) {
                    if ($correctAnswers[$i] == $userAnswers[$i]) {
                        $result += 1;
                    }
                }

                return $result;
            }

            function get_result_text_based_on_right_answers_num($name, $rightAnswersNum) {
                switch ($rightAnswersNum) {
                    case 9:
                        $resultText = ", you have excellent knowledge of geography";
                        break;
                    case 8:
                        $resultText = ", you have good knowledge of geography";
                        break;
                    case 7:
                        $resultText = ", you have very good knowledge of geography";
                        break;
                    case 6:
                        $resultText = " you have good knowledge of geography";
                        break;
                    case 5:
                        $resultText = " you have satisfactory knowledge of geography";
                        break;
                    case 4:
                        $resultText = " you have fair knowledge of geography";
                        break;
                    case 3:
                        $resultText = " you have poor knowledge of geography";
                        break;
                    case 2:
                        $resultText = " you have very poor knowledge of geography";
                        break;
                    default: 
                        $resultText = " you don't know geography at all";
                }

                return $name . $resultText;
            }

            $correctAnswers = array("6", "9", "4", "1", "3", "2", "5", "8", "7");
            $userAnswers = $_POST["answers"];
            $name = $_POST["user"];

            $rightAnswersNum = get_right_answers_num($correctAnswers, $userAnswers);
            $resultText = get_result_text_based_on_right_answers_num($name, $rightAnswersNum);

            print "<p align='center'>$resultText";
            print "<p align='center'><a href='z4-3a.html'>back</a>";
        ?>
    </body> 
</html>
