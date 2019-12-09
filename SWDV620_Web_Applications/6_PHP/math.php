<!DOCTYPE html>
<html>
    <head>
        <title>Basic Math Operations</title>

        <script type="text/javascript">
            function checkInput(event) {
                const numberOne = event.target[0].value,
                    numberTwo = event.target[2].value,
                    operation = event.target[1].value;
                let grtThanZero = true;

                switch(operation) {
                    case 'addition':
                        grtThanZero = numberOne + numberTwo >= 0;
                        break;
                    case 'subtraction':
                        grtThanZero = numberOne - numberTwo >= 0;
                        break;
                    case 'division':
                        grtThanZero = numberOne / numberTwo >= 0;
                        break;
                    case 'multiplication':
                        grtThanZero = numberOne * numberTwo >= 0;
                        break;
                }

                if (!grtThanZero) {
                    event.preventDefault();
                    alert('Your calculated result was less than 0!')
                }
            }
        </script>
    </head>
    <body>
        <h1>Basic Math Operations</h1>
        <p>The result of the operation must be greater than 0.</p>

        <form action="./results.php" method="get" onsubmit="checkInput(event)">

            <input type="number" name="number_one" autofocus required />
            <select name="operation">
                <option name="addition" value="addition">+</option>
                <option name="subtraction" value="subtraction">-</option>
                <option name="multiplication" value="multiplication">*</option>
                <option name="division" value="division">/</option>
            </select>
            <input type="number" name="number_two" required />
            <input type="submit" value="Calculate" />

        </form>
    </body>
</html>