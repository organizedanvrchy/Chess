# Chess Game with Pygame and Stockfish
This project is a Python-based chess game that utilizes the Pygame library for the graphical interface and the Stockfish chess engine for AI gameplay. The game allows a human player to play as White against the AI (Black) in a standard game of chess.

---

## Features
### Python Concepts Used
- **Object-Oriented Programming (OOP)**: The code is structured using classes and methods, although the main logic is currently in a procedural style.
- **Event Handling**: The game uses Pygame's event handling to manage user inputs like mouse clicks and releases.
- **File I/O**: The game loads piece images from the `pieces/` directory.
- **External Libraries**: The project integrates with the `chess` and `chess.engine` libraries for game logic and AI moves, respectively.
- **Global Variables**: The game uses global variables to track the state of the game, such as the piece being dragged and its starting position.

### Game Features
- **Interactive Chessboard**: The game features an 8x8 chessboard with alternating colors. The board is drawn using Pygame's drawing functions.
- **Piece Movement**: Players can click and drag pieces to move them. The game enforces legal moves according to standard chess rules.
- **AI Opponent**: The game uses the Stockfish chess engine to play as the opponent (Black). The AI makes moves after the player (White) makes a move.
- **Check and Checkmate Detection**: The game highlights the king in red when it is in check and the attacking pieces in orange. It also detects checkmate and displays the result.
- **Draw Conditions**: The game detects stalemates, insufficient material, and the 75-move rule, and declares a draw when applicable.
- **Game Over Screen**: When the game ends (checkmate, stalemate, etc.), a result screen is displayed with appropriate text and background colors.

### Code Structure
- **Initialization**: The game initializes Pygame, loads piece images, and sets up the chessboard and Stockfish engine.
- **Drawing Functions**: The `draw_board()` function renders the chessboard, pieces, and highlights for check and attacking pieces.
- **Event Handling**: The `handle_mouse_down()` and `handle_mouse_up()` functions manage piece movement based on user input.
- **AI Move**: The `ai_move()` function uses Stockfish to generate a move for the AI opponent.
- **Game Over Handling**: The `display_result()` function displays the game result when the game ends.
- **Main Loop**: The `main()` function contains the game loop, which handles events, updates the display, and manages the game state.

---

## Requirements
- **Python 3.x**: The code is written in Python 3.
- **Pygame**: The graphical interface is built using the Pygame library.
- **python-chess**: The game logic is managed using the `chess` library.
- **Stockfish**: The AI opponent is powered by the Stockfish chess engine. Ensure Stockfish is installed and accessible at `/usr/games/stockfish`.

---

## Installation
1. **Install Python**: <br> Ensure Python 3.x is installed on your system.
2. **Install Pygame**: <br> Install the Pygame library using pip:
   ```bash
   pip install pygame
   ```
3. **Install python-chess**: <br> Install the chess library using pip:
   ```bash
   pip install python-chess
   ```
4. **Install Stockfish**: <br> Ensure Stockfish is installed on your system. On Debian-based systems, you can install it using:
   ```bash
   sudo apt-get install stockfish
   ```
5. **Download Piece Images**: <br> Place the piece images (in SVG format) in a pieces/ directory. The images should be named according to the piece symbols (e.g., K.svg for the white king, k.svg for the black king, etc.).

---

## Running the Game
To run the game, execute the following command in the terminal:
```bash
python main.py
```

---

## Controls
Mouse `Click` and `Drag`: <br>
`Click` on a piece to select it, `drag` it to the desired square, and `release` to make a move.

---

## Possible Future Improvements
Undo Move: Implement an undo feature to allow players to revert their last move.

Multiplayer Mode: Add support for two-player gameplay (human vs. human).

Customizable AI Strength: Allow players to adjust the AI's strength by changing the thinking time or depth.

Sound Effects: Add sound effects for moves, captures, and checkmate.

Improved UI: Enhance the user interface with better graphics, animations, and a menu system.

---

## License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as per the license terms.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

## Acknowledgments
Pygame: For providing the graphical framework.

python-chess: For handling the chess logic.

Stockfish: For powering the AI opponent.

---

**Enjoy playing chess! 🎉**
