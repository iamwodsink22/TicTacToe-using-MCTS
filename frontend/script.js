let userSymbol = '';
let aiSymbol = '';
const board = Array(9).fill(0);

function chooseSymbol(symbol) {
  userSymbol = symbol;
  aiSymbol = symbol === 'X' ? 'O' : 'X';
  console.log(userSymbol)
  document.getElementById("choice").classList.add("hidden");
  document.getElementById("board").classList.remove("hidden");
}

function makeMove(index) {
  if (board[index] || !userSymbol) return;

  board[index] = userSymbol;
  document.querySelectorAll('.cell')[index].innerText = userSymbol;

  if (checkWin(userSymbol)) {
    alert("You win!");
    resetGame();
    return;
  }
  if(board.includes(0)==false){
    resetGame()
 }

  aiMove(); 
}

async function aiMove() {
  
  const aiMoveIndex = await getAIMove(board, aiSymbol)

  
  if (aiMoveIndex !== -1) {
    board[aiMoveIndex] = aiSymbol;
    document.querySelectorAll('.cell')[aiMoveIndex].innerText = aiSymbol;

    
    if (checkWin(aiSymbol)) {
      alert("AI wins!");
      resetGame();
    }

  }
}

function checkWin(symbol) {
  const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]             
  ];

  return winPatterns.some(pattern => 
    pattern.every(index => board[index] === symbol)
  );
  
}

function resetGame() {
  board.fill(0);
  document.querySelectorAll('.cell').forEach(cell => cell.innerText = '');
  document.getElementById("choice").classList.remove("hidden");
  document.getElementById("board").classList.add("hidden");
  userSymbol = '';
  aiSymbol = '';
}

async function getAIMove(board, aiSymbol) {

  try {
    const response = await fetch('https://tic-tac-toe-using-mcts-1jhb.vercel.app/move', {
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json' 
      },
      mode: 'cors', 
      body: JSON.stringify({
        state: board,
        symbol: userSymbol 
      })
    });

    if (!response.ok) {
      throw new Error('Network response was not ok: ' + response.statusText);
    }

    const data = await response.json();
    return data.action;

  } catch (error) {
    console.error('Error fetching AI move:', error); 
    return null; 
  }
}

