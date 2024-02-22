### Password Generator with Python

##### Instructions
The program will ask:

1. How many letters would you like in your password?

2. How many symbols would you like?

3. How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password. 
- My knowledge about Python lists and loops was used to complete this project.

#### Easy Level Generator
I generated the password in sequence. If the user wants:
- 4 letters (fgdx), 
- 2 symbols ($*), and;
- 3 numbers (924).
then the password might look like this:
"fgdx$*924"

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. That's why I labelled it the "easy level generator"

#### Hard Level Generator
In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

"x$d24g*f9"
And every time a new password is being generated, the positions of the symbols, numbers, and letters are different.
".shuffle()" helped is scattering the position of the generated password.
