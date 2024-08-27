import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BROWN = (181, 101, 29)
LIGHT_BROWN = (222, 184, 135)

# Load images
def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bP", "wR", "wN", "wB", "wQ", "wK", "wP"]
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load(f"images/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE))
    return images

# Draw the board
def draw_board(win):
    colors = [LIGHT_BROWN, DARK_BROWN]
    for row in range(ROWS):
        for col in range(COLS):
            color = colors[(row + col) % 2]
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw pieces on the board
def draw_pieces(win, board, images):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != "--":
                win.blit(images[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Initialize the game window
def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Chess Game")

    images = load_images()

    # Sample board setup (starting position)
    board = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    ]

    run = True
    while run:
        draw_board(win)
        draw_pieces(win, board, images)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if _name_ == "_main_":
    main()
