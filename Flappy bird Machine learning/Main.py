import pygame
import neat
import time
import os
import random
pygame.font.init()

win_width = 500#if you want to make to second monitior make 2000 with 800 height to see it all
win_height = 700#also you can go for settings of displaymint and make to show onlu on 2

gen = 0

bird_imgs = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
bg_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

stat_font = pygame.font.SysFont("comicsans", 40)
stat_font_small = pygame.font.SysFont("comicsans", 20)

class Bird:
    imgs = bird_imgs
    max_rotation = 25
    rot_velocity =20
    anime_time = 5

    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count =0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.imgs[0]
    
    def jump(self):
        self.vel = -5.5
        self.tick_count = 0
        self.height = self.y
    
    def move(self):
        self.tick_count += 1

        d = displacement = self.vel*(self.tick_count) + 0.5*(3)*(self.tick_count)**2

        if d >= 16:
            d = (displacement/abs(displacement)) * 16
        
        if d < 0 :
            d -= 2

        self.y += d#self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.max_rotation:
                self.tilt = self.max_rotation
        #else:#i hate that additional tap it took me a lot of work to guess what is wrong
        elif self.tilt > -90:#it is a loop when no jumps so it keeps going in loosing degrese tell it hits a smaller than -90 
            self.tilt -= self.rot_velocity

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.anime_time:
            self.img = self.imgs[0]
        elif self.img_count < self.anime_time*2:
            self.img = self.imgs[1]
        elif self.img_count < self.anime_time*3:
            self.img = self.imgs[2]
        elif self.img_count < self.anime_time*4:
            self.img = self.imgs[1]
        elif self.img_count == self.anime_time*4 + 1:
            self.img = self.imgs[0]
            self.img_count = 0
        
        if self.tilt <= -80:
            self.img = self.imgs[1]
            self.img_count = self.anime_time*2
        
        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_img, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe():
    gap = 200#(200)
    vel = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img

        self.passed = False
        
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.gap

    def move(self):
        self.x -= self.vel
    
    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))#you can chose to use it or not it is the red lines
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True

        return False

class Base:
    VEL = 5
    WIDTH = base_img.get_width()
    IMG = base_img

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


class background:
    VEL = 5
    WIDTH = bg_img.get_width()
    IMG = bg_img

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))




def draw_window(win, birds, pipes, base, score, gen, pipe_ind, fitness, bg):
    if gen == 0:
        gen = 1
    win.blit(bg_img, (0,0))
    
    for pipe in pipes:
        pipe.draw(win)

    #bg.draw(win)
    base.draw(win)
   
    for bird in birds:
        #to draw lines from bird to pipe
        DRAW_LINES = True

        if DRAW_LINES:#you can chose to use it or not it is the red lines
            try:
                pygame.draw.line(win, (255,0,0), (bird.x+bird.img.get_width()/2, bird.y + bird.img.get_height()/2), (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_TOP.get_width()/2, pipes[pipe_ind].height), 5)
                pygame.draw.line(win, (255,0,0), (bird.x+bird.img.get_width()/2, bird.y + bird.img.get_height()/2), (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_BOTTOM.get_width()/2, pipes[pipe_ind].bottom), 5)
            except:
                pass

        bird.draw(win)

    text = stat_font.render("Score: " + str(score), 1,(255,255,255))  
    win.blit(text, (win_width - 10 - text.get_width(), 10))

    score_label = stat_font_small.render("Gens: " + str(gen-1),1,(255,255,255))
    win.blit(score_label, (10, 10))

    score_label = stat_font_small.render("Alive: " + str(len(birds)),1,(255,255,255))
    win.blit(score_label, (10, 25))

    score_label = stat_font_small.render("Fitness: " + str(fitness),1,(255,255,255))
    win.blit(score_label, (10, 50))
 
    pygame.display.update()

def main(genomes, config):
    global gen 
    fitness = 0
    gen += 1
    nets = []
    ge = []
    birds = []
    
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230,350))
        g.fitness = 0  # start with fitness level of 0
        ge.append(g)

    bg = background(0)
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((win_width,win_height))
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_icon(bird_imgs[1])
    clock = pygame.time.Clock()

    score = 0
    run = True
    while run and len(birds) > 0:
        clock.tick(30)#how fast is it going
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1  
        
        fitness += 0.1

        for x, bird in enumerate(birds):  
            ge[x].fitness += 0.1
            bird.move()
            
            output = nets[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:  
                bird.jump()
                
        bg.move()
        base.move()
        
        rem = goedn_rmzi_theChif_faliuers = []
        add_pipe = False
        for pipe in pipes:
            pipe.move()
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -= 1
                    nets.pop(x)
                    ge.pop(x)
                    birds.pop(x)

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

        if add_pipe:
            score += 1 
            fitness += 5
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(700))   
        
        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() - 10 >= 730 or bird.y < -50:
                nets.pop(x)
                ge.pop(x)
                birds.pop(x)
        draw_window(win, birds, pipes, base, score, gen, pipe_ind, fitness, bg)

        if score >= 50:
            #break
            print("stop")
            #nets.pop(x)
            #ge.pop(x)
           # birds.pop(x)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run for up to 50 generations.and stop
    winner = p.run(main, 30)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))



if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
