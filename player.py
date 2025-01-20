from constants import *
from circleshape import *
from shots import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    # copied from boot.dev
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # draw the ship
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)
    
    # allow the ship to rotate
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

     # increase or decrease speed, not sure how this part works 
     #       
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.shot_timer <= 0:
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)  # Create shot at player's position
            forward = pygame.Vector2(0, 1).rotate(self.rotation)         # Calculate forward direction
            bullet.velocity = forward * PLAYER_SHOOT_SPEED               # Set bullet's velocity
            self.shot_timer = PLAYER_SHOOT_COOLDOWN