
# E02a-Control-Structures

- Open main01.py. Before running it, what do you expect this program to do?
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
   It greets me, then asks for "my" favorite color. I responded with purple, then the program stopped.
  - What do you think the program did with what you typed in answer to the question? 
   It likely stored my answer to be used for a later purpose.
- Open main02.py. Before running it, describe how this is different than main01.py. 
It includes the variable of color this time around. It also includes a line that will print the aforementioned variable.
  - What do you think the color = input() will do? 
  Define the variable "color" to be whatever the user inputs.
  - Run the program in the terminal and answer the question. Did the program do what you expected? Yes.
- Open main03.py. Before running it, describe how this is different than main02.py.
This time around, an if/else statement is in place and a correct and incorrect message are present.
  - What is happening on lines 9–12?
An if/else statement that will determine what a correct and incorrect answer will be.
  - Why are lines 10 and 12 indented?
To make sure they fall in line with the if/else statement rather than definining if and then as separate variables.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
It says that your answer is incorrect.
  - What does this tell you about "color"?
It's a case sensitive variable, requiring proper capitalization.
- Open main04.py. Before running it, describe how this is different than main03.py.
It includes an additional section in the line defining red as the correct answer.
  - What problem is this trying to solve?
The issue of case sensitivity and required capitalization.
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
Says that the answer is incorrect, showing us that this is still case sensitive to a degree. 
- Open main05.py. What do you expect line 9 to do?
Allow for any capitalization of red to still appear as correct.
  - What problem is it trying to solve?
Case sensitivity still persisting.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
Continues to see the input as incorrect.
 - Open main06.py. How is line 9 different than in main05.py?
Includes a section of code on top of the correct answer definer, labeled as ".strip"
   - What would you guess .strip() is doing?
Taking whatever the input is, and defining it as correct so long as it contains red within a set area.
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
If you space out each of the letters. (r e d)
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
I assume it will hint at the player being close to the answer if they answer pink. 
   - What is happening on line 12?
It's an else/if "elif" line that will hint at the player's proximity to the corrrect answer.
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
To hold all the other code within a larger 'while' statement.
   - Why are lines 10–17 indented?
Because they all fall under the same 'while' statement.
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
It would break the code, and take the input as if we were still on main01.py.
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
 - Open main09.py. What is happening on line 13?
It's setting up a count statement that will add 1 each time the player tries.
   - What is the purpose of “count”?
To count the amount of tries it's taking the player to reach the correct answer.
   - What is happening on line 22?
There is no line 22, but if you are referring to line 21, it's displaying how many tries it took the player to reach the correct answer.
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 Did that ^.
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
 It's definining a function, choose_color, which will repeat each time the game is restarted, and will select a new color each time. On top of this, it will change the color to another random one if the previous match's color was selected again by chance.
  
