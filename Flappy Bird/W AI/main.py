import pygame
import random
import os
import neat
pygame.font.init()

# Declaring the Screen Dimensions
SCREENHEIGHT = 800
SCREENWIDTH = 500
WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# Importing the images
BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]
PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))
BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))
BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))
font = pygame.font.SysFont("LM ROMAN 12", 20)

class Bird:

    IMAGES = BIRD_IMAGES
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        """
        Initializes the object, of the class Bird
        :param x: Starts off at x
        :param y: Starts off at y
        :return: None, as the function only initializes the object
        """
        self.x = x # X Coordinate
        self.y = y # Y Coordinate
        self.tilt = 0 # Degrees to tilt
        self.tick_count = 0 # Physics of the bird, similar to time, we will see this just after a few moments, where we will get more deep understanding of it.
        self.velocity = 0 # Bird Velocity in 'Y' axes
        # One thing that's necessary to remember in the flappy bird game, is that, in this game, the bird don't move in 'X' axes, it only moves in 'Y' axes.
        # The pipes moves from the right to the left, which creates an illusion that the bird is moving forward...LOL.
        self.height = self.y # Physics of the bird, similar to displacement, we will see this just after a few moments, where we will get more deep understanding of it.
        self.img_count = 0 # Since, we are using 3 images, for the birds, i.e, flaps up, flaps flat, flaps down, we need to maintain a variable that could guide us, which image to use.
        self.img = self.IMAGES[0] # Bird1.png, flaps up position.

    def jump(self):
        """
        Makes the Bird Jump, or in just terms, move along Y axes when the bird flaps
        :return: None
        """
        self.velocity = -10.5 # Velocity of ascent...Note that the Velocity is negative, as in pygame the coordinate system is like:
        # -------------------------> X
        # |
        # |
        # |
        # |
        # |
        # |
        # Y
        self.tick_count = 0 # Physics of the bird, similar to time, we will see this just after a few moments, where we will get more deep understanding of it.
        self.height = self.y # Updates the height of the bird after flapping, or jumping

    def move(self):
        """
        Makes the Bird Move by law of gravity, when it's not flapping
        :return: None
        """
        self.tick_count = self.tick_count + 1
        # In Physics, we learned about Laws of Motion,
        # The Second Law was s = ut + (1/2) * a * t * t
        # where,
        # s = displacement or height
        # u = initial velocity
        # t = time
        # a = acceleration or gravity
        d = (((self.velocity) * (self.tick_count)) + (0.5 * 3 * (self.tick_count) * (self.tick_count)))
        # self.velocity <- initial velocity (u)
        # self.tick_count <- time (t)
        # 3 <- acceleration (a) or gravity
        # d <- displacement
        if d >= 16:
            d = 16 # Stabilizing (similar to terminal velocity)

        if d < 0:
            d -= 2 # Increment on jumps

        self.y = self.y + d # Updated position of the bird

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self. MAX_ROTATION # Keep the bird titled at it's MAX_ROTATION, till it catches with the required gradient of ascent
                # Or in simple words keeps the bird titled till it's having a negative displacement from the point where it starts from.
        else:
            if self.tilt > -90:
                self.tilt -= self. ROTATION_VELOCITY # Makes sure that the bird don't show some weird rotations

    def draw (self, win):
        """
        Draws the flappy bird
        :param win: pygame window
        :return: None
        """
        self.img_count += 1 # As mentioned earlier, it keeps count of which bird images is to blitted

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMAGES[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMAGES[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMAGES[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMAGES[1]
        elif self.img_count < self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMAGES[0]
            self.img_count = 0 # Reset count

        if self.tilt <= -80: # If the rotation exceeds 80 degrees, or with more visualization, if the bird's nose tends to face directly to the ground blit the image with flat flaps
            self.img = self.IMAGES[1]
            self.img_count = self.ANIMATION_TIME * 2

        # Rotate image about it's centre of mass in pygame
        # https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        """
        Gets the mask for the current image of the bird
        :return: None
        """
        return pygame.mask.from_surface(self.img)
        # Will be used in checking collisions
        # Generally, for collisions, we keep a check of it by square shaped boxes, by considering all the pixels enclosed in the box as a whole.
        # But this increases chances of error. Even if there is no collision, the bird may give True output on Collsion Check. The
        # So, we make use of the mask attribute present in pygame library that checks exact match

class Pipe():

    GAP = 200 # Minimum Gap between two pipes
    VELOCITY_PIPE = 5 # This velocity will be towards the left

    def __init__(self, x):
        """
        Initializes Pipes
        """
        # Only 'X' coordinate is relevant as the Y coordinates of the pies are generated randomly
        self.x = x # 'X' Coordinate
        self.height = 0 # Displacement
        self.top = 0 # Initial blitting ordinate for the upper pipe.
        self.bottom = 0 # Initial blitting ordinate for the lower pipes.
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMAGE, False, True) # The Upper Pipe is obtained by flipping the pipe
        self.PIPE_BOTTOM = PIPE_IMAGE # This is the Lower Pipe

        self.passed = False # This boolean variable keeps track whether the bird has crossed the randomly generated pipe.
        self.set_height()

    def set_height(self):
        """
        Sets the height of the pipes from the top of the screen
        :return: None
        """
        self.height = random.randrange(50, 450) # Randomly generating a height
        self.top = self.height - self.PIPE_TOP.get_height() # Height of the upper pipe.
        self.bottom = SCREENHEIGHT + self.top # Height of the lower pipe.

    def move(self):
        """
        Move the pipe based on velocity
        :return: None
        """
        self.x = self.x - self.VELOCITY_PIPE # Moves the pipe towards <-

    def draw(self, win):
        """
        Draw the upper and lower pipes
        :param win: pygame window
        :return: None
        """
        win.blit(self.PIPE_TOP, (self.x, self.top)) # Draw the Upper Pipe
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom)) # Draw the Lower Pipe

    def collide(self, bird, win):
        """
        Returns the result - whether the bird collides with the pipe or not.
        :param bird: The object Bird
        :param win: The Window
        :return: Boolean Value
        """
        bird_mask = bird.get_mask() # The Bird Mask
        top_mask = pygame.mask.from_surface(self.PIPE_TOP) # The Top Pipe Mask
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM) # The Bottom Pipe Mask
        top_offset = self.x - bird.x, self.top - round(bird.y) # Offset tuple for Upper Pipe
        bottom_offset = self.x - bird.x, self.bottom - round(bird.y) # Offset tuple for Lower Pipe
        b_point = bird_mask.overlap(bottom_mask, bottom_offset) # Boolean Values that check for o'erlaps
        t_point = bird_mask.overlap(top_mask, top_offset) # Boolean Values that check for o'erlaps

        if t_point or b_point: # If any of the boolean values is true, return true as the output of the function
            return True

        return False

class Base:

    VELOCITY_BASE = 5 # The Velocity with which the base will move, which in turn will create real illusion of the bird's motion in  <-> directions
    BASE = BASE_IMAGE # Using the image
    WIDTH_BASE = BASE.get_width() # Getting the width of the base

    def __init__(self, y):
        """
        Initializes the base
        :param y: Integer
        """
        self.y = y # The 'Y' Coordinate of the Base
        # Now, since, the Base image have fixed width, we will have to blit it again and again on the screen.
        # We will work little greedy here
        # We will be using two instances of the base image, and arrange them one after another
        # The Y Coordinate of both will be same.
        self.x1 = 0 # The 'X' Coordinate of the first Base Image
        self.x2 = self.WIDTH_BASE # The 'X' Coordinate of the second Base Image

    def move(self):
        """
        Make the base appear to move
        :return: None
        """
        self.x1 = self.x1 - self.VELOCITY_BASE # Moving the 1'st instance towards the left <-
        self.x2 = self.x2 - self.VELOCITY_BASE # Moving the 2'st instance towards the left <-
        # Once the first image gets completely out of the screen, we will pop it from the beginning and push it at the end
        if self.x1 + self.WIDTH_BASE < 0:
            self.x1 = self.x2 + self.WIDTH_BASE
        if self.x2 + self.WIDTH_BASE < 0:
            self.x2 = self.x1 + self.WIDTH_BASE

    def draw(self, win):
        """
        Blitting the base images
        :param win: pygame window
        :return: None
        """
        win.blit(self.BASE, (self.x1, self.y))
        win.blit(self.BASE, (self.x2, self.y))

def draw_window(win, birds, base, pipes, score):
    """
    :param win: pygame window
    :param birds: All the birds generated by the NEAT Algorithm for a given generation
    :param base: The Base Object
    :param pipes: All the pipes generated by the randomized algorithm.
    :param score: The Current Score of the AI Algorithm (who is the player in this case)
    :return: None
    """
    # Lets blit our sprites Now
    # the order, we will follow for blitting, is
    # 1. Background
    # 2. Obstacles
    # 3. Player
    win.blit(BACKGROUND_IMAGE, (0, 0))
    for pipe in pipes:
        pipe.draw(win)
    screen_text = font.render("SCORE: " + str(score), True, (0, 0, 0)) # Blitting the score
    win.blit(screen_text, [SCREENWIDTH - 300, 10])
    base.draw(win)
    for bird in birds:
        bird.draw(win) # Blitting all the birds
    pygame.display.update() # Updating the display

def fitness_function(genomes, config):
    """
    Runs the simulation of the current population of birds and sets their fitness based on the distance they reach in the game.
    :param genomes: List of all the birds generated by the NEAT Algorithm for a given population, these are simply bunch of neural networks
    :param config: Configuration File for the NEAT Algorithm
    :return: None
    """
    # Whenever we are creating fitness function for NEAT, we need to make sure that there is genomes and config.
    # It's like the minimal requisites for the function.
    global WIN # Declaring the game window globally
    win = WIN # locally declaring a descent

    nets = [] # Used to keep track of the Algorithmic Instances
    ge = [] # Used to keep track of the Algorithmic Instances
    birds = [] # List of the whole population of the birds

    for genome_id, genome in genomes: # Setting up the Neural Network
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net) # Append net to nets
        birds.append(Bird(230, 350)) # Initialize the Bird on the basis of it's X and Y Coordinate
        genome.fitness = 0 # Make the fitness value of each neurons to be Zero initially
        ge.append(genome) # Append genome to list of genomes

    SCORE = 0 # Declaring the Score, which is initially 0
    pipes = [Pipe(700)] # Instantiates the Pipe Class by passing the 'X' coordinate which marks the beginning of the pipe, And in turn, the random pipes are generated.
    base = Base(730) # Spawning the base at a depth of 730 in the Game Window (800 x 500)
    clock = pygame.time.Clock() # General Etiquette for PyGame

    run = True # Instantiate for the Game Loop boolean

    # Game Loop
    while run:

        clock.tick(60) # Frames Per Second = 60
        for event in pygame.event.get(): # This is the general Event Get loop
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)): # If the cross button in the game window is pressed or ESCAPE key is pressed, break the game loop and go to sleep. :-)
                run = False # Making the Game Loop Boolean False
                pygame.quit() # Quiting the PyGame Window
                quit() # Quit the Python 3.9 Terminal

        pipe_ind = 0
        if len(birds) > 0:
            if len(birds) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break
        # Enumerate method comes with an automatic counter / index to each of the items present in to Enumerate list
        # in Python. The first-index value will start from 0. You can also specify the start index by using the optional
        # parameter startIndex in enumerate
        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.05 # Increase Fitness of Each Genome by 0.05
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom))) # Output Function, based on which, we will make our decision of jumping or not jumping

            if output[0] > 0.5:
                bird.jump() # Telling the bird to jump.

        add_pipe = False
        remove = []
        # Enumerate method comes with an automatic counter / index to each of the items present in to Enumerate list
        # in Python. The first-index value will start from 0. You can also specify the start index by using the optional
        # parameter startIndex in enumerate
        for pipe in pipes: # Looping for all the pipes
            for x, bird in enumerate(birds): # Looping for all the birds
                if pipe.collide(bird, win): # Checking for Collision
                    ge[x].fitness -= 1 # If any of the bird amongst the population collides, decrease it's Fitness Value by 1
                    birds.pop(x) # Flushing away the bird
                    nets.pop(x) # Flushing away the attribute of the bird from 'nets' list.
                    ge.pop(x) # Flushing away the attribute of the bird from 'ge' list.
                if not pipe.passed and pipe.x < bird.x: # Check whether the bird has crossed the pipe or not
                    pipe.passed = True
                    add_pipe = True # It it has crossed, spawn another pipe.

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                    remove.append(pipe) # Appending the Pipe back to the list of pipes to be removed.
            pipe.move()

        if add_pipe: # Pipe is added, that means atleast one pipe is crossed...So, score has to be updated
            SCORE += 1 # Increment score
            for g in ge:
                g.fitness += 5 # Increment fitness for each bird in the population by 5.
            pipes.append(Pipe(700)) # Spawning a new pipe with randomized algorithm and append it to the list of pipes.

        for r in remove:
            pipes.remove(r) # Remove all pipes
        # Enumerate method comes with an automatic counter / index to each of the items present in to Enumerate list
        # in Python. The first-index value will start from 0. You can also specify the start index by using the optional
        # parameter startIndex in enumerate
        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0: # If any of the bird hit the base or the zenith, pop them
                birds.pop(x)  # Flushing away the bird
                nets.pop(x)  # Flushing away the attribute of the bird from 'nets' list.
                ge.pop(x)  # Flushing away the attribute of the bird from 'ge' list.

        base.move() # Calling the move instance of the class Base
        draw_window(win, birds, base, pipes, SCORE) # Calling the draw_window function declared above

def run(config_file):

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)
    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # These lines prints the stats in the terminal...They are optional
    p.add_reporter(neat.StdOutReporter(True) )# Optional
    stats = neat.StatisticsReporter() # Optional
    p.add_reporter(stats) # Optional

    # Run for up to 50 generations.
    winner = p.run(fitness_function, 50)

    # These lines prints the stats in the terminal...They are optional
    print('\nBest genome:\n{!s}'.format(winner)) # Optional

if __name__ == "__main__": # Staring Point

    # Fetches the config file of the NEAT algorithm used in this instance
    local_dir = os.path.dirname(__file__) # Fetching
    config_path = os.path.join(local_dir, 'config-feedforward.txt') # Merging
    run(config_path) # Calling the run method by passing the config file