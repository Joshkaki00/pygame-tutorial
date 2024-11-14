# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

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

# Create the game loop
running = True
while running:
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
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Draw a circle
  screen.fill((255, 255, 255))
  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
  # Update the window
  pygame.display.flip()