# Import and initialize pygame
import pygame
pygame.init()
from random import randint, choice

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Define GameObject class
# Game Object
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image).convert_alpha() # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

#Define Apple class
class Apple(GameObject):
 def __init__(self):
   super(Apple, self).__init__(0, 0, 'apple.png')
   self.dx = 0
   self.dy = (randint(0, 100) / 100) + 1
   self.reset() # call reset here! 

 def move(self):
   self.y += self.dy
   # Check the y position of the apple
   if self.y > 500: 
     self.reset()

 # add a new method
 def reset(self):
  lanes = [93, 218, 343]
  self.x = choice(lanes)
  self.y = -64

# Define Strawberry class
class Strawberry(GameObject):
  def __init__(self):
    y = randint(0, 450) # Random y position
    super(Strawberry, self).__init__(-64, y, 'strawberry.png')
    self.dx = (randint(100, 200) / 100) + 1 # Random horizontal speed

  def move(self):
    self.x += self.dx
    # Reset strawberry if it goes off screen
    if self.x > 500:
      self.x = -64 # Start off screen
      self.y = randint(0, 450) # New random y position
      
  def reset(self):
    lanes = [93, 218, 343]
    self.y = choice(lanes)
    self.x = -64

# Load the images
apple_image = 'apple.png'
strawberry_image = 'strawberry.png'

# Create lists to hold apples and strawberries
falling_apple = [Apple() for _ in range(3)]
moving_strawberry = [Strawberry() for _ in range(2)]

# Load moving apple image
apple = Apple()

# Grid setup
grid_size = 3
spacing = 64 + 75 # 64 pixels for image size, 100 pixels for spacing
total_width = (grid_size * 64) + ((grid_size - 1) * 75)
total_height = (grid_size * 64) + ((grid_size - 1) * 75)
start_x = (500 - total_width) / 2
start_y = (500 - total_height) / 2

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
    
# Get the clock
clock = pygame.time.Clock()

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

  # Move and render falling apple
  for apple in falling_apple:
    apple.move()
    apple.render(screen)

  # Move and render moving strawberry
  for strawberry in moving_strawberry:
    strawberry.move()
    strawberry.render(screen)

  # Draw apple
  apple.move()
  apple.render(screen)

  # Set the frame rate
  clock.tick(60)

  # Update the window
  pygame.display.flip()


# Quit pygame
pygame.quit()