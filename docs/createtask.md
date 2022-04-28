{% include navigation.html %} <br>

# <a href="https://replit.com/@Samayas/Create-Task#main.py">Runtime and Code</a>

# <a href="https://loom.com/share/4b50277afde247b1b25d4e882a9ee789">Video</a>




## Written Response Questions for Create Task
<table>
   <tr>
    <th>Number</th>
    <th>Question</th>
      <th>Answer</th>
   </tr>
   <tr>
    <th>3ai</th>
    <th>Describes the overall purpose of the program</th>
    <th>
       This program allows the user to play an entertaining game to help stimulate their mind to improve their analytical skills in an enjoyable way.</th>
   </tr>
   <tr>
    <th>3aii</th>
    <th>Describes what functionality of the program is demonstrated in the video</th>
    <th>The user is given six guesses to evaluate a randomly chosen word based on the color change of letters from the word inputted. If the letters turn green they are correct, if they are present, yellow, otherwise, no color change is seen.</th>
   </tr>
   <tr>
    <th>3aiii</th>
    <th>Describes the input and output of the program demonstrated in the video</th>
      <th> In the video, the 5-letter valid word 'irate' is inputted. The output depends on the input and displays the letters, 'r' and 't' in green and yellow, respectively. Once the user has guessed the correct word, 'you win!' is outputted. In the second scenario, a 4 letter word, and an invalid word are inputted, so the program outputs a message saying that the input is, 'not a 5 letter word' or, 'not a valid word' and prompts the user with another input opportunity.
</th>
   </tr>
   <tr>
    <th>3bi</th>
    <th>The first program code segment must show how data have been stored in the list.</th>
    <th><img width="409" alt="mistake" src="https://user-images.githubusercontent.com/89225474/165684009-e559e9f0-726d-4aa9-92b7-a5a4cd4891d3.png"></th>
   </tr>
   <tr>
    <th>3bii</th>
    <th>The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.</th>
    <th><img width="212" alt="mistake" src="https://user-images.githubusercontent.com/89225474/165684201-537e01d3-b208-449c-a181-25443c211c99.png"></th>
   </tr>
   <tr>
    <th>3biii</th>
    <th>Identifies the name of the list being used in this response</th>
    <th>The list is named wordbank and in the second image wordbank is accessed to assign a random value to variable word.</th>
   </tr>
   <tr>
    <th>3biv</th>
    <th>Describes what the data contained in the list represent in your program</th>
      <th>The data contained in the list represents all of the possible words the user might be able to guess.</th>
   </tr>
   <tr>
    <th>3bv</th>
    <th>Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list</th>
      <th>The list allows for the program to store all the possible words in one location. Without the list holding many diverse words the program can only be played a certain amount of times until it becomes redundant. One would have to resort to using different variables to hold many different words which would be impractical.</th>
   </tr>
   <tr>
    <th>3ci</th>
    <th>The first program code segment must be a student-developed procedure that:□ Defines the procedure’s name and return type (if necessary) □ Contains and uses one or more parameters that have an effect on the functionality of the procedure □ Implements an algorithm that includes sequencing, selection, and iteration</th>
      <th><img width="166" alt="mistake" src="https://user-images.githubusercontent.com/89225474/165685759-1bf18ad0-41ca-4cbd-9ea9-1fec6bb45588.png"></th>
   </tr>
   <tr>
    <th>3cii</th>
    <th>The second program code segment must show where your student-developed procedure is being called in your program.</th>
      <th><img width="272" alt="mistake" src="https://user-images.githubusercontent.com/89225474/165685990-9917480c-dd1b-4ea1-958a-dc9c9a3972a0.png"></th>
   </tr>
   <tr>
    <th>3ciii</th>
    <th>Describes in general what the identified procedure does and how it contributes to the overall functionality of the program</th>
    <th>The procedure contributes to the overall functionality of the program as it is the majority of the code that checks the word inputted and compares it to the random word chosen from the list. The for loop is implemented to check whether the number of letters inputted is the correct amount according to the rules, and if so let the letter inputted into each specific tile be assigned to the variable "letter". The if statements are used to compare the inputted word with the randomly chosen word, so if one of the letters inputted is in the chosen word and in the correct spot the tile will turn green. If one of the letters is included in the chosen word the tile will turn yellow, and else the tile will turn gray.</th>
   </tr>
   <tr>
    <th>3civ</th>
    <th>Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.</th>
      <th>First one should set the number of correctly identified letters to 0 so that it is able to be incremented for each correct letter. Next a for loop is needed to call each tile by its name. Inside each span id value is one letter which the user has inputted. One should assign the innerText of the span id to a variable so that all the letters can be checked. Next if statements are used so that each letter of the inputted word can be compared to that of the chosen word, so one should use each letter in the randomly chosen word and equate it to each letter in the inputted word. If the letter is present in the chosen word the correctly identified letters variable should be incremented by one and the color of the tile should be assigned to a data-variable id to change the color of it accordingly. Next else if is used to check whether or not the chosen word includes any of the letters in the inputted word with the .includes function. If so assign the current span id to the specific data-variable to change the color of the tile. Lastly if neither of those conditions are met assign the current span id tile to the data-variable which grays out all the absent letters.</th>
   </tr>
   <tr>
    <th>3di</th>
    <th>Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.</th>
      <th>First Call: The update function is called when the enter key is pressed and lifted upwards.
Second Call:</th>
   </tr>
   <tr>
    <th>3dii</th>
    <th>Describes what condition(s) is being tested by each call to the procedure</th>
      <th>Condition(s) tested by the first call: The program listens for the keyUp which means when the key is pressed and lifted upwards, so when the enter key is pressed the program has a condition that if the user inputted guess is included in the array of all available guess words then the function update will be called to compared the inputted value with the randomly chosen word.
Condition(s) tested by the second call:</th>
   </tr>
   <tr>
    <th>3diii</th>
    <th>Identifies the result of each call</th>
      <th>Result of the first call: The result of this called function is that the gameOver function will be equal to true meaning the user has won the game or the colors of tiles would change accordingly.
Result of the second call:</th>
   </tr>
   </table>

## Requirements

<table>
   <tr>
    <th>Requirements</th>
    <th>Description</th>
      <th>Implementation</th>
   </tr>
   <tr>
    <th>Program Purpose and Function</th>
    <th>Program runs including input, program functionality, output</th>
      <th>Input will come from user entering different words/letters in different attempts to guess the word. Program output will return if the word guessed is correct or if the letter guessed is correct/exists in the word</th>
   </tr>
  <tr>
    <th>Data Abstraction</th>
    <th>Includes two program code segments showing data being stored in list and data from list being used in program</th>
      <th>A predetermined list will be full of different words that are to be guessed. A random math function will generate an index for this list to select random words for the user to guess. The letters/words that the user gueses/inputs will be stored in a separate list to be tested for similarities elsewhere in the code.</th>
   </tr>
  <tr>
    <th>Managing Complexity</th>
    <th>Shows code that uses a list to manage the complexity of the program. The list should be used because it is needed not just for the sake of the grade.</th>
      <th>Instead of the letters of the word being stored in individual variables, they are stored in a single list. Without this list the code will be unorganized and the list allows the letters/words to be called easier. The list containing the word that the user guessed will be called in multiple places to see if any of the letters match any of the corresponding letters in the real word list.</th>
   </tr>
  <tr>
    <th>Procedural Abstraction</th>
    <th>Includes two program code segments, one showing a student developed procedure with at least one parameter that has an affect on the functionality of the procedure, and one showing where the student developed procedure will be called.</th>
      <th>A function to check if the word guessed is correct will be called in multiple places. The parameters for the word guess game will be that the word inputed by user is a real word and has 5 letters. The parameters for the hang man game will be that the input exists in the English alphabet and it has not been guessed before. Only when these parameters are met will the algorithms run and the word/letter will be checked.</th>
   </tr>
  <tr>
    <th>Algorithm Implementation</th>
    <th>Includes sequencing, selection and iteration. The algorithm should be student developed, and it should be descriptive and self-explanatory.</th>
      <th>Algorithm will select each letter in the list/word via linear search (going down the line, increasing indexes from 0), iteration will check that each letter matches the corresponding letter in the actual word for every element in list, sequencing will allow for algorithm to return true or false if letter matches or not, and thus if the word matches or not.</th>
   </tr>

