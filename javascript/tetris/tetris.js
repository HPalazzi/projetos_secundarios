class  Tetris{
  constructor(imageX, imageY, template) {
    this.imageY = imageY;
    this.imageX = imageX;
    this.template = template;
    this.x = squareCountX / 2;
    this.y = 0;
    }
    
    checkBottom(){};
      
    checkLeft(){};
      
    checkRight(){};
      
    moveLeft(){};
      
    moveRight(){};
      
    moveBottom(){};
    changeRotation(){};
 };

 const imageSquareSize = 24;
 const size = 40;
 const framePerSecond = 24;
 const gameSpeed = 5;
 const canvas = document.getElementById("canvas");
 const nextShapeCanvas = document.getElementById("nextShapeCanvas");
 const scoreCanvas = document.getElementById("scoreCanvas");
 const image = document.getElementById("image");
 const ctx = canvas.getContext("2d");
 const nctx = nextShapeCanvas.getContext("2d");
 const sctx = scoreCanvas.getContext("2d");
 const squareCountX = canvas.width / size;
 const squareCountY = canvas.height / size;

const shapes = [
    new Tetris(0, 120, [
      [0, 1, 0],
      [0, 1, 0],
      [1, 1, 0],
    ]),
    new Tetris(0, 96, [
      [0, 0, 0],
      [1, 1, 1],
      [0, 1, 0],
    ]),
    new Tetris(0, 72, [
      [0, 1, 0],
      [0, 1, 0],
      [0, 1, 1],
    ]),
    new Tetris(0, 48, [
      [0, 0, 0],
      [0, 1, 1],
      [1, 1, 0],
    ]),
    new Tetris(0, 24, [
      [0, 0, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 0],
    ]),
    new Tetris(0, 0, [
      [1, 1],
      [1, 1],
    ]),
  
    new Tetris(0, 48, [
      [0, 0, 0],
      [1, 1, 0],
      [0, 1, 1],
    ]),
  ];

let gameMap;
let gameOver;
let currentShape;
let nextShape; 
let score;
let initialTwoDArr;
let whiteLineThickness = 4

let gameLoop = () => {
    setInterval(update, 1000/gameSpeed)
    setInterval(draw, 1000/framePerSecond)
};

let update = () => {};

let drawRect = (x, y, width, height, color) => {
  ctx.fillStyle = color
  ctx.fillRect(x, y, width, height)
}

let drawBackground = () => {
  drawRect(0, 0, canvas.width, canvas.height, "#bca0dc");
  for (let i = 0; i < squareCountX + 1; i++) {
    drawRect(size * i - whiteLineThickness, 0, whiteLineThickness, canvas.height, "white");
  }

  for (let i = 0; i < squareCountY + 1; i++) {
    drawRect(0, size * i - whiteLineThickness, canvas.width, whiteLineThickness,"white");
  }
};

let draw = () => { // 16:20 https://www.youtube.com/watch?v=h1-zQ0SSS6M&t=996s
    ctx.clearRect(0,0, canvas.width, canvas.height)
    drawBackground();
    drawSquares();
    drawCurrentTetris();
    drawNextShape();
    if(gameOver){
        drawGameOver()
    }
};

let getRandomShape = () => {
    return Object.create(shapes [ Math.floor[ Math.random() * shapes.length ] ])
}

let resetVars = () => {
    initialTwoDArr = []
    for(let i = 0; i < squareCountY; i++){
        let temp = []
        for(let j = 0; j < squareCountX; j++){
            temp.push({imageX: -1, imageY: -1});
        }
        initialTwoDArr.push(temp)
    }
    score = 0
    gameOver =  false
    currentShape =  getRandomShape()
    nextShape = getRandomShape()
    gameMap = initialTwoDArr
};

resetVars();
gameLoop();