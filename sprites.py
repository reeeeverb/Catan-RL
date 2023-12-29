import pygame

class Resource_Card(pygame.sprite.Sprite):
    def __init__(self):
        super(Resource_Card, self).__init__()
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/lumber.png").convert(),.25)
        self.rect = self.surf.get_rect()
