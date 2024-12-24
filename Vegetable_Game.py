import pygame
import random as rn

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vegetable Game")
pygame.display.set_icon(pygame.image.load('icon.jpg'))

background_image = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(background_image, (screen_width, screen_height))

vegetables_list = [pygame.image.load(f"Asset\\{i}.png") for i in range(1, 48)]
scaled_vegetables_list = [pygame.transform.scale(veg, (60, 60)) for veg in vegetables_list]


pygame.mixer.music.load("background_music.mp3")  
pygame.mixer.music.set_volume(0.1)  
pygame.mixer.music.play(-1)  


class Vegetable:
    def __init__(self):
        self.image = rn.choice(scaled_vegetables_list)  
        self.x = rn.randint(50, 750)  
        self.y = rn.randint(50, 550)  

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def collide(self, player_rect):
        
        veg_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return player_rect.colliderect(veg_rect)


class Player:
    def __init__(self):
        self.image = pygame.image.load("Player.jpg")  
        self.image = pygame.transform.scale(self.image, (60, 60)) 
        self.x = 100
        self.y = 50
        self.v = 5

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0: 
            self.x -= self.v
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.image.get_width(): 
            self.x += self.v
        if keys[pygame.K_UP] and self.y > 0: 
            self.y -= self.v
        if keys[pygame.K_DOWN] and self.y < screen_height - self.image.get_height():  
            self.y += self.v


score = 0
time_limit = 60
font = pygame.font.SysFont(None, 30)


def display_score(score, time_left):
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  
    time_text = font.render(f"Time: {time_left}s", True, (0, 0, 0))  
    screen.blit(score_text, (10, 10))  
    screen.blit(time_text, (screen_width - 100, 10))  


vegetables = [Vegetable() for _ in range(10)]  


player = Player()


def display_game_over(message):
    game_over_font = pygame.font.SysFont(None, 60)
    restart_font = pygame.font.SysFont(None, 40)

    game_over_text = game_over_font.render(message, True, (255, 0, 0))  
    restart_text = restart_font.render("Press 'R' to Play Again or 'Q' to Quit", True, (0, 0, 0))

    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
    screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2))


running = True
clock = pygame.time.Clock()


start_ticks = pygame.time.get_ticks()  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000  
    time_left = time_limit - seconds  

    
    if time_left <= 0:
        if score >= 100:
            display_game_over("You Won!")
        else:
            display_game_over("Game Over!")
        pygame.display.update()

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:  
            score = 0
            time_left = time_limit
            start_ticks = pygame.time.get_ticks()
            vegetables = [Vegetable() for _ in range(5)]  
            player = Player() 
        elif keys[pygame.K_q]:  
            running = False
        continue

    
    screen.blit(bg, (0, 0))

    
    keys = pygame.key.get_pressed()

    
    player.move(keys)

    
    for veg in vegetables:
        veg.draw()
        
        if veg.collide(pygame.Rect(player.x, player.y, player.image.get_width(), player.image.get_height())):
            vegetables.remove(veg)  
            
            vegetables.append(Vegetable())
            
            score += 1
        

    
    player.draw()

    
    display_score(score, time_left)

    
    pygame.display.update()

    
    clock.tick(60)

pygame.quit()
