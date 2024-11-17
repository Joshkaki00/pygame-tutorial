# Import and initialize pygame
import pygame
from random import randint, choice
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Lanes
lanes = [93, 218, 343]

# Game Object
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image).convert_alpha()
    self.x = x
    self.y = y
    self.rect = self.surf.get_rect()

  def render(self, screen):
    self.rect.x = self.x
    self.rect.y = self.y
    screen.blit(self.surf, (self.x, self.y))

  def move(self):
    pass

# Define Apple class
class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.rect.y += self.dy
    if self.rect.y > 500:  # Reset when off-screen
      self.reset()

  def reset(self):
    self.rect.x = choice(lanes)
    self.rect.y = -64

# Define Strawberry class
class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.rect.x += self.dx
    if self.rect.x > 500:  # Reset when off-screen
      self.reset()

  def reset(self):
    self.rect.x = -64
    self.rect.y = choice(lanes)

# Define Bomb class
class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'bomb.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.rect.x += self.dx
    if self.rect.x > 500:  # Reset when off-screen
      self.reset()

  def reset(self):
    self.rect.x = -64
    self.rect.y = choice(lanes)

# Define Player class
class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    self.pos_x = 1
    self.pos_y = 1
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
    self.update_position()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
    self.update_position()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
    self.update_position()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
    self.update_position()

  def move(self):
    self.rect.x -= (self.rect.x - self.dx) * 0.25
    self.rect.y -= (self.rect.y - self.dy) * 0.25

    if abs(self.rect.x - self.dx) < 1:
      self.rect.x = self.dx
    if abs(self.rect.y - self.dy) < 1:
      self.rect.y = self.dy

  def reset(self):
    self.rect.x = lanes[self.pos_x]
    self.rect.y = lanes[self.pos_y]
    self.dx = self.rect.x
    self.dy = self.rect.y

  def update_position(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]


# Make instances of sprites
player = Player()
apple = Apple()
strawberry = Strawberry()
bomb = Bomb()

# Make a group
all_sprites = pygame.sprite.Group(player, apple, strawberry, bomb)

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

  # Move and render all sprites
  for entity in all_sprites:
    entity.move()
    screen.blit(entity.surf, entity.rect.topleft)

  # Set the frame rate
  clock.tick(60)

  # Update the window
  pygame.display.flip()


# Quit pygame
pygame.quit()