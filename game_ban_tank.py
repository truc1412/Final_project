import pygame
import time
import random

pygame.init()

#Khởi tạo màn hình 
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))


pygame.display.set_caption('GAME BẮN XE TĂNG')

#Định nghĩa màu
wheat=(245,222,179)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0,0,255)
brown=(150,75,0)
red = (200, 0, 0)
light_red = (255, 0, 0)
pink=(255,192,203)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

clock = pygame.time.Clock()
#Kích thước xe tăng
tankWidth = 40
tankHeight = 20
#Kích thước tháp pháo và bánh xe tăng
turretWidth = 5
wheelWidth = 5
#Độ dày mặt đát
ground_height = 35
#Thiết lập font chữ

smallfont = pygame.font.SysFont("Times new Roman", 25)
medfont = pygame.font.SysFont("Times new Roman", 50)
largefont = pygame.font.SysFont("Times new Roman", 75)
#Khởi tạo đối tượng văn bản
def setup_text(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    
    return textSurface, textSurface.get_rect()

# Text trong nút nhấn
def text_button(msg, color, button_x, button_y, button_width, button_height, size="small"):
    textSurf, textRect = setup_text(msg, color, size)
    textRect.center = ((button_x + (button_width / 2)), button_y + (button_height / 2))
    gameDisplay.blit(textSurf, textRect)
    
#Text trên màn hình
def message_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = setup_text(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)

#Thiết lập nút nhấn
def button(text, x, y, width, height, inactive_color, active_color, action=None,size=" "):
    #Vị trí con trỏ chuột
    cur = pygame.mouse.get_pos()
    #Lấy trạng thái con trỏ chuột
    click = pygame.mouse.get_pressed()
    #Hiệu ứng nút nhấn và các sự kiện khi nhấn nút và có chuột đưa vào
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                controls_game()

            if action == "play":
                gameLoop()

            if action == "main":
                intro_game()
    #Hiển thị nút nhấn khi không có chuột đưa vào
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
    #Hiển thị text trong nút nhấn
    text_button(text, black, x, y, width, height)
    
#Màn hình giới thiệu game
def intro_game():
    intro = True
    #Các sự kiện trong vòng lập intro
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    #Nhấn để bắt đầu trò chơi
                    intro = False
                elif event.key == pygame.K_q:
                    #Nhấn để thoát trò chơi
                    pygame.quit()
                    quit()
        #Hiện thị các thông tin trò chơi
        gameDisplay.fill(black)
        message_screen("GAME BẮN XE TĂNG", white, -100, size="large")
        #Hiện thị nút nhấn
        button("Play", 150, 500, 100, 50, wheat, light_green, action="play",size="small")
        button("Controls", 350, 500, 100, 50, wheat, light_yellow, action="controls",size="small")
        button("Quit", 550, 500, 100, 50, wheat, light_red, action="quit",size="small")

        pygame.display.update()

        clock.tick(15)    

#Màn hình hướng dẫn điều khiển
def controls_game():
    gcont = True

    while gcont:
        #Kiểm trab người dùng có tắt ứng dụng không
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #Nhấn "esc" để thoát game
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    #Nhấn "c" để chơi lại game
                    gameLoop()
        #In ra màn hình các hướng dẫn
        gameDisplay.fill(black)
        message_screen("Control", white, -100, size="large")
        message_screen("Fire: Spacebar", wheat, -30)
        message_screen("Move Turret: Up and Down arrows", wheat, 10)
        message_screen("Move Tank: Left and Right arrows", wheat, 50)
        message_screen("Press D to raise Power / Press A to lower Power", wheat, 140)
        message_screen("Pause: P", wheat, 90)
        #Thiết lập nút nhấn
        button("Play", 150, 500, 100, 50, green, light_green, action="play")
        button("Main", 350, 500, 100, 50, yellow, light_yellow, action="main")
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit")
        #Cập nhật các phần hiển thị của màn hình
        pygame.display.update()
        #Tốc độ khung hình
        clock.tick(15)    
        
#Màn hình dừng trò chơi
def pause():
    paused = True
    #In ra thông báo màn hình
    message_screen("Paused", white, -100, size="large")
    message_screen("Press C to continue playing or Q to quit", wheat, 25)
    pygame.display.update()
    #Các sự kiện trong vòng lập paused
    while paused:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Bắt sự kiện nhấn nút
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)
     
#Màn hình khi game over
def game_over():
    game_over = True
    #Các sự kiện trong vòng lập game over
    while game_over:
        for event in pygame.event.get():
          
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #Nhấn "esc" để thoát game
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    #Nhấn "c" để chơi lại game
                    gameLoop()

        gameDisplay.fill(black)
        #Hiển thị thông báo thua cuộc
        message_screen("Game Over", white, -100, size="large")
        message_screen("You died.", wheat, -30)
        #Hiển thị nút nhấn
        button("Play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        button("Controls", 350, 500, 100, 50, wheat, light_yellow, action="controls")
        button("Quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()
        clock.tick(15)     

#Màn hình khi thắng cuộc 
def win_game():
    win = True

    while win:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #Nhấn "esc" để thoát game
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    #Nhấn "c" để chơi lại game
                    gameLoop()

        gameDisplay.fill(black)
        message_screen("You won!", white, -100, size="large")
        message_screen("Congratulations!", wheat, -30)

        button("Play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        button("Controls", 350, 500, 100, 50, wheat, light_yellow, action="controls")
        button("Quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)   
#Bước tường chắn
def wall(xlocation, randomHeight, wall_width):
    pygame.draw.rect(gameDisplay, brown, [xlocation, display_height - randomHeight, wall_width, randomHeight])       
    
# Vẽ xe tăng người chơi
def user_tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x - 27, y - 2),
                       (x - 26, y - 5),
                       (x - 25, y - 8),
                       (x - 23, y - 12),
                       (x - 20, y - 14),
                       (x - 18, y - 15),
                       (x - 15, y - 17),
                       (x - 13, y - 19),
                       (x - 11, y - 21)]

    pygame.draw.circle(gameDisplay, blue, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, blue, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, blue, (x, y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 15, y + 20), wheelWidth)
    return possibleTurrets[turPos]

# Vẽ xe tăng địch
def enemy_tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x + 27, y - 2),
                       (x + 26, y - 5),
                       (x + 25, y - 8),
                       (x + 23, y - 12),
                       (x + 20, y - 14),
                       (x + 18, y - 15),
                       (x + 15, y - 17),
                       (x + 13, y - 19),
                       (x + 11, y - 21)]

    pygame.draw.circle(gameDisplay, red, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, red, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, red, (x, y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, red, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x - 10, y + 20), wheelWidth)

    pygame.draw.circle(gameDisplay, red, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x + 15, y + 20), wheelWidth)

    return possibleTurrets[turPos]

#Hiển thị thanh lực bắn
def power(level):
    text = smallfont.render("Power: " + str(level) + "%", True, wheat)
    gameDisplay.blit(text, [display_width / 2, 0])
    
#Thanh máu của xe tăng người chơi và xe tăng địch       
def health_bars(player_health, enemy_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if enemy_health > 75:
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
        enemy_health_color = red
    
    #Vẽ thanh máu
    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))
    
def gameLoop():
    gameExit = False
    # gameOver = False
    FPS = 15
    #----------Máu------------
    player_health = 100
    enemy_health = 100
    #----------Độ dày của vật cản----------------
    wall_width = 50

    #Vị trí xe tăng
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9

    tankMove = 0
    currentTurPos = 0
    changeTur = 0
    #Vị trí xe tăng địch
    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9
    #Lực bắn mặc định
    fire_power = 50
    power_change = 0


    #Random vị trí vật cản     
    xlocation = (display_width / 2) + random.randint(-0.05 * display_width, 0.05 * display_width)
    #Random chiều cao vật cản  
    randomHeight = random.randrange(display_height * 0.1, display_height * 0.4)

    while not gameExit:
        #Kiểm tra các sự kiện
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()
                
                elif event.key == pygame.K_ESCAPE:
                    gameExit = True
                #--------------------------------------------------------------------------------------------------------------------------------------------------------                        
                elif event.key == pygame.K_SPACE:
                    #Lấy giá trị sất thương
                    damage = fire(gun, currentTurPos, fire_power, xlocation, wall_width, randomHeight, enemyTankX)
                    enemy_health -= damage
                    
                    #Thực hiện việc di chuyển
                    possibleMovement = ["forward", "backward"]
                    moveIndex = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):

                        if display_width * 0.3 > enemyTankX and enemyTankX > display_width * 0.03:
                            if possibleMovement[moveIndex] == "forward":
                                enemyTankX += 5
                            elif possibleMovement[moveIndex] == "backward":
                                enemyTankX -= 5

                            gameDisplay.fill(black)
                            health_bars(player_health, enemy_health)
                            gun = user_tank(mainTankX, mainTankY, currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            # fire_power += power_change

                            power(fire_power)

                            wall(xlocation, randomHeight, wall_width)
                            gameDisplay.fill(brown,rect=[0, display_height - ground_height, display_width, ground_height])
                            pygame.display.update()

                            clock.tick(FPS)
                    if player_health < 1:
                        game_over()
                    elif enemy_health < 1:
                        win_game()
                    damage = e_fire(enemy_gun, 8, 50, xlocation, wall_width,randomHeight, mainTankX)
                    player_health -= damage
                #-----------------------------------------------------------------------------------------------------------------------------------------
                #Thiết lập các nút thay đổi lực bắn
                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1
                #Thiết lập các nút khi ngừng nhấn nút
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        tankMove = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        changeTur = 0

                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        power_change = 0

        #Gioi han vi tri xe tang
        mainTankX += tankMove
        if mainTankX > display_width-(tankWidth/2):
            mainTankX=display_width-(tankWidth/2)
        
        if mainTankX - (tankWidth / 2) < xlocation + wall_width:
            mainTankX += 5
        
        currentTurPos += changeTur
        #Giới hạn nòng pháo
        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        gameDisplay.fill(black)
        health_bars(player_health, enemy_health)
        gun = user_tank(mainTankX, mainTankY, currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        
        #Giới hạn lực bắn
        fire_power += power_change

        if fire_power > 100:
            fire_power = 100
        elif fire_power < 1:
            fire_power = 1

        power(fire_power)
        #Tạo vật chắn
        wall(xlocation, randomHeight, wall_width)
        gameDisplay.fill(brown, rect=[0, display_height - ground_height, display_width, ground_height])
        pygame.display.update()
        
        # Điều kiện thắng thua 
        if player_health < 1:
            game_over()
        elif enemy_health < 1:
            win_game()
        clock.tick(FPS)
#Thực hiện khai hỏa
def fire(xy, turPos, gun_power, xlocation, wall_width, randomHeight, enemyTankX):
    
    fire = True
    damage = 0

    starting_bulle = list(xy)

    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay, red, (starting_bulle[0], starting_bulle[1]), 5)

        starting_bulle[0] -= (12 - turPos) * 2

       
        starting_bulle[1] += int((((starting_bulle[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if starting_bulle[1] > display_height - ground_height:
            #Lay vi tri dan
            print("Last shell:", starting_bulle[0], starting_bulle[1])
            hit_x = int((starting_bulle[0] * display_height - ground_height) / starting_bulle[1])
            hit_y = int(display_height - ground_height)
            print("Impact:", hit_x, hit_y)
            # Tinh damage
            if (enemyTankX + 10 > hit_x) and (hit_x > enemyTankX - 10):
                print("Critical Hit!")
                damage = 30
            elif (enemyTankX + 15 > hit_x) and (hit_x > enemyTankX - 15):
                print("Hard Hit!")
                damage = 20
            elif (enemyTankX + 25 > hit_x) and (hit_x > enemyTankX - 25):
                print("Medium Hit")
                damage = 10
            elif (enemyTankX + 35 > hit_x) and (hit_x > enemyTankX - 35):
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False
        
        # Check va chạm bước tường
        check_x_1 = starting_bulle[0] <= xlocation + wall_width
        check_x_2 = starting_bulle[0] >= xlocation

        check_y_1 = starting_bulle[1] <= display_height
        check_y_2 = starting_bulle[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", starting_bulle[0], starting_bulle[1])
            hit_x = int((starting_bulle[0]))
            hit_y = int(starting_bulle[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage
#Thực hiện khai hỏa của xe tăng địch
def e_fire(xy, turPos, gun_power, xlocation, wall_width, randomHeight, utankx):
    
    damage = 0
    currentPower = 1
    power_found = False

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True
        print(currentPower)

        fire = True
        starting_bullet = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            starting_bullet[0] += (12 - turPos) * 2
            starting_bullet[1] += int((((starting_bullet[0] - xy[0]) * 0.015 / (currentPower / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

            if starting_bullet[1] > display_height - ground_height:
                hit_x = int((starting_bullet[0] * display_height - ground_height) / starting_bullet[1])
                hit_y = int(display_height - ground_height)
                
                if utankx + 15 > hit_x > utankx - 15:
                    print("target acquired!")
                    power_found = True                    
                fire = False    

    fire = True
    starting_bullet = list(xy)
    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
       
        pygame.draw.circle(gameDisplay, red, (starting_bullet[0], starting_bullet[1]), 5)

        starting_bullet[0] += (12 - turPos) * 2

        gun_power = random.randrange(int(currentPower * 0.90), int(currentPower * 1.15))

        starting_bullet[1] += int((((starting_bullet[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if starting_bullet[1] > display_height - ground_height:
            print("last shell:", starting_bullet[0], starting_bullet[1])
            hit_x = int((starting_bullet[0] * display_height - ground_height) / starting_bullet[1])
            hit_y = int(display_height - ground_height)
            print("Impact:", hit_x, hit_y)

            if utankx + 10 > hit_x > utankx - 10:
                print("Critical Hit!")
                damage = 30 
            elif utankx + 15 > hit_x > utankx - 15:
                print("Hard Hit!")
                damage = 20
            elif utankx + 25 > hit_x > utankx - 25:
                print("Medium Hit")
                damage = 10
            elif utankx + 35 > hit_x > utankx - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False
        #Check va chạm bước tường
        check_x_1 = starting_bullet[0] <= xlocation + wall_width
        check_x_2 = starting_bullet[0] >= xlocation

        check_y_1 = starting_bullet[1] <= display_height
        check_y_2 = starting_bullet[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", starting_bullet[0], starting_bullet[1])
            hit_x = int((starting_bullet[0]))
            hit_y = int(starting_bullet[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage

#Hiệu ứng nổ
def explosion(x, y, size=20):
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # startPoint = x, y

        colorChoices = [red, light_red, yellow, light_yellow]

        magnitude = 1

        while magnitude < size:
            exploding_bit_x = x + random.randrange(-1 * magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1 * magnitude, magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y),random.randrange(1, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False
        
intro_game()
gameLoop()
pygame.quit()
quit()