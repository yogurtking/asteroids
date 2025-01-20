from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)  # Store position as a Vector2!
        self.velocity = pygame.Vector2(0, 0)  # Default velocity

    def draw(self, screen):
        # pygame.draw.circle(surface, color, (x,y), radius, width)
        pygame.draw.circle(screen, WHITE, self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)