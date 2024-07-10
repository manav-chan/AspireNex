# AspireNex - Artifical Intelligence

1. # Tic-Tac-Toe AI
   [Link of deployed application](https://manav-chan.github.io/tic-tac-toe/)
   - Created the Tic-Tac-Toe game using HTML/CSS and Javascript.
   -  Implemented 2 modes for the computer to play it's turn:
      - Random mode: Computer will randomly select one of the free cells in the Tic-Tac-Toe grid and play it's turn thus enabling fairness in the game.
      - MiniMax algorithm: Optimal algorithm that makes the computer unbeatable.
   
   ## MiniMax Algorithm
   The Minimax algorithm is a decision-making algorithm used in game theory, artificial intelligence, and computer science to find the optimal move for a player, assuming that the opponent is also playing optimally. It is widely used in two-player turn-based games such as Tic-Tac-Toe, Chess, and Go. How it works-
   - Tree Structure: The algorithm constructs a game tree, starting from the current board state and expanding down to terminal states (end of the game) by simulating all possible moves for both players.
   
   - Terminal States Evaluation: Each terminal state is evaluated to determine the score from the perspective of the maximizing player. Positive scores favor the maximizer, while negative scores favor the minimizer.
   
   - Minimax Decision: The algorithm recursively applies the following rules to determine the best move:
   
   - Maximizer's Move: When it's the maximizer's turn, it chooses the move that leads to the state with the maximum score.
   - Minimizer's Move: When it's the minimizer's turn, it chooses the move that leads to the state with the minimum score.
   - Pruning: Alpha-beta pruning is often used in conjunction with Minimax to reduce the number of nodes evaluated in the game tree. It does this by eliminating branches that cannot possibly influence the final decision.
   
   - Best Move Selection: Starting from the terminal states, the algorithm backtracks and selects the move that leads to the best possible outcome, taking into account that the opponent is also playing optimally.
   
   Algorithm:
   ```javascript
   function minimax(newBoard, player, alpha = -Infinity, beta = Infinity) {
       // returns list of indices denoting empty cells on the board
       let availableSpots = emptySquares(newBoard);
       
       // base conditions
       if (checkWin(newBoard, huPlayer)) {
           return {score: -1};
       } else if (checkWin(newBoard, aiPlayer)) {
           return {score: 1};
       } else if (availableSpots.length === 0) {
           return {score: 0};
       }
   
       // recursively call for every possible move and store the score corresponding to each move in 'moves' list
       let moves = [];
       for (let i = 0; i < availableSpots.length; i++) {
           let move = {};
           move.index = newBoard[availableSpots[i]];
           newBoard[availableSpots[i]] = player;
   
           let result;
           if (player === aiPlayer) {
               result = minimax(newBoard, huPlayer, alpha, beta);
               move.score = result.score;
               alpha = Math.max(alpha, result.score);
           } else {
               result = minimax(newBoard, aiPlayer, alpha, beta);
               move.score = result.score;
               beta = Math.min(beta, result.score);
           }
   
           newBoard[availableSpots[i]] = move.index;
           moves.push(move);
   
           // alpha-beta pruning to save computation time and memory
           if(beta <= alpha) {
               break;
           }
       }
   
       // calculates best move on the basis of highest score for ai player, and lowest score for computer player
       let bestMove;
       if (player === aiPlayer) {
           let bestScore = -Infinity;
           for (let i = 0; i < moves.length; i++) {
               if (moves[i].score > bestScore) {
                   bestScore = moves[i].score;
                   bestMove = i;
               }
           }
       } else {
           let bestScore = Infinity;
           for (let i = 0; i < moves.length; i++) {
               if (moves[i].score < bestScore) {
                   bestScore = moves[i].score;
                   bestMove = i;
               }
           }
       }
   
       return moves[bestMove];
   }
   ```
   ## GUI
   ![image](https://github.com/manav-chan/AspireNex/assets/71835184/65032505-d278-4794-9ee9-fc06267c5bdd)

2. # Image Captioning
   - Defined and trained an Image Caption Generator model on the Flickr 8K image dataset and achieved a BLEU-1 score of 0.546282 and BLEU-2 score of 0.320683.
   - Used pretrained VGG16 CNNd model for image feature extraction after removing the last classification layer.
   - Implemented Long Short-Term Memory Recurrent Neural Network layer in the model.
   - Created a web server for hosting the web application using Python Flask.
   - Created GUI using HTML, Javascript and Bootstrap.

   ## BLEU Score
   - Bilingual Evaluation Understudy scores are a metric used to evaluate the quality of text which has been machine-translated from one language to another. They are also commonly used for evaluating the quality of generated text in tasks like image captioning, where the generated text is compared against one or more reference texts.
   - BLEU-1: Measures the precision of unigrams (single words). It checks how many single words in the generated text match the reference text.
   - BLEU-2: Measures the precision of bigrams (pairs of consecutive words). It checks how many word pairs in the generated text match the reference text.
   - BLEU-1 score of 0.546282 and BLEU-2 score of 0.320683 are considered reasonably good scores. For state-of-the-art models, BLEU-1 scores can often be in the range of 0.6 to 0.7, and BLEU-2 scores can be around 0.4 to 0.5 or higher.
   
   ## Model Architecture
   ![model](https://github.com/manav-chan/AspireNex/assets/71835184/2df41241-fe5e-49b3-97ea-c8d984793c52)

   ## How to use?
   1. Clone this repository, navigate into the repository.
   2. Download the machine learning model from this [link](https://drive.google.com/file/d/1EQ1gj9u3hHrDGsxhL1C-g1-PA_lAwUnV/view?usp=sharing) into the root directory of the application.
   3. Create a python virtual environment.
      ```terminal
      python3 -m venv venv
      ```
   4. Activate the virtual environment.
      ```terminal
      source venv/bin/activate
      ```
   5. Build the project.
      ```terminal
      pip install -r requirements.txt
      ```
   6. Run the appliction.
      ```terminal
      python app.py
      ```

   ## GUI
   ![image](https://github.com/manav-chan/AspireNex/assets/71835184/1296ab46-0bf6-418e-b089-4c5569c23c06)
   ![image](https://github.com/manav-chan/AspireNex/assets/71835184/319566c8-a25c-43a7-b9eb-62cefdb0491b)


     

   
