**CONSTRAINTS**
1. Enter the tip as a percentage. For example, a 15% tip would be entered as 15, not 0.15. Your program should handle the division.
2. Round fractions of a cent up to the next cent.

If you can’t figure out how to enforce these constraints, write the program without them and come back to it later. The point of these exercises is to practice and improve.

**Additional Challenges**
When you’ve finished writing the basic version of the program, try tackling some additional challenges:

* Ensure that the user can enter only numbers for the bill amount and the tip rate. If the user enters non-numeric values, display an appropriate message and exit the program. Here’s a test plan as an example:
​ 	
```
Input:
​ 	
  bill amount: abcd
​ 	
  tip rate: 15
​ 	
Expected result: Please enter a valid number for the bill amount.
```

* Instead of displaying an error message and exiting the program, keep asking the user for correct input until it is provided.
* Don’t allow the user to enter a negative number.
* Break the program into functions that do the computations.
* Implement this program as a GUI program that automatically updates the values when any value changes.
* Instead of the user entering the value of the tip as a percentage, have the user drag a slider that rates satisfaction with the server, using a range between 5% and 20%.
