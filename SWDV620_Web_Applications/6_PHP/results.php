<!DOCTYPE html>
<html>
    <head>
        <title>Math Operations Results</title>

        <style>
            img {
                max-width: 200px;
            }
        </style>
    </head>
    <body>
        <h1>Results:</h1>

        <?php
            $values = array('operation', 'number_one', 'number_two');

            for ($i = 0; $i < count($values); $i++) {
                echo '<p>' . $values[$i] . ': <span id="operation">' . $_GET[$values[$i]] . '</span></p>';
            }

            $operation = $_GET['operation'];
            $result = 0;

            switch ($operation) {
                case 'addition': 
                    $result = $_GET['number_one'] + $_GET['number_two'];
                    break;
                case 'subtraction':
                    $result = $_GET['number_one'] - $_GET['number_two'];
                    break;
                case 'multiplication':
                    $result = $_GET['number_one'] * $_GET['number_two'];
                    break;
                case 'division':
                    $result = $_GET['number_one'] / $_GET['number_two'];
                    break;
            }

            echo '<p>Calculation Results: ' . $result . '</p>';

            echo '<img src="./' . $operation . '.jpg" />';
        ?>
    </body>
</html>