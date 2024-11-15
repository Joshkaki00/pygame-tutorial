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
    self.surf = pygame.image.load(image).convert_alpha() # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# Load the images
apple_image = 'apple.png'
strawberry_image = 'strawberry.png'

# Grid setup
start_x, start_y = 100, 100
spacing = 150

# List to hold all GameObjects on grid
objects = []

# Create a 3x3 grid of GameObjects
for row in range(3):
  for col in range(3):
    # Alternate between apple and strawberry
    image = apple_image if (row + col) % 2 == 0 else strawberry_image
    x = start_x + col * spacing
    y = start_y + row * spacing
    obj = GameObject(x, y, image)
    objects.append(obj)

# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Clear screen
  screen.fill((255, 255, 255))

  # Render game objects in grid
  for obj in objects:
    obj.render(screen)

  # Update the window
  pygame.display.flip()


# Quit pygame
pygame.quit()