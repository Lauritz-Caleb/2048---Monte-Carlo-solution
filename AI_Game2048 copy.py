# Game 2048: Artificial intelligence

# Instructions:
#   Move up, down, left, or right to merge the tiles. The objective is to 
#   get a tile with the number 2048 (or higher)
#
# Control:
#    arrows  : Merge up, down, left, or right
#    r       : Restart game
#    q / ESC : Quit

from Game2048 import Game2048
import numpy as np
import pygame




finalscore = []



succes = 0

rounds = 10

simrounds = 50

for p in range(rounds):
    env = Game2048()
    env.reset()
    actions = ['left', 'right', 'up', 'down']
    exit_program = False
    action_taken = False

    done = False
    sim_done = False

    maxlist = {}

    timer = 0

    while not exit_program:
        pygame.event.pump()

        while not done:
            #env.render()
            cur_list = []
            for attempt in ['left', 'right', 'up', 'down']:
                maxlist[attempt] = 0
                for i in range(simrounds):
                    sim = Game2048((env.board, env.score))
                    (board, score), reward, sim_done = sim.step(attempt)
                    while not sim_done:
                        action = actions[np.random.randint(0, 4)]
                        (board, score), reward, sim_done = sim.step(action)
                    maxlist[attempt] += score
            act = max(maxlist, key=maxlist.get)
            print(f'still going on round {timer}')
            timer += 1

            action_taken = True
            if action_taken:
                (board, score), reward, done = env.step(act)
                action_taken = False    
                 
        if np.max(env.board) >= 2048: # 2**11=2048
            succes +=1
        finalscore.append(score)
        
        exit_program = True
    env.close()
    #pygame.display.quit()
    print(f'score({p}/{rounds}) = {score}' )
    
print(f'Mean({rounds}) = {np.mean(finalscore)}')
print(f'Succes = {succes/rounds}')
    

