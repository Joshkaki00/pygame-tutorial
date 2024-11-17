# Import and initialize pygame
import pygame
pygame.init()
from random import randint, choice

# Configure the screen
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode([screen_width, screen_height])

# Define GameObject class
# Game Object
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image).convert_alpha()
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# Define Apple class
class Apple(GameObject):
 def __init__(self):
   super(Apple, self).__init__(0, 0, 'apple.png')
   self.dx = 0
   self.dy = (randint(0, 100) / 100) + 1
   self.reset() # call reset here! 

 def move(self):
   self.y += self.dy
   # Check the y position of the apple
   if self.y > screen_height: 
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
    if self.x > screen_width:
      self.x = -64 # Start off screen
      self.y = randint(0, 450) # New random y position

  def reset(self):
    lanes = [93, 218, 343]
    self.y = choice(lanes)
    self.x = -64


# Define Player class
class Player(GameObject):
    def __init__(self):
        lanes = [93, 218, 343]
        super(Player, self).__init__(lanes[1], lanes[1], 'player.png')  # Start in the center
        self.lanes = lanes
        self.dx = self.x  # Target x position
        self.dy = self.y  # Target y position

    def left(self):
        if self.x > self.lanes[0]:  # Check if not already in the leftmost lane
            self.dx = self.lanes[self.lanes.index(self.x) - 1]  # Set target to the previous lane

    def right(self):
        if self.x < self.lanes[-1]:  # Check if not already in the rightmost lane
            self.dx = self.lanes[self.lanes.index(self.x) + 1]  # Set target to the next lane

    def up(self):
        if self.y > self.lanes[0]:  # Check if not already in the topmost lane
            self.dy = self.lanes[self.lanes.index(self.y) - 1]  # Set target to the previous lane

    def down(self):
        if self.y < self.lanes[-1]:  # Check if not already in the bottommost lane
            self.dy = self.lanes[self.lanes.index(self.y) + 1]  # Set target to the next lane

    def move(self):
        # Smoothly move the player to the target position using an easing function
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

        # Snap to target position when close enough
        if abs(self.x - self.dx) < 1:
            self.x = self.dx
        if abs(self.y - self.dy) < 1:
            self.y = self.dy


# Make instances of sprites
player = Player()
falling_apple = [Apple() for _ in range(3)]
moving_strawberry = [Strawberry() for _ in range(2)]

# Make a group
all_sprites = pygame.sprite.Group()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(falling_apple)
all_sprites.add(moving_strawberry)

# Grid setup
grid_size = 3
spacing = 64 + 75 # 64 pixels for image size, 100 pixels for spacing
total_width = (grid_size - 1) * spacing + 64
total_height = (grid_size - 1) * spacing + 64
start_x = (screen_width - total_width) / 2
start_y = (screen_height - total_height) / 2

# Create a 3x3 grid of GameObjects
objects = [
    GameObject(start_x + col * spacing, start_y + row * spacing,
               'apple.png' if (row + col) % 2 == 0 else 'strawberry.png')
    for row in range(grid_size)
    for col in range(grid_size)
]
    
# Get the clock
clock = pygame.time.Clock()

# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
        elif event.key == pygame.K_LEFT:
            player.left()
        elif event.key == pygame.K_RIGHT:
            player.right()
        elif event.key == pygame.K_UP:
            player.up()
        elif event.key == pygame.K_DOWN:
            player.down()

  # Clear screen
  screen.fill((255, 255, 255))

  # Render game objects in grid
  for obj in objects:
    obj.render(screen)

  # Move and render all sprites
  for entity in all_sprites:
     entity.move()
     entity.render(screen)

  # Set the frame rate
  clock.tick(60)

  # Update the window
  pygame.display.flip()


# Quit pygame
pygame.quit()