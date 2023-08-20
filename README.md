### Tic-Tac-Toe

A quick Python implementation, supports two algorithms for the computer play,
Negamax & Monte Carlo Tree Search.

For a quiz, challenge for beginner students is to convert to C# (Haskell is an alternative).

See ```main.py```.

Many thanks to [Code Monkey King (Maksim Korzh)](https://github.com/maksimKorzh), take
a look at that GitHub repo. Lots of examples (inc. tic-tac-toe) of game playing programs.


#### Notes

1. Some notes on the implementation. Watch some YouTube videos on each
   of the three below;
   1. Two BitBoards are used for board state, one to represent
      naughts and the other crosses.
   2. Negmax with Alpha, Beta pruning.
   3. Monte Carlo Tree Search.

First Goal is to migrate the code to C#; 

1. Create 3 projects in an empty solution; 
   1. TicTacToe.Core (core abstractions, algorithms etc.)
   2. TicTacToe.Test (think about test cases).
   3. TicTacToe.App (build a simple app, can use console game loop per Python implementation).

#### Questions, are in the code;

- Any changes to MCTS to allow it to play naughts first?
- Could you implement an interrupt, so the program chooses the best so far move.
- Python Enum are classes with methods, convert to classes with constants or
  add extension methods.
  
  
#### Suggestions (pick one or two);
   
- Read up on BitBoards, using these is preferable to using numpy/arrays
  of ones and zeros!! We just use two integers.
- You could even convert the board state to one integer of 18 bits with
  more complicated masking.
- Play around with the num. of iterations in MCTS and depth for negamax.
- The game loop should be a higher order function, taking a function 
  (which search algorithm?) as a parameter.
- Allow the code to play NegaMax vs MCTS.
- Add traversal logic to display the game tree.


#### Convert to Haskell;

Read Graham Hutton's 'Programming in Haskell' (2nd edition) book,
he has a very basic tic-tac-toe implementation.

- Convert it to using numerical scoring and implement MCTS.
- (Advanced) Think about changing the book implementation, using data structure with Zipper
  and State Monad.


#### Finally;

- Read up on machine learning techniques. Tic-Tac-Toe is a great
  way to experiment with ML frameworks to gain intuition on how they
  work. Apply techniques to more advanced game.
