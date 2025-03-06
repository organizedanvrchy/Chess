import pygame
import chess
import chess.engine

# Screen Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (240, 234, 214)         # Off-white color
BLACK = (118, 150, 86)          # Actually a green color
COLORS = [BLACK, WHITE]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Load piece images
piece_images = {}

def load_pieces():
    pieces = "rnbqkpRNBQKP"
    for piece in pieces:
        img = pygame.image.load(f"pieces/{piece}.svg")
        piece_images[piece] = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))

# Initialize Chess Board
chess_board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

# Track piece being moved
dragging_piece = None
start_pos = None

# Font for displaying text
font = pygame.font.SysFont('Lexend', 36)

def draw_board():
    """Draws the chessboard, highlights the king in check, and attacking piece."""
    king_in_check = None
    attacking_pieces = []

    # Check if the king is actually in check
    if chess_board.is_check():
        king_in_check = chess_board.king(chess_board.turn)  # Get the checked king's square
        
        # Find all pieces attacking the king
        for move in chess_board.legal_moves:
            if move.to_square == king_in_check:
                attacking_pieces.append(move.from_square)

    for row in range(ROWS):
        for col in range(COLS):
            square = chess.square(col, 7 - row)
            color = COLORS[(row + col) % 2]  # Default square color

            # Only highlight if the king is actually in check
            if square == king_in_check:
                color = (255, 0, 0)  # Red for king in check
            elif square in attacking_pieces:
                color = (255, 165, 0)  # Orange for attacking piece

            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Draw pieces
    for square in chess.SQUARES:
        piece = chess_board.piece_at(square)
        if piece:
            col, row = chess.square_file(square), chess.square_rank(square)
            screen.blit(piece_images[piece.symbol()], (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE))

def ai_move():
    """AI makes a move using Stockfish."""
    if not chess_board.is_game_over():
        result = engine.play(chess_board, chess.engine.Limit(time=0.5))  # AI thinks for 0.5s
        chess_board.push(result.move)

def handle_mouse_down(pos):
    """Handles when a player clicks on a piece."""
    global dragging_piece, start_pos
    col, row = pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE
    square = chess.square(col, 7 - row)  # Convert Pygame coordinates to chess board index

    piece = chess_board.piece_at(square)
    if piece and piece.color == chess.WHITE:  # Allow moving only white pieces
        dragging_piece = piece
        start_pos = square

def handle_mouse_up(pos):
    """Handles when a player releases a piece."""
    global dragging_piece, start_pos

    if dragging_piece is None:
        return
    
    col, row = pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE
    target_square = chess.square(col, 7 - row)

    move = chess.Move(start_pos, target_square)
    if move in chess_board.legal_moves:
        chess_board.push(move)  # Make move
        ai_move()  # Let AI respond
    
    dragging_piece, start_pos = None, None

def display_result():
    """Display the result of the game."""
    if chess_board.is_checkmate():
        result_text = "Checkmate! " + ("White" if chess_board.turn == chess.BLACK else "Black") + " wins!"
        text_color = (255, 255, 255)  # White text
        background_color = (255, 0, 0)  # Red background for checkmate
    elif chess_board.is_stalemate() or chess_board.is_insufficient_material() or chess_board.is_seventyfive_moves():
        result_text = "Draw!"
        text_color = (255, 255, 255)  # White text
        background_color = (0, 0, 0)  # Black background for draw
    elif chess_board.is_check():
        result_text = "Check!"
        text_color = (0, 0, 0)  # Black text
        background_color = (255, 255, 0)  # Yellow background for check
    else:
        result_text = "Game Over!"
        text_color = (0, 0, 0)  # Black text
        background_color = (200, 200, 200)  # Light gray background for game over
    
    # Create the result text surface
    result_surface = font.render(result_text, True, text_color)
    result_rect = result_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    # Draw background rectangle for the text
    pygame.draw.rect(screen, background_color, result_rect.inflate(20, 20))  # Adding padding around the text

    # Draw the result text
    screen.blit(result_surface, result_rect)

def update_display():
    """Updates the game display."""
    draw_board()

    if chess_board.is_game_over():
        display_result()

    pygame.display.update()

def main():
    load_pieces()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_down(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                handle_mouse_up(event.pos)
        
        update_display()
    
    engine.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
