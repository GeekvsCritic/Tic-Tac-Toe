# Tic-Tac-Toe

<h2 style="text-align: center;">Description</h2>

<p>We are at the finish line! But playing alone is not so interesting, is it? Let's combine our successes in past stages and get Tic-Tac-Toe with the ability to play from the beginning (empty field) to the result (win or draw).</p>

<p>Now it is time to make a working game!</p>

<p>In the last stage, make it so you can play a full game with a friend. First one of you moves as X, and then the other one moves as O.</p>

<h2 style="text-align: center;">Objectives</h2>

<p>In this stage, you should write a program that:</p>

<ol>
	<li>Prints an empty field at the beginning of the game.</li>
	<li>Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a field with the changes if everything is ok.</li>
	<li>Ends the game when someone wins or there is a draw.</li>
</ol>

<p>You need to output the final result after the end of the game.</p>

<p>Good luck gaming!</p>

<h2 style="text-align: center;">Example</h2>

<p>The example below shows how your program should work.<br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">---------
|       |
|       |
|       |
---------
Enter the coordinates: &gt; 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: &gt; 2 2
This cell is occupied! Choose another one!
Enter the coordinates: &gt; two two
You should enter numbers!
Enter the coordinates: &gt; 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: &gt; 1 3
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: &gt; 3 1
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: &gt; 1 2
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: &gt; 1 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: &gt; 3 2
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: &gt; 2 1
---------
| O     |
| O X O |
| X X X |
---------
X wins</code></pre>
