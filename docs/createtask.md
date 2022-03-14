{% include navigation.html %}


## PBL Plan
Goal was to implement these different types of code into our technicals to ensure they blend into our website, but are still able to be shown for the Create Task. There are 4 different written types of code: Data Abstraction, Managing Complexity, Procedural Abstraction, and Algorithm Implementation.  

StudyOwl is a studying website that encourages students to learn in a more efficient manner. One of the main features of the studyowl is the StudyRoom where students are inserted into the right environment to concentrate. While there are many features to help students focus, the studyowl team believes that hard word should be balanced with small breaks to give the brain time to reset. This learning strategy will be implemented in a BreakRoom which directly compliments our StudyRoom. Inside the break room will be mind stimulating games so that students can improve their logic and reasoning skills even while not studying. These games will be part of the create task project and include word games, memory games, etc.

## Ideas
Ideas: Hangman(string-man), Guess the word, Tic-Tac-Toe, Complex games, Memory game

Hangman - 5 letter word, user guesses different letters. if the letter is in the word then the spot gets filled in, if not, a man gains his limbs one by one. (Possible idea: implement words with an API)

Word Guess - user has 6 chances to guess a 5 letter word. user guesses different 5 letter words until they guess the right one. For every guess letters that are present in the actual word are indicated and letters that are in the correct spot are also indicated. (Possible idea: implement words with an API)

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

