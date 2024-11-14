# Import and initialize pygame
import pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Define GameObject class
# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image) # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# Instance of GameObject
apple = GameObject(120, 300, 'apple.png')
strawberry = GameObject(210, 210, 'strawberry.png')

# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Clear screen
  screen.fill((255, 255, 255))

  # Render game object
  apple.render(screen)
  strawberry.render(screen)

  # Update the window
  pygame.display.flip()


# Quit pygame
pygame.quit()