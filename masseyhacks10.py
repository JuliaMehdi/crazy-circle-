from pygame import * 

init() 
font.init()
screen = display.set_mode((800, 600))

running = True 

clock = time.Clock()
menu = 1 

xpos = 5
ypos = 300
colour = (255, 155, 0)
myFont = font.SysFont("onyx", 100)
xmouse, ymouse = 0, 0 
leftClick, rightClick = False, False 
while running:
    xmouse, ymouse = mouse.get_pos() 
    leftClick, rightClick = False, False 

    for action in event.get(): 
        if action.type == QUIT: 
            running = False 
            break
        elif action.type == MOUSEBUTTONDOWN: 
            if action.button == 1: 
                leftClick = True
            elif action.button == 3: 
                rightClick = True

    if menu == 1:
        screen.fill((232, 184, 179))
        draw.rect(screen, (240, 207, 206), (180, 80, 440, 140))
        draw.rect(screen, (204, 131, 129), (200, 100, 400, 105))
        draw.rect(screen, (136, 178, 130), (200, 250, 400, 100), 0)
        draw.rect(screen, (156, 198, 150), (210, 260, 380, 80), 0)
        
        draw.rect(screen, (136, 178, 130), (200, 450, 400, 100), 0) 
        draw.rect(screen, (156, 198, 150), (210, 460, 380, 80), 0) 
        if xmouse > 200 and xmouse < 600 and ymouse > 450 and ymouse < 550:
            draw.rect(screen, (116, 158, 120), (200, 450, 400, 100), 0)
            draw.rect(screen, (136, 178, 130), (210, 460, 380, 80), 0) 
            if leftClick:
                menu = 2
        elif xmouse > 200 and xmouse < 600 and ymouse > 250 and ymouse < 350:
            draw.rect(screen, (116, 158, 120), (200, 250, 400, 100), 0)
            draw.rect(screen, (136, 178, 130), (210, 260, 380, 80), 0)
            if leftClick:
                menu = 17
        title = myFont.render ("ABOUT ME!", False, (0, 0, 0))
        screen.blit(title,(275, 248))
        title = myFont.render ("PLAY", False, (0, 0, 0))
        screen.blit(title,(325, 448))
        title = myFont.render ("CRAZY CIRCLE", False, (0, 0, 0))
        screen.blit(title,(225, 100))

    elif menu == 2:
        screen.fill((255, 200, 200))
        draw.rect(screen, (116, 158, 110), (100, 50, 600, 100), 0)
        draw.rect(screen, (136, 178, 130), (110, 60, 580, 80), 0)
        title = myFont.render ("---LEVELS---", False, (0, 0, 0))
        screen.blit(title,(250, 50))
        
        draw.rect(screen, (116, 158, 110), (50, 200, 300, 100), 0)
        draw.rect(screen, (136 , 178, 130), (60, 210, 280, 80), 0)
        
        draw.rect(screen, (116, 158, 110), (50, 400, 300, 100), 0)
        draw.rect(screen, (136 , 178, 130), (60, 410, 280, 80), 0)
        
        draw.rect(screen, (116, 158, 110), (450, 400, 300, 100), 0)
        draw.rect(screen, (136 , 178, 130), (460, 410, 280, 80), 0)
        
        draw.rect(screen, (116, 158, 110), (450, 200, 300, 100), 0)
        draw.rect(screen, (136 , 178, 130), (460, 210, 280, 80), 0)
        
        if xmouse > 50 and xmouse < 350 and ymouse > 200 and ymouse < 300:
            draw.rect(screen, (106, 148, 100), (50, 200, 300, 100), 0)
            draw.rect(screen, (126 , 168, 120), (60, 210, 280, 80), 0)
            if leftClick:
                menu = 3

        elif xmouse > 50 and xmouse < 350 and ymouse > 400 and ymouse < 500:
            draw.rect(screen, (106, 148, 100), (50, 400, 300, 100), 0)
            draw.rect(screen, (126 , 168, 120), (60, 410, 280, 80), 0)
            if leftClick:
                menu = 4

        elif xmouse > 450 and xmouse < 750 and ymouse > 400 and ymouse < 500:
            draw.rect(screen, (106, 148, 100), (450, 400, 300, 100), 0)
            draw.rect(screen, (126 , 168, 120), (460, 410, 280, 80), 0)
            if leftClick:
                menu = 5 

        elif xmouse > 450 and xmouse < 750 and ymouse > 200 and ymouse < 300:
            draw.rect(screen, (106, 148, 100), (450, 200, 300, 100), 0)
            draw.rect(screen, (126 , 168, 120), (460, 210, 280, 80), 0)
            if leftClick:
                menu = 6
        title = myFont.render ("EASY", False, (0, 0, 0))
        screen.blit(title,(130, 200))
               
        title = myFont.render ("MEDIUM", False, (0, 0, 0))
        screen.blit(title,(105, 400))
                     
        title = myFont.render ("HARD", False, (0, 0, 0))
        screen.blit(title,(525, 400))

        title = myFont.render ("DIFFICULT", False, (0, 0, 0))
        screen.blit(title,(475, 200))

        
        draw.rect(screen, (130, 130, 130), (10, 10, 50, 50),)
        if xmouse > 10 and xmouse < 60 and ymouse > 10 and ymouse < 60:
            draw.rect(screen, (100, 100, 100), (10, 10, 50, 50), 0)
            if leftClick:
                xpos = 0
                ypos = 400
                menu = 1

###########################################################
    elif menu == 3:
        screen.fill((171, 217, 163))
        draw.rect(screen, (116, 158, 110), (50, 25, 700, 125), 0)
        draw.rect(screen, (136, 178, 130), (60, 35, 680, 105), 0)
        
        draw.rect(screen, (205, 145, 70), (100, 200, 600, 100), 0)
        draw.rect(screen, (255 , 195, 130), (110, 210, 580, 80), 0)
        
        draw.rect(screen, (100, 100, 200), (100, 400, 600, 100), 0)
        draw.rect(screen, (150 , 150, 250), (110, 410, 580, 80), 0)
        if xmouse > 100 and xmouse < 700 and ymouse > 200 and ymouse < 300:
            draw.rect(screen, (185, 125, 50), (100, 200, 600, 100), 0)
            draw.rect(screen, (235 ,175, 100), (110, 210, 580, 80), 0)
            if leftClick:
                menu = 7
        elif xmouse > 100 and xmouse < 700 and ymouse > 400 and ymouse < 500:
            draw.rect(screen, (80,80, 180), (100, 400, 600, 100), 0)
            draw.rect(screen, (130 , 130, 230), (110, 410, 580, 80), 0)
            if leftClick:
                menu = 8
                        
        draw.rect(screen, (130, 130, 130), (10, 10, 50, 50),)
        if xmouse > 10 and xmouse < 60 and ymouse > 10 and ymouse < 60:
            draw.rect(screen, (100, 100, 100), (10, 10, 50, 50), 0)
            if leftClick:
                xpos = 0
                ypos = 400
                menu = 2
        title = myFont.render ("----EASY----", False, (0, 0, 0))
        screen.blit(title,(270, 35))
        title = myFont.render ("THEME 2", False, (0, 0, 0))
        screen.blit(title,(275, 400))

        title = myFont.render ("THEME 1", False, (0, 0, 0))
        screen.blit(title,(275, 200))


##############################################################
    elif menu == 4:
        screen.fill((240, 240, 163))
        draw.rect(screen, (116, 158, 110), (50, 25, 700, 125), 0)
        draw.rect(screen, (136, 178, 130), (60, 35, 680, 105), 0)
        
        draw.rect(screen, (205, 145, 70), (100, 200, 600, 100), 0)
        draw.rect(screen, (255 , 195, 130), (110, 210, 580, 80), 0)
        
        draw.rect(screen, (100, 100, 200), (100, 400, 600, 100), 0)
        draw.rect(screen, (150 , 150, 250), (110, 410, 580, 80), 0)
        if xmouse > 100 and xmouse < 700 and ymouse > 200 and ymouse < 300:
            draw.rect(screen, (185, 125, 50), (100, 200, 600, 100), 0)
            draw.rect(screen, (235 ,175, 100), (110, 210, 580, 80), 0)
            if leftClick:
                menu = 9
        elif xmouse > 100 and xmouse < 700 and ymouse > 400 and ymouse < 500:
            draw.rect(screen, (80,80, 180), (100, 400, 600, 100), 0)
            draw.rect(screen, (130 , 130, 230), (110, 410, 580, 80), 0)
            if leftClick:
                menu = 10
                                    
        draw.rect(screen, (130, 130, 130), (10, 10, 50, 50),)
        if xmouse > 10 and xmouse < 60 and ymouse > 10 and ymouse < 60:
            draw.rect(screen, (100, 100, 100), (10, 10, 50, 50), 0)
            if leftClick:
                xpos = 0
                ypos = 400
                menu = 2
        title = myFont.render ("THEME 1", False, (0, 0, 0))
        screen.blit(title,(275, 200))
        title = myFont.render ("THEME 2", False, (0, 0, 0))
        screen.blit(title,(275, 400))
        title = myFont.render ("----MEDIUM----", False, (0, 0, 0))
        screen.blit(title,(200, 35))

###########################################################
    elif menu == 5:
        screen.fill((10, 10, 10))
        draw.rect(screen, (116, 158, 110), (50, 25, 700, 125), 0)
        draw.rect(screen, (136, 178, 130), (60, 35, 680, 105), 0)
        
        draw.rect(screen, (205, 145, 70), (100, 200, 600, 100), 0)
        draw.rect(screen, (255 , 195, 130), (110, 210, 580, 80), 0)
        
        draw.rect(screen, (100, 100, 200), (100, 400, 600, 100), 0)
        draw.rect(screen, (150 , 150, 250), (110, 410, 580, 80), 0)
        if xmouse > 100 and xmouse < 700 and ymouse > 200 and ymouse < 300:
            draw.rect(screen, (185, 125, 50), (100, 200, 600, 100), 0)
            draw.rect(screen, (235 ,175, 100), (110, 210, 580, 80), 0)
            if leftClick:
                menu = 11
        elif xmouse > 100 and xmouse < 700 and ymouse > 400 and ymouse < 500:
            draw.rect(screen, (80,80, 180), (100, 400, 600, 100), 0)
            draw.rect(screen, (130 , 130, 230), (110, 410, 580, 80), 0)
            if leftClick:
                menu = 12
                                    
        draw.rect(screen, (130, 130, 130), (10, 10, 50, 50),)
        if xmouse > 10 and xmouse < 60 and ymouse > 10 and ymouse < 60:
            draw.rect(screen, (100, 100, 100), (10, 10, 50, 50), 0)
            if leftClick:
                xpos = 0
                ypos = 400
                menu = 2
        title = myFont.render ("THEME 1", False, (0, 0, 0))
        screen.blit(title,(275, 200))
        title = myFont.render ("THEME 2", False, (0, 0, 0))
        screen.blit(title,(275, 400))
        title = myFont.render ("----HARD----", False, (0, 0, 0))
        screen.blit(title,(250, 35))

######################################################
    elif menu == 6:
        screen.fill((200, 15, 20))
        draw.rect(screen, (116, 158, 110), (50, 25, 700, 125), 0)
        draw.rect(screen, (136, 178, 130), (60, 35, 680, 105), 0)
        
        draw.rect(screen, (205, 145, 70), (100, 200, 600, 100), 0)
        draw.rect(screen, (255 , 195, 130), (110, 210, 580, 80), 0)
        
        draw.rect(screen, (100, 100, 200), (100, 400, 600, 100), 0)
        draw.rect(screen, (150 , 150, 250), (110, 410, 580, 80), 0)
        if xmouse > 100 and xmouse < 700 and ymouse > 200 and ymouse < 300:
            draw.rect(screen, (185, 125, 50), (100, 200, 600, 100), 0)
            draw.rect(screen, (235 ,175, 100), (110, 210, 580, 80), 0)
            if leftClick:
                menu = 13
        elif xmouse > 100 and xmouse < 700 and ymouse > 400 and ymouse < 500:
            draw.rect(screen, (80,80, 180), (100, 400, 600, 100), 0)
            draw.rect(screen, (130 , 130, 230), (110, 410, 580, 80), 0)
            if leftClick:
                menu = 14
                                    
        draw.rect(screen, (130, 130, 130), (10, 10, 50, 50),)
        if xmouse > 10 and xmouse < 60 and ymouse > 10 and ymouse < 60:
            draw.rect(screen, (100, 100, 100), (10, 10, 50, 50), 0)
            if leftClick:
                xpos = 0
                ypos = 400
                menu = 2
        title = myFont.render ("THEME 1", False, (0, 0, 0))
        screen.blit(title,(275, 200))
        title = myFont.render ("THEME 2", False, (0, 0, 0))
        screen.blit(title,(275, 400))
        title = myFont.render ("----DIFFICULT----", False, (0, 0, 0))
        screen.blit(title,(200, 35))


###########################################################
    elif menu == 7:
        
        screen.fill((255, 255, 150))
        draw.rect(screen, (255, 0, 0), (790,1 , 10, 800))
        draw.circle(screen, (250, 90, 90), (xpos, ypos), 50)
        if key.get_pressed()[K_UP]:
            ypos -= 1
        if key.get_pressed()[K_DOWN]:
            ypos += 1
        if key.get_pressed()[K_RIGHT]:
            xpos += 1
        if key.get_pressed()[K_LEFT]:
            xpos-= 1 
        if xpos >= 799:
            menu = 15
        
        centers = [(100, 200), (500, 300), (300, 50)]
        sizes = [50, 150, 75]
        circlecount = 3
        for i in range (circlecount):
            draw.circle(screen, (135, 206, 235), centers[i], sizes[i])
        for i in range (circlecount):
            xdist = xpos - centers[i][0]
            ydist = ypos - centers[i][1]
            dist = (xdist**2 + ydist**2)**0.5
            if dist < sizes[i] + 50:
                menu = 16
        if ypos >= 599 or ypos < 1 or xpos < 1:
            menu = 16
###################################################################################
    elif menu == 8:
        
        screen.fill((135, 206, 235))
        draw.rect(screen, (255, 0, 0), (790,1 , 10, 800))
        draw.circle(screen, (250, 250, 250), (xpos, ypos), 50)
        if key.get_pressed()[K_UP]:
            ypos -= 1
        if key.get_pressed()[K_DOWN]:
            ypos += 1
        if key.get_pressed()[K_RIGHT]:
            xpos += 1
        if key.get_pressed()[K_LEFT]:
            xpos-= 1 
        if xpos >= 799:
            menu = 15
        
        centers = [(200, 100), (600, 200), (300, 500)]
        sizes = [50, 100, 75]
        circlecount = 3
        for i in range (circlecount):
            draw.circle(screen, (100, 100, 200), centers[i], sizes[i])
        for i in range (circlecount):
            xdist = xpos - centers[i][0]
            ydist = ypos - centers[i][1]
            dist = (xdist**2 + ydist**2)**0.5
            if dist < sizes[i] + 50:
                menu = 16
        if ypos >= 599 or ypos < 1 or xpos < 1:
            menu = 16
##########################################################################################        
    elif menu == 9:
        
        screen.fill((255, 255, 150))
        draw.rect(screen, (255, 0, 0), (790,1 , 10, 800))
        draw.circle(screen, (250, 90, 90), (xpos, ypos), 50)
        if key.get_pressed()[K_UP]:
            ypos -= 1
        if key.get_pressed()[K_DOWN]:
            ypos += 1
        if key.get_pressed()[K_RIGHT]:
            xpos += 1
        if key.get_pressed()[K_LEFT]:
            xpos-= 1 
        if xpos >= 799:
            menu = 15
        
        centers = [(100, 200), (600, 300), (300, 500), (400, 50)]
        sizes = [50, 150, 120, 50]
        circlecount = 4
        for i in range (circlecount):
            draw.circle(screen, (135, 206, 235), centers[i], sizes[i])
        for i in range (circlecount):
            xdist = xpos - centers[i][0]
            ydist = ypos - centers[i][1]
            dist = (xdist**2 + ydist**2)**0.5
            if dist < sizes[i] + 50:
                menu = 16
        if ypos >= 599 or ypos < 1 or xpos < 1:
            menu = 16
#####################################################################################
    elif menu == 10:
        
        screen.fill((135, 206, 235))
        draw.rect(screen, (255, 0, 0), (790,1 , 10, 800))
        draw.circle(screen, (250, 250, 250), (xpos, ypos), 50)
        if key.get_pressed()[K_UP]:
            ypos -= 1
        if key.get_pressed()[K_DOWN]:
            ypos += 1
        if key.get_pressed()[K_RIGHT]:
            xpos += 1
        if key.get_pressed()[K_LEFT]:
            xpos-= 1 
        if xpos >= 799:
            menu = 15
        
        centers = [(100, 200), (600, 300), (300, 500), (300, 50)]
        sizes = [50, 150, 100, 75]
        circlecount = 4
        for i in range (circlecount):
            draw.circle(screen, (100, 100, 200), centers[i], sizes[i])
        for i in range (circlecount):
            xdist = xpos - centers[i][0]
            ydist = ypos - centers[i][1]
            dist = (xdist**2 + ydist**2)**0.5
            if dist < sizes[i] + 50:
                menu = 16
        if ypos >= 599 or ypos < 1 or xpos < 1:
            menu = 16
########################################################################################################

    elif menu == 11:
        
        screen.fill((255, 255, 150))
        draw.rect(screen, (255, 0, 0), (790,1 , 10, 800))
        draw.circle(screen, (250, 90, 90), (xpos, ypos), 50)
        if key.get_pressed()[K_UP]:
            ypos -= 2
        if key.get_pressed()[K_DOWN]:
            ypos += 2
        if key.get_pressed()[K_RIGHT]:
            xpos += 2
        if key.get_pressed()[K_LEFT]:
            xpos-= 2
        if xpos >= 799:
            menu = 15
        if ypos >= 599 or ypos < 1 or xpos < 1:
            menu = 16        
        centers = [(100, 200), (600, 300), (300, 500), (500, 50), ]
        sizes = [25, 150, 100, 75]
        circlecount = 4
        for i in range (circlecount):
            draw.circle(screen, (135, 206, 235), centers[i], sizes[i])
        for i in range (circlecount):
            xdist = xpos - centers[i][0]
            ydist = ypos - centers[i][1]
            dist = (xdist**2 + ydist**2)**0.5
            if dist < sizes[i] + 50:
                menu = 16
#######################################################################################
    elif menu == 12:
        
        screen.fill((135, 206, 235))
        draw.rect(screen, (255, 0, 0), (790,1 , 10, 800))
        draw.circle(screen, (250, 250, 250), (xpos, ypos), 50)
        if key.get_pressed()[K_UP]:
            ypos -= 1
        if key.get_pressed()[K_DOWN]:
            ypos += 1
        if key.get_pressed()[K_RIGHT]:
            xpos += 1
        if key.get_pressed()[K_LEFT]:
            xpos-= 1 
        if xpos >= 799:
            menu = 15       
        centers = [(100, 200), (600, 300), (300, 500), (500, 50)]
        sizes = [50, 125, 100, 75]
        circlecount = 4
        for i in range (circlecount):
            draw.circle(screen, (100, 100, 200), centers[i], sizes[i])
        for i in range (circlecount):
            xdist = xpos - centers[i][0]
            ydist = ypos - centers[i][1]
            dist = (xdist**2 + ydist**2)**0.5
            if dist < sizes[i] + 50:
                menu = 16
        if ypos >= 599 or ypos < 1 or xpos < 1:
            menu = 16

################################################################################################### medium 

    elif menu == 13:
        
        screen.fill((255, 255, 150))
        draw.rect(screen, (255, 0, 0), (790,1 , 10, 800))
        draw.circle(screen, (250, 90, 90), (xpos, ypos), 50)
        if key.get_pressed()[K_UP]:
            ypos -= 1
        if key.get_pressed()[K_DOWN]:
            ypos += 1
        if key.get_pressed()[K_RIGHT]:
            xpos += 1
        if key.get_pressed()[K_LEFT]:
            xpos-= 1 
        if xpos >= 799:
            menu = 15
        
        centers = [(100, 200), (600, 300), (300, 500), (500, 50), (775, 575)]
        sizes = [50, 125, 100, 75, 25]
        circlecount = 5
        for i in range (circlecount):
            draw.circle(screen, (135, 206, 235), centers[i], sizes[i])
        for i in range (circlecount):
            xdist = xpos - centers[i][0]
            ydist = ypos - centers[i][1]
            dist = (xdist**2 + ydist**2)**0.5
            if dist < sizes[i] + 50:
                menu = 16
        if ypos >= 599 or ypos < 1 or xpos < 1:
            menu = 16
########################################################################
    elif menu == 14:
        
        screen.fill((100, 100, 200))
        draw.rect(screen, (255, 0, 0), (790,1 , 10, 800))
        draw.circle(screen, (250, 250, 250), (xpos, ypos), 50)
        if key.get_pressed()[K_UP]:
            ypos -= 1
        if key.get_pressed()[K_DOWN]:
            ypos += 1
        if key.get_pressed()[K_RIGHT]:
            xpos += 1
        if key.get_pressed()[K_LEFT]:
            xpos-= 1 
        if xpos >= 799:
            menu = 15
        
        centers = [(100, 200), (600, 300), (300, 500), (500, 50), (50, 550)]
        sizes = [50, 125, 100, 75, 25]
        circlecount = 5
        for i in range (circlecount):
            draw.circle(screen, (135, 206, 235), centers[i], sizes[i])
        for i in range (circlecount):
            xdist = xpos - centers[i][0]
            ydist = ypos - centers[i][1]
            dist = (xdist**2 + ydist**2)**0.5
            if dist < sizes[i] + 50:
                menu = 16
        if ypos >= 599 or ypos < 1 or xpos < 1:
            menu = 16

################################################################################################################################################################

    if menu == 15:
        xpos = 5
        ypos = 400
        screen.fill((135, 220, 235))
        draw.rect(screen, (100, 226, 95), (200, 300, 400, 200), 0) 
        if xmouse > 200 and xmouse < 600 and ymouse > 300 and ymouse < 500:
            draw.rect(screen, (80, 206, 75), (200, 300, 400, 200), 0) 
            if leftClick:
                menu = 1
        title = myFont.render ("YOU WIN :)", False, (0, 0, 0))
        screen.blit(title,(250, 100))
        title = myFont.render ("BACK TO MENU", False, (0, 0, 0))
        screen.blit(title,(225, 350))

                
        
    if menu == 16:
        xpos = 5
        ypos = 400
        screen.fill((252, 209, 207))
        draw.rect(screen, (255, 184, 192), (200, 300, 400, 200),)
        if xmouse > 200 and xmouse < 600 and ymouse > 300 and ymouse < 500:
            draw.rect(screen, (250, 179, 187), (200, 300, 400, 200), 0)
            if leftClick:
                menu = 2
        title = myFont.render ("YOU LOSE :(", False, (0, 0, 0))
        screen.blit(title,(250, 100))
        title = myFont.render ("BACK TO MENU", False, (0, 0, 0))
        screen.blit(title,(225, 350))

    if menu == 17:
        screen.fill((232, 179, 187))
        myFont = font.SysFont("Times New Roman", 75)
        title = myFont.render ("ABOUT ME", False, (0, 0, 0))
        screen.blit(title,(200, 25))
        myFont = font.SysFont("Times New Roman", 20)
        title = myFont.render ("Hello! My name is Julia Mehdi. I’m 15 years old and in grade 9.  I attended Massey hacks  ", False, (0, 0, 0))
        screen.blit(title,(25, 225))
        title = myFont.render ("last year as my first hackathon. I’ve always had a passion in learning python, and just", False, (0, 0, 0))
        screen.blit(title,(25, 250))
        title = myFont.render ("coding as a whole. Knowing how well it does in careers and you can use it in almost anything ", False, (0, 0, 0))
        screen.blit(title,(25, 275))
        title = myFont.render ("as most of jobs are now using computers. I have lots of people in my life who know computer ", False, (0, 0, 0))
        screen.blit(title,(25, 300))
        title = myFont.render (" science, some being my brothers and I look up to them a lot! At first, I was hesitant to  ", False, (0, 0, 0))
        screen.blit(title,(25, 325))
        title = myFont.render ("coming to Massey hacks this year, as this year as my first year in high school was very  ", False, (0, 0, 0))
        screen.blit(title,(25, 350))
        title = myFont.render ("rough, but coming here to Massey hacks was genuinely such a good idea. Being surrounded  ", False, (0, 0, 0))
        screen.blit(title,(25, 375))
        title = myFont.render ("by so many passionate hackers gave me the motivation to finish a whole project which ", False, (0, 0, 0))
        screen.blit(title,(25, 400))
        title = myFont.render ("I didn’t think id be able to finish If I had a week! Having a future with computer science  ", False, (0, 0, 0))
        screen.blit(title,(25, 425))
        title = myFont.render ("is defiantly a goal I have. Even though its more difficult for me to get into as its more of  ", False, (0, 0, 0))
        screen.blit(title,(25, 450))
        title = myFont.render ("a male dominated field, my dream is to learn more about it and have a future in said field.  ", False, (0, 0, 0))
        screen.blit(title,(25, 475))
        
        draw.rect(screen, (130, 130, 130), (10, 10, 50, 50),)
        if xmouse > 10 and xmouse < 60 and ymouse > 10 and ymouse < 60:
            draw.rect(screen, (100, 100, 100), (10, 10, 50, 50), 0)
            if leftClick:
                xpos = 0
                ypos = 400
                myFont = font.SysFont("onyx", 100)
                menu = 1

    display.flip()
    
    clock.tick(100) 
quit() 
