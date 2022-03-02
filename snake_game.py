import pygame,random

a = pygame.init()

#Game loop
def game_loop():
    #Game specification (GS):
    #GS-1 Windows height and width
    window_width_x = 800
    window_height_y = 400
    #GS-2 Exit and Game-over event
    game_exit = False
    game_over = False

    #GS-3 Colors
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    #GS-4 Creating a snake
    starting_position_x = 50
    starting_position_y = 50
    snake_width_x = 20
    sanke_height_y = 20
    #GS-5 Creating clock and fps
    clock = pygame.time.Clock()
    fps = 30
    #GS-6 Continious movement of snake
    velocity_x = 0
    velocity_y = 0
    snake_speed = 5
    #GS-7 Creating food
    food_x = random.randint(20, window_width_x) / 3
    food_y = random.randint(20, window_height_y) / 3
    #GS-8 Score
    score = 0

    #Creating a Game-window and title
    game_window = pygame.display.set_mode((window_width_x, window_height_y))
    pygame.display.set_caption("NH-Game")
    font = pygame.font.SysFont(None,50,True,False)

    snk_list = []
    snk_length = 1

    def scoreboard(score,color,x,y):
        sc_tx = font.render(score, True, color)
        game_window.blit(sc_tx,[x,y])

    def snake_plot(game_window,green,snk_list,snake_width_x,sanke_height_y):
        for x,y in snk_list:
            # print(snk_list)
            pygame.draw.rect(game_window,green,[x,y,snake_width_x,sanke_height_y]) 
    def food_plot(game_window,color,food_x,food_y,snake_width_x,sanke_height_y):
        pygame.draw.rect(game_window,red,[food_x,food_y,snake_width_x,sanke_height_y]) 

    while game_exit!=True:
        
        # List of Events
        if game_over:
            game_window.fill(black)
            scoreboard("GAME-OVER", red, 250, 100)
            scoreboard("Press Enter to continue", red, 150, 155)
            scoreboard("Press Esc to exit", red, 200, 200)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
        else:
            for event in pygame.event.get():
                #print(event)
                #Game exit evnt
                if event.type == pygame.QUIT:
                    game_exit = True
                #Movement of snake
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT :
                        velocity_x += snake_speed
                        velocity_y = 0
                    if event.key == pygame.K_LEFT :
                        velocity_x -= snake_speed
                        velocity_y = 0
                    if event.key == pygame.K_UP :
                        velocity_y -= snake_speed
                        velocity_x = 0
                    if event.key == pygame.K_DOWN :
                        velocity_y += snake_speed                
                        velocity_x = 0
            #Continuous movement of snake
            starting_position_x += velocity_x
            starting_position_y += velocity_y
            #Eating Food
            if abs(food_x - starting_position_x) < 15 and abs(food_y - starting_position_y) < 15:
                food_x = random.randint(20, window_width_x) / 2
                food_y = random.randint(20, window_height_y) / 2
                score += 10
                snk_length += 1
               
                
            head = []
            head.append(starting_position_x)
            head.append(starting_position_y)
            
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
                # print(score)
            if starting_position_x < 0 or starting_position_x > window_width_x or starting_position_y < 0 or starting_position_y > window_height_y:
                game_over = True


            if head in snk_list[:-1]:
                game_over = True
           
            #Background color
            game_window.fill(black)  
            #Displaying snake and food 
            food_plot(game_window,red,food_x,food_y,snake_width_x,sanke_height_y) 
            snake_plot(game_window,green,snk_list,snake_width_x,sanke_height_y) 
            #Cordinates
                 
            scoreboard("Score : "+str(score),white,5,5)
        pygame.display.update()
        clock.tick(fps)

game_loop()