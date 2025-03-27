import pygame

print("Setup Started")
pygame.init()
screen = pygame.display.set_mode((800, 600))
print("Setup Finished")

print("Loop Started")
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting...")
            pygame.quit() #Close Game
            quit() #End game
