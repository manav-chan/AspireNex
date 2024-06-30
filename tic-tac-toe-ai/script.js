let board;
const huPlayer = 'O';
const aiPlayer = 'X';
const winCombos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

let huWins = 0;
let aiWins = 0;
let minimaxFlag = false;
const cells = document.querySelectorAll('.cell');

start();

function start() {
    document.querySelector(".msg").style.display = "none";
    board = Array.from(Array(9).keys());
    for (let i = 0; i < cells.length; i++) {
        cells[i].innerText = '';
        cells[i].style.removeProperty('background-color');
        cells[i].addEventListener('click', turnClick, false);
    }
}

function turnClick(event) {
    if (typeof board[event.target.id] === 'number') {
        turn(event.target.id, huPlayer);
        if (!checkTie()) {
            turn(bestSpot(), aiPlayer);
        }
    }
}

function turn(cellId, player) {
    board[cellId] = player;
    document.getElementById(cellId).innerText = player;
    let gameWon = checkWin(board, player);
    if (gameWon) gameOver(gameWon);
}

function checkWin(board, player) {
    let plays = [];
    for (let i = 0; i < 9; i++) {
        if (board[i] === player) {
            plays.push(i);
        }
    }
    let gameWon = null;
    for (let index = 0; index < winCombos.length; index++) {
        let win = winCombos[index];
        let winFound = true;
        for (let elem of win) {
            if (!plays.includes(elem)) {
                winFound = false;
                break;
            }
        }
        if (winFound) {
            gameWon = {index: index, player: player};
            break;
        }
    }
    return gameWon;
}

function gameOver(gameWon) {
    for (let index of winCombos[gameWon.index]) {
        document.getElementById(index).style.backgroundColor = gameWon.player === huPlayer ? "green" : "red";
    }
    for (let i = 0; i < cells.length; i++) {
        cells[i].removeEventListener('click', turnClick, false);
    }
    declareWinner(gameWon.player === huPlayer ? "You win!" : "You lose!");
}

function checkTie() {
    if (emptySquares(board).length === 0) {
        for (let i = 0; i < cells.length; i++) {
            cells[i].style.backgroundColor = "green";
            cells[i].removeEventListener('click', turnClick, false);
        }
        declareWinner("Tie Game!");
        return true;
    }
    return false;
}

function declareWinner(msg) {
    document.querySelector(".msg").style.display = "block";
    document.querySelector(".msg .text").innerText = msg;
    
    if (msg === "You win!") {
        huWins++;
    } else if (msg === "You lose!") {
        aiWins++;
    }

    updateScore();
}

function updateScore() {
    document.querySelector(".score .hu").innerText = huWins;
    document.querySelector(".score .ai").innerText = aiWins;
}

function resetScore() {
    huWins = 0;
    aiWins = 0;
    updateScore();
}

function toggleAi() {
    const aiBtn = document.querySelector("#aibtn");
    if (aiBtn.innerText.includes("Enable")) {
        aiBtn.innerText = "Disable unbeatable AI";
        minimaxFlag = true;
    } else {
        aiBtn.innerText = "Enable unbeatable AI";
        minimaxFlag = false;
    }
}


function bestSpot() {
    if (minimaxFlag) {
        return minimax(board, aiPlayer).index;
    } else {
        let availableSpots = emptySquares(board);
        let randIdx = Math.floor(Math.random() * availableSpots.length);
        return availableSpots[randIdx];
    }
}

function emptySquares(newBoard) {
    return newBoard.filter(s => typeof s === 'number');
}

function minimax(newBoard, player, alpha = -Infinity, beta = Infinity) {
    let availableSpots = emptySquares(newBoard);
    
    // base condition
    if (checkWin(newBoard, huPlayer)) {
        return {score: -1};
    } else if (checkWin(newBoard, aiPlayer)) {
        return {score: 1};
    } else if (availableSpots.length === 0) {
        return {score: 0};
    }

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

        // alpha-beta pruning
        if(beta <= alpha) {
            break;
        }
    }

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
