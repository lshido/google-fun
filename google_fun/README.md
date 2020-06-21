# Description
google-fun is where I keep my code solutions for the google foobar challenge.
The ones that get published are ones that I have submitted (or attempted to submit).
I also have my own set of unit tests that are modeled off the non-hidden tests.

# Results
I was able to complete Levels 1 and 2. 
On the first challenge of Level 3, I was able to pass 3 out of 5 test cases, but I couldn't figure out how to get the other hidden cases to pass, and I ran out of time (that week also just happened to be particularly busy at work, so I couldn't dedicate as much time as I would have liked.)

## Level 3 Recursion Problem
The first challenge on Level 3 is a maze-solving problem and this was the one I couldn't succesfully verify and submit.

After searching online for people's guesses as to what the hidden test cases were and playing around with the code some more, my suspicion is that their test cases have to do with solving for mazes of a larger size and checking that the solve time is below a certain value. I used the Lee Algorithm based on Breadth-first search (BFS) to solve the maze. It's simple but known to be memory intensive and time-consuming, and based on my unit tests, it was clear that it was taking too long to solve a single problem. I'm fairly confident that given enough time, my code will output the correct answer to any given maze.

# Other Tidbits
It might seem strange for me to have packaged this, but I just did it so I could import my methods for unit testing. TDD FTW!
Please be cool and don't cheat on the foobar challenge by submitting my solutions as your own. You could probably find better, more elegant solutions from someone else, and besides, what's the fun in copying and pasting someone else's work?