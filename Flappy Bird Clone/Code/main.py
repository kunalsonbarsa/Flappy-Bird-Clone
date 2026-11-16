import pygame, random, sys

pygame.init()
W, H = 400, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

PIPE_W, GAP, SPEED = 60, 150, 3

def new_game():
    bird = pygame.Rect(100, 300, 30, 30)
    return bird, 0, [], 0, 0   # bird, velocity, pipes, score, timer

def make_pipe():
    gap_y = random.randint(100, 400)
    top = pygame.Rect(W, 0, PIPE_W, gap_y)
    bottom = pygame.Rect(W, gap_y + GAP, PIPE_W, H - gap_y - GAP)
    return {"top": top, "bottom": bottom, "scored": False}

bird, velocity, pipes, score, timer = new_game()
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                velocity = -10            # flap
            if event.key == pygame.K_r and game_over:
                bird, velocity, pipes, score, timer = new_game()
                game_over = False         # restart

    if not game_over:
        velocity += 1                     # gravity
        bird.y += velocity                # move bird

        timer += 1
        if timer % 90 == 0:               # new pipe
            pipes.append(make_pipe())

        for p in pipes:
            p["top"].x -= SPEED
            p["bottom"].x -= SPEED
            if not p["scored"] and p["top"].right < bird.left:
                p["scored"] = True
                score += 1                # score +1
            if bird.colliderect(p["top"]) or bird.colliderect(p["bottom"]):
                game_over = True

        pipes = [p for p in pipes if p["top"].right > 0]   # remove old pipes

        if bird.bottom >= H or bird.top < 0:               # ground / top
            game_over = True

    screen.fill((135, 206, 235))
    for p in pipes:
        pygame.draw.rect(screen, (0, 160, 0), p["top"])
        pygame.draw.rect(screen, (0, 160, 0), p["bottom"])
    pygame.draw.rect(screen, (255, 215, 0), bird)
    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    if game_over:
        screen.blit(font.render("Game Over", True, (200, 0, 0)), (130, 260))
        screen.blit(font.render("Press R to restart", True, (0, 0, 0)), (100, 300))

    pygame.display.flip()
    clock.tick(30)