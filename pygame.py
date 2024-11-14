# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Define GameObject class
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height):
    super(GameObject, self).__init__()
    self.surf = pygame.Surface((width, height))
    self.surf.fill((255, 0, 255))
    self.rect = self.surf.get_rect()
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# Instance of GameObject
box = GameObject(120, 300, 50, 50)

# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Clear screen
  screen.fill((255, 255, 255))
      
  # Draw a circle
  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

  # Render game object
  box.render(screen)

  # Update the window
  pygame.display.flip()


# Quit pygame

pygame.quit()