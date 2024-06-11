# Marco Polo Python

## Lab Description:

In this lab, you will experiment with a Python function named marco() that is designed to respond "Polo!" when given the input "Marco" and respond "No!" to any other input. This mimics the classic children's game of Marco Polo. You'll call the function with different inputs and observe the output.

## Lab Steps:

1. Examine the provided Python code that defines the marco() function

2. Call marco() function in the Python interactive window, passing "Marco" as the input 

3. Observe the output

4. Call marco() again, this time passing your name as the input

5. Observe how the output changes based on the different input 

6. Experiment by calling marco() multiple times, each time passing a different input string

Reflection Questions:

1. What does the marco() function do?

2. What input will make it return "Polo!"?  

3. What input will make it return "No!"?

4. How could you modify the function to return a different response for inputs other than "Marco"?

5. What real-world problems does this map to with AWS Step Functions?

Challenge Questions:


1. Modify the marco() function to return "Let's play!" if the input is your name. Test it out.


2. Create a new function called hello() that returns "Hello" if no input is passed, and returns "Hello <input>!" if a name is passed.


3. Combine the marco() and hello() functions by calling hello() inside marco(). If the input to marco() is "Marco", have it call hello("Marco") to return the greeting.


4. Write a new function called game() with 2 parameters - name and game. Have it return "<name> wants to play <game>" where it inserts the parameter values.


5. Call your new game() function within the marco() function to return a message like "Marco wants to play Marco Polo!" when given the input "Marco". Get creative with other inputs!