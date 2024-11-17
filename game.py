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


# Define Player class with animations
class Player(GameObject):
    def __init__(self):
        # Load animation frames
        self.frames = {
            "idle": [pygame.image.load(f"player_idle_{i}.png").convert_alpha() for i in range(2)],
            "move_left": [pygame.image.load(f"player_left_{i}.png").convert_alpha() for i in range(2)],
            "move_right": [pygame.image.load(f"player_right_{i}.png").convert_alpha() for i in range(2)],
            "move_up": [pygame.image.load(f"player_up_{i}.png").convert_alpha() for i in range(2)],
            "move_down": [pygame.image.load(f"player_down_{i}.png").convert_alpha() for i in range(2)],
        }
        self.current_frame = 0
        self.animation_speed = 0.1
        self.time_since_last_frame = 0
        self.current_animation = "idle"

        lanes = [93, 218, 343]
        super(Player, self).__init__(lanes[1], lanes[1], self.frames["idle"][0])  # Start in the center
        self.lanes_x = lanes
        self.lanes_y = lanes
        self.current_x_lane = 1
        self.current_y_lane = 1

    def update_animation(self, dt):
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.animation_speed:
            self.time_since_last_frame = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames[self.current_animation])
            self.surf = self.frames[self.current_animation][self.current_frame]

    def left(self):
        if self.current_x_lane > 0:
            self.current_x_lane -= 1
        self.x = self.lanes_x[self.current_x_lane]
        self.current_animation = "move_left"

    def right(self):
        if self.current_x_lane < len(self.lanes_x) - 1:
            self.current_x_lane += 1
        self.x = self.lanes_x[self.current_x_lane]
        self.current_animation = "move_right"

    def up(self):
        if self.current_y_lane > 0:
            self.current_y_lane -= 1
        self.y = self.lanes_y[self.current_y_lane]
        self.current_animation = "move_up"

    def down(self):
        if self.current_y_lane < len(self.lanes_y) - 1:
            self.current_y_lane += 1
        self.y = self.lanes_y[self.current_y_lane]
        self.current_animation = "move_down"

    def reset_animation(self):
        self.current_animation = "idle"

# Make an instance of Player
player = Player()

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
start_x = (screen_width - total_width) / 2
start_y = (screen_height - total_height) / 2

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

  # Move and render falling apple
  for apple in falling_apple:
    apple.move()
    apple.render(screen)

  # Move and render moving strawberry
  for strawberry in moving_strawberry:
    strawberry.move()
    strawberry.render(screen)

  # Draw player 
  player.render(screen)

  # Set the frame rate
  clock.tick(60)

  # Update the window
  pygame.display.flip()


# Quit pygame
pygame.quit()