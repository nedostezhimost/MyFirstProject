import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Buggy Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Paddle settings
paddle_width = 15
paddle_height = 100

left_paddle = pygame.Rect(20, HEIGHT // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(WIDTH - 35, HEIGHT // 2, paddle_width, paddle_height)

paddle_speed = 6

# Ball settings
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
ball_dx = 5
ball_dy = 5

left_score = 0
right_score = 0

font = pygame.font.SysFont(None, 48)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        left_paddle.y -= paddle_speed

    if keys[pygame.K_s]:
        left_paddle.y += paddle_speed

    if keys[pygame.K_UP]:
        right_paddle.y -= paddle_speed

    if keys[pygame.K_DOWN]:
        right_paddle.y += paddle_speed

    # Move ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Bounce off top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dx *= -1

    # Paddle collisions
    if ball.colliderect(left_paddle):
        ball_dx *= -1

    if ball.colliderect(right_paddle):
        ball_dx *= -1

    # Scoring
    if ball.left <= 0:
        right_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)

    if ball.right >= WIDTH:
        left_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    score_text = font.render(
        f"{left_score} : {right_score}",
        True,
        WHITE
    )

    screen.blit(score_text, (WIDTH // 2 - 40, 20))

    pygame.display.flip()
    clock.tick(60)