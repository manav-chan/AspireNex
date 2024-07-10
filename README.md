# AspireNex

## Artifical Intelligence

### Tic-Tac-Toe AI

1. Created the Tic-Tac-Toe game using HTML/CSS and Javascript.
2. Implemented 2 modes for the computer to play it's turn
   - Random mode: Computer will randomly select one of the free cells in the Tic-Tac-Toe grid and play it's turn thus enabling fairness in the game.
   - MiniMax algorithm: Optimal algorithm that makes the computer unbeatable.

### MiniMax Algorithm

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
