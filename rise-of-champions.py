#RISE OF CHAMPIONS (MAIN)
#Computer Science Grade 11 FSE Macanovik
#Partners: Jack Li & Cameron Beneteau
from pygame import * #import pygam module
from time import time as tm #import real time module

mixer.init() #initiate mixer (sound system)
font.init() #initiate font

width, height = 1200, 800 #width and height of the screen
screen = display.set_mode((1200,800)) #setting the screen
clock = time.Clock() #clock for frame rate
#####################################################################
#MUSIC
#MUSIC / SONGS
introSong = mixer.Sound("sounds/music/intro/introSong.ogg") #import intro song
gameOneMusic = mixer.Sound("sounds/music/game/gameOneMusic.ogg") #import game song
bossMusic = mixer.Sound("sounds/music/boss/bossMusic.ogg") #import boss song
winnerSong = mixer.Sound("sounds/music/boss/winnerSong.ogg") #import winner song

#EFFECTS
deathSound = mixer.Sound("sounds/music/death/deathSound.ogg") #import death sound
pauseSound = mixer.Sound("sounds/music/pause/pauseSound.ogg") #import pause sound
swordSwooshSound = mixer.Sound("sounds/effects/character/swordSwooshSound.ogg") #import attack sound
swordPickupSound = mixer.Sound("sounds/effects/objects/swordPickupSound.ogg") #import sword pickup sound
healthSound = mixer.Sound("sounds/effects/objects/healthSound.ogg") #import import health pickup sound
clickSound = mixer.Sound("sounds/effects/menu/clickSound.ogg") #import button click sound
doorSound = mixer.Sound("sounds/effects/objects/doorSound.ogg") #import door sound
portalSound = mixer.Sound("sounds/effects/objects/portalSound.ogg") #import portal sound
keySound = mixer.Sound("sounds/effects/objects/keySound.ogg") #import key sound

musicChannel = mixer.Channel(0) #setting 1st music channel
musicChannel.set_volume(0.5) #setting volume of 1st music channel
effectChannel = mixer.Channel(1)#setting 2nd music channel
optionsChannel = mixer.Channel(2)#setting 3rd music channel
bossChannel = mixer.Channel(3)#setting 4th music channel
bossChannel.set_volume(0.5) #setting volume of 2nd music channel

musicVolume = 0.75 #variable for music volume
musicBarRect = Rect(450, 200, 400, 20) #rectangle for music slider
musicSliderRect = Rect(830*0.5 + 240, 180, 20, 60) #rectangle for music slider
musicVolumeRect = Rect(450, 180, 400, 60) #rectangle for music slider

effectVolume = 1 #variable for effect volume
effectBarRect = Rect(450, 500, 400, 20) #rectangle for effect slider
effectSliderRect = Rect(830, 480, 20, 60) #rectangle for effect slider
effectVolumeRect = Rect(450, 480, 400, 60) #rectangle for effect slider
#################################################
#CHARACTER SPRITES
manFrameDict = {'up': [image.load('character/man061.png')], #import standing sprites for man character
                'left': [image.load('character/man070.png')],
                'down': [image.load('character/man079.png')],
                'right': [image.load('character/man088.png')]}

manWalkFrameDict = {'up': [image.load('character/man0{0}.png'.format(n)) for n in range(62, 70)], #import walking sprites for man character
                    'left': [image.load('character/man0{0}.png'.format(n)) for n in range(71, 79)],
                    'down': [image.load('character/man0{0}.png'.format(n)) for n in range(80, 88)],
                    'right': [image.load('character/man0{0}.png'.format(n)) for n in range(89, 97)]}

manAttackFrameDict = {'up': [image.load('character/man{0}.png'.format(n)) for n in range(179, 185)], #import attacking sprites for girl character
                      'left': [image.load('character/man{0}.png'.format(n)) for n in range(185, 191)],
                      'down': [image.load('character/man{0}.png'.format(n)) for n in range(191, 197)],
                      'right': [image.load('character/man{0}.png'.format(n)) for n in range(197, 203)]}
#GIRL
girlFrameDict = {'up': [image.load('character/girl061.png')], #import standing sprites for man character
                 'left': [image.load('character/girl070.png')],
                 'down': [image.load('character/girl079.png')],
                 'right': [image.load('character/girl088.png')]}

girlWalkFrameDict = {'up': [image.load('character/girl0{0}.png'.format(n)) for n in range(62, 70)], #import walking sprites for girl character
                     'left': [image.load('character/girl0{0}.png'.format(n)) for n in range(71, 79)],
                     'down': [image.load('character/girl0{0}.png'.format(n)) for n in range(80, 88)],
                     'right': [image.load('character/girl0{0}.png'.format(n)) for n in range(89, 97)]}

girlAttackFrameDict = {'up': [image.load('character/girl{0}.png'.format(n)) for n in range(179, 185)], #import attacking sprites girl man character
                       'left': [image.load('character/girl{0}.png'.format(n)) for n in range(185, 191)],
                       'down': [image.load('character/girl{0}.png'.format(n)) for n in range(191, 197)],
                       'right': [image.load('character/girl{0}.png'.format(n)) for n in range(197, 203)]}
#####################################################################
#ENEMY SPRITES
#ORC
orcFrameDict = {'up': [image.load('enemies/orc001.png')], #import standing sprites for orc enemy
                'left': [image.load('enemies/orc010.png')],
                'down': [image.load('enemies/orc019.png')],
                'right': [image.load('enemies/orc028.png')]}

orcWalkFrameDict = {'up': [image.load('enemies/orc00{0}.png'.format(n)) for n in range(2, 10)], #import walking sprites for orc enemy
                    'left': [image.load('enemies/orc0{0}.png'.format(n)) for n in range(11, 19)],
                    'down': [image.load('enemies/orc0{0}.png'.format(n)) for n in range(19, 28)],
                    'right': [image.load('enemies/orc0{0}.png'.format(n)) for n in range(28, 37)]}

orcAttackFrameDict = {'up': [image.load('enemies/orc0{0}.png'.format(n)) for n in range(37, 43)], #import attacking sprites for orc enemy
                'left': [image.load('enemies/orc0{0}.png'.format(n)) for n in range(43, 49)],
                'down': [image.load('enemies/orc0{0}.png'.format(n)) for n in range(49, 55)],
                'right': [image.load('enemies/orc0{0}.png'.format(n)) for n in range(55, 61)]}

#SKELETON
orcFrameDict = {'up': [image.load('enemies/skeleton001.png')], #import standing sprites for skeleton enemy
                'left': [image.load('enemies/skeleton010.png')],
                'down': [image.load('enemies/skeleton019.png')],
                'right': [image.load('enemies/skeleton028.png')]}

skeletonWalkFrameDict = {'up': [image.load('enemies/skeleton00{0}.png'.format(n)) for n in range(2, 10)], #import walking sprites for skeleton enemy
                    'left': [image.load('enemies/skeleton0{0}.png'.format(n)) for n in range(11, 19)],
                    'down': [image.load('enemies/skeleton0{0}.png'.format(n)) for n in range(19, 28)],
                    'right': [image.load('enemies/skeleton0{0}.png'.format(n)) for n in range(28, 37)]}

skeletonAttackFrameDict = {'up': [image.load('enemies/skeleton0{0}.png'.format(n)) for n in range(37, 43)], #import attacking sprites for skeleton enemy
                'left': [image.load('enemies/skeleton0{0}.png'.format(n)) for n in range(43, 49)],
                'down': [image.load('enemies/skeleton0{0}.png'.format(n)) for n in range(49, 55)],
                'right': [image.load('enemies/skeleton0{0}.png'.format(n)) for n in range(55, 61)]}

#KEEPER
keeperFrameDict = {'up': [image.load('enemies/keeper001.png')], #import standing sprites for keeper enemy
                'left': [image.load('enemies/keeper010.png')],
                'down': [image.load('enemies/keeper019.png')],
                'right': [image.load('enemies/keeper028.png')]}

keeperWalkFrameDict = {'up': [image.load('enemies/keeper00{0}.png'.format(n)) for n in range(2, 10)], #import walking sprites for keeper enemy
                    'left': [image.load('enemies/keeper0{0}.png'.format(n)) for n in range(11, 19)],
                    'down': [image.load('enemies/keeper0{0}.png'.format(n)) for n in range(19, 28)],
                    'right': [image.load('enemies/keeper0{0}.png'.format(n)) for n in range(28, 37)]}

keeperAttackFrameDict = {'up': [image.load('enemies/keeper0{0}.png'.format(n)) for n in range(37, 43)], #import attacking sprites for keeper enemy
                'left': [image.load('enemies/keeper0{0}.png'.format(n)) for n in range(43, 49)],
                'down': [image.load('enemies/keeper0{0}.png'.format(n)) for n in range(49, 55)],
                'right': [image.load('enemies/keeper0{0}.png'.format(n)) for n in range(55, 61)]}

#BOSS
bossFrameDict = {'up': [image.load('enemies/boss001.png')], #import standing sprites for boss enemy
                'left': [image.load('enemies/boss010.png')],
                'down': [image.load('enemies/boss019.png')],
                'right': [image.load('enemies/boss028.png')]}

bossWalkFrameDict = {'up': [image.load('enemies/boss00{0}.png'.format(n)) for n in range(2, 10)], #import walking sprites for boss enemy
                    'left': [image.load('enemies/boss0{0}.png'.format(n)) for n in range(11, 19)],
                    'down': [image.load('enemies/boss0{0}.png'.format(n)) for n in range(19, 28)],
                    'right': [image.load('enemies/boss0{0}.png'.format(n)) for n in range(28, 37)]}

bossAttackFrameDict = {'up': [image.load('enemies/boss0{0}.png'.format(n)) for n in range(37, 43)], #import attacking sprites for boss enemy
                'left': [image.load('enemies/boss0{0}.png'.format(n)) for n in range(43, 49)],
                'down': [image.load('enemies/boss0{0}.png'.format(n)) for n in range(49, 55)],
                'right': [image.load('enemies/boss0{0}.png'.format(n)) for n in range(55, 61)]}

#####################################################################
#IMPORT TITLE PICTURES
def makeMove(character,start,end):
    move = [] #list for imported images
    for i in range(start,end+1):
        move.append(image.load("character/%s%03d.png" % (character,i)).convert_alpha()) #for each picture in a certain range, append it to the list
    return move #return the list with pictures
#CHARACTER IMAGES FOR TITLE SCREEN
#MAN
manWalkingPics = [makeMove("man",88,96), #calling the function for images with ending 88 - 96
                  makeMove("man",79,87), #calling the function for images with ending 79 - 87
                  makeMove("man",61,69), #calling the function for images with ending 61 - 69
                  makeMove("man",70,78)] #calling the function for images with ending 70 - 78
#TRANSFORM MAN PICS
for i in range(len(manWalkingPics)): #for each item in the 2-D list
    for j in range(len(manWalkingPics[i])):
        manWalkingPics[i][j] = transform.scale(manWalkingPics[i][j],(manWalkingPics[i][j].get_width()*9,manWalkingPics[i][j].get_height()*9)) #making each image larger (for title screen purposes)
#GIRL
girlWalkingPics = [makeMove("girl", 88, 96), #calling the function for images with ending 88 - 96
                   makeMove("girl", 79, 87), #calling the function for images with ending 79 - 87
                   makeMove("girl", 61, 69), #calling the function for images with ending 61 - 69
                   makeMove("girl", 70, 78)] #calling the function for images with ending 70 - 78
#TRANSFORM GIRL PICS
for i in range(len(girlWalkingPics)):
    for j in range(len(girlWalkingPics[i])):
        girlWalkingPics[i][j] = transform.scale(girlWalkingPics[i][j],(girlWalkingPics[i][j].get_width()*10,int(girlWalkingPics[i][j].get_height()*9.5))) #making each image larger (for title screen purposes)
#####################################################################
#IMAGES
titlePic = transform.scale(image.load("images/titlePic.png").convert_alpha(),(1400, 900)) #import title images
titleTwoPic = transform.scale(image.load("images/titleTwoPic.png").convert_alpha(),(1200, 800))

#BACKGROUND
grassBackground = transform.scale(image.load("images/grassBackground.png").convert_alpha(), (1200, 900)) #import map background images
dirtBackground = transform.scale(image.load("images/dirtBackground.png").convert_alpha(), (1200, 900))
sandBackground = transform.scale(image.load("images/sandBackground.png").convert_alpha(), (1200, 900))
darkBackground = transform.scale(image.load("images/darkBackground.png").convert_alpha(), (1200, 900))
bossBackground = transform.scale(image.load("images/bossBackground.png").convert_alpha(), (1200, 1200))

#OUTLINE
grassOutline = transform.scale(image.load("images/grassOutline.png").convert_alpha(), (100, 100)) #import map outline images
dirtOutline = transform.scale(image.load("images/dirtOutline.png").convert_alpha(), (100, 100))
sandOutline = transform.scale(image.load("images/sandOutline.png").convert_alpha(), (100, 100))
darkOutline = transform.scale(image.load("images/darkOutline.png").convert_alpha(), (100, 100))
bossOutline = transform.scale(image.load("images/bossOutline.png").convert_alpha(), (100, 100))

#OBJECTS
keyImage = transform.scale(image.load("images/keyImage.png").convert_alpha(), (80, 50)) #import object images
healthImage = transform.scale(image.load("images/health.png").convert_alpha(), (50, 50))
levelGate = transform.scale(image.load("images/levelGate.png").convert_alpha(), (100, 100))
finalGate = transform.scale(image.load("images/finalGate.png").convert_alpha(), (100, 100))
swordImage =  transform.scale(image.load("images/swordImage.png").convert_alpha(), (30, 60))
portalImage =  transform.scale(image.load("images/portalImage.png").convert_alpha(), (110, 100))
spikeImage = transform.scale(image.load("images/spikeImage.png").convert_alpha(), (100, 100))
torchImage = transform.scale(image.load("images/torchImage.png").convert_alpha(), (100, 100))
#####################################################################
#MENU TEXT IMAGES
titleTextPic = image.load("text/titleTextPic.png").convert_alpha() #import menu text images
playYellowPic = image.load("text/playYellowPic.png").convert_alpha()
playWhitePic = image.load("text/playWhitePic.png").convert_alpha()
instructionsYellowPic = image.load("text/instructionsYellowPic.png").convert_alpha()
instructionsWhitePic = image.load("text/instructionsWhitePic.png").convert_alpha()
optionsYellowPic = image.load("text/optionsYellowPic.png").convert_alpha()
optionsWhitePic = image.load("text/optionsWhitePic.png").convert_alpha()
creditsYellowPic = image.load("text/creditsYellowPic.png").convert_alpha()
creditsWhitePic = image.load("text/creditsWhitePic.png").convert_alpha()
quitYellowPic = image.load("text/quitYellowPic.png").convert_alpha()
quitWhitePic = image.load("text/quitWhitePic.png").convert_alpha()
backYellowPic = image.load("text/backYellowPic.png").convert_alpha()
backWhitePic = image.load("text/backWhitePic.png").convert_alpha()
chooseCharacterText = image.load("text/chooseCharacterText.png").convert_alpha()
callumText = image.load("text/callumText.png").convert_alpha()
melitaText = image.load("text/melitaText.png").convert_alpha()
musicVolumePic = image.load("text/musicVolumePic.png").convert_alpha()
effectVolumePic = image.load("text/effectVolumePic.png").convert_alpha()

#INSTRUCTION IMAGES
instructionsPic = image.load("text/instructions.png").convert_alpha() #import instruction images
keyControlPic = transform.scale(image.load("images/keyControl.png").convert_alpha(), (190, 150))
spaceControlPic = transform.scale(image.load("images/spaceControl.png").convert_alpha(), (220, 130))
spikePic = transform.scale(image.load("images/spikeImage.png").convert_alpha(), (100, 100))

#GAME OVER TEXT IMAGES
diedText = image.load("text/diedText.png").convert_alpha() #import game over images
diedPlayAgainYellow = image.load("text/diedPlayAgainYellow.png").convert_alpha()
diedPlayAgainBlack = image.load("text/diedPlayAgainBlack.png").convert_alpha()
diedMenuYellow = image.load("text/diedMenuYellow.png").convert_alpha()
diedMenuBlack = image.load("text/diedMenuBlack.png").convert_alpha()
diedQuitYellow = image.load("text/diedQuitYellow.png").convert_alpha()
diedQuitBlack = image.load("text/diedQuitBlack.png").convert_alpha()
winnerPic = image.load("text/winnerPic.png").convert_alpha()

#PAUSE TEXT IMAGES
pausedPic = image.load("text/pausedPic.png").convert_alpha() #import pause images
resumeYellowPic = image.load("text/resumeYellowPic.png").convert_alpha()
resumeBlackPic = image.load("text/resumeBlackPic.png").convert_alpha()
#####################################################################
#CREDITS IMAGES
creditsText = image.load("text/creditsText.png").convert_alpha() #import credits image
#####################################################################
#MENU BOXES
playNowRect = Rect(600+playYellowPic.get_width()//2, 320, playYellowPic.get_width(), playYellowPic.get_height()) #menu rectangles
instructionsRect = Rect(340+instructionsYellowPic.get_width()//2, 450, instructionsYellowPic.get_width(), instructionsYellowPic.get_height())
optionsRect = Rect(700+optionsYellowPic.get_width()//2, 450, optionsYellowPic.get_width(), optionsYellowPic.get_height())
creditsRect = Rect(500+creditsYellowPic.get_width()//2, 550, creditsYellowPic.get_width(), creditsYellowPic.get_height())
quitRect = Rect(700+optionsYellowPic.get_width()//2, 550, quitYellowPic.get_width(), quitYellowPic.get_height())
backRect = Rect(950+backYellowPic.get_width()//2, 20, backYellowPic.get_width(), backYellowPic.get_height())

#GAME OVER BOXES
diedPlayAgainRect = Rect(480, 410, diedPlayAgainYellow.get_width(), diedPlayAgainYellow.get_height()) #game over rectangles
diedMenuRect = Rect(430, 500, diedMenuYellow.get_width(), diedMenuYellow.get_height())
diedQuitRect = Rect(600 - diedQuitYellow.get_width()//2, 470, diedQuitYellow.get_width(), diedQuitYellow.get_height())

#PAUSE RECTANGLES
resumeRect = Rect(500, 410, resumeYellowPic.get_width(), resumeYellowPic.get_height()) #pause rectangles
pauseQuitRect = Rect(600 - diedQuitYellow.get_width()//2,500, diedQuitYellow.get_width(), diedQuitYellow.get_height())

#RECTANGLES
endSurface = Surface((1200, 800), SRCALPHA) #translucent rectangles
endRect = Rect(0, 0, 1200, 800)
gameOverSurface = Surface((600,400), SRCALPHA)
gameOverRect = Rect(0,0,1200,800)
manRect = Rect(190,153,340,492)
girlRect = Rect(680,153,340,492)
#####################################################################
#MENU FUNCTIONS
def menu():
    if not musicChannel.get_busy(): #if the music is not already playing
        musicChannel.play(introSong) #play the intro song
    screen.fill((0,0,0)) #filling the screen black each frame
    screen.blit(titlePic,(-150,0)) #blitting the title picture
    screen.blit(titleTextPic,((width-titleTextPic.get_width())//2,100)) #blitting the title text picture
    if playNowRect.collidepoint(mx,my): #if the mouse hovers over the play rectangle
        screen.blit(playWhitePic,(600+playWhitePic.get_width()//2,320)) #blit the white version of the image
    else:
        screen.blit(playYellowPic,(600+playYellowPic.get_width()//2,320)) #blit the yellow version of the image
    if instructionsRect.collidepoint(mx,my): #if the mouse hovers over the instructions rectangle
        screen.blit(instructionsWhitePic,(340+instructionsWhitePic.get_width()//2,450)) #blit the white version of the image
    else:
        screen.blit(instructionsYellowPic,(340+instructionsWhitePic.get_width()//2,450)) #blit the yellow version of the image
    if optionsRect.collidepoint(mx,my): #if the mouse hovers over the options rectangle
        screen.blit(optionsWhitePic,(700+optionsWhitePic.get_width()//2,450)) #blit the white version of the image
    else:
        screen.blit(optionsYellowPic,(700+optionsYellowPic.get_width()//2,450)) #blit the white version of the image
    if creditsRect.collidepoint(mx,my): #if the mouse hovers over the credits rectangle
        screen.blit(creditsWhitePic,(500+creditsWhitePic.get_width()//2,550)) #blit the white version of the image
    else:
        screen.blit(creditsYellowPic,(500+creditsYellowPic.get_width()//2,550)) #blit the white version of the image
    if quitRect.collidepoint(mx,my): #if the mouse hovers over the quit rectangle
        screen.blit(quitWhitePic,(700+optionsYellowPic.get_width()//2,550)) #blit the white version of the image
    else:
        screen.blit(quitYellowPic,(700+optionsYellowPic.get_width()//2,550)) #blit the white version of the image
    
    if playNowRect.collidepoint(mx,my) and release: #if the mouse hovers over the play rectangle and mouse is released
        effectChannel.play(clickSound)
        return 'playNow' #return playNow (switching the mode)
    if instructionsRect.collidepoint(mx,my) and release: #if the mouse hovers over the instructions rectangle and mouse is released
        effectChannel.play(clickSound)
        return 'instructions' #return instructions (switching the mode)
    if optionsRect.collidepoint(mx,my) and release: #if the mouse hovers over the options rectangle and mouse is released
        effectChannel.play(clickSound)
        return 'options' #return options (switching the mode)
    if creditsRect.collidepoint(mx,my) and release: #if the mouse hovers over the credits rectangle and mouse is released
        effectChannel.play(clickSound)
        return 'credits' #return credits (switching the mode)
    if quitRect.collidepoint(mx,my) and release: #if the mouse hovers over the quit rectangle and mouse is released
        return 'quit' #return quit (switching the mode)
    clock.tick(60)
    return 'menu' #return menu (keeping the same mode)

def playNow():
    global manFrame,girlFrame,manRect,girlRect,name,hero #setting global variables
    if not musicChannel.get_busy(): #if the music is not already playing
        musicChannel.play(introSong) #play the intro song
    screen.fill((0,0,0)) #fill the screen black each frame
    screen.blit(titleTwoPic,(0,0)) #blit the title picture
    screen.blit(chooseCharacterText,((width-chooseCharacterText.get_width())//2-40,30)) #blit the chose your character text picture
    screen.blit(callumText,(240,675)) #blit the man name text
    screen.blit(melitaText,(735,675)) #blit the girl name text
    if manRect.collidepoint(mx,my): #if the mouse hovers over the man rectangle
        draw.rect(screen,((0,0,255)),manRect,5) #draw the man rectangle
        screen.blit(manWalkingPics[1][int(manFrame)%9],(210,160)) #blit the man image
        manFrame+=0.3 #increase the frame to move to the next picture (walking animations)
    else:
        manFrame=0 #reset the frame
        screen.blit(manWalkingPics[1][manFrame],(210,160)) #blit the original image
        
    if girlRect.collidepoint(mx,my): #if the mouse hovers over the girl rectangle
        draw.rect(screen,((252,78,223)),girlRect,5) #draw the girl rectangle
        screen.blit(girlWalkingPics[1][int(girlFrame)%9],(710,170)) #blit the girl image
        girlFrame+=0.3 #increase the frame to move to the next picture (walking animations)
    else:
        girlFrame=0 #reset the frame
        screen.blit(girlWalkingPics[1][girlFrame],(710,170)) #blit the original image
        
    if backRect.collidepoint(mx,my): #if the mouse hovers over the back rectangle
        screen.blit(backWhitePic,(950+backWhitePic.get_width()//2,20)) #blit the white version of the image
    else:
        screen.blit(backYellowPic,(950+backYellowPic.get_width()//2,20)) #blit the yellow version of the image
    if backRect.collidepoint(mx,my) and release: #if the mouse is released on the back rectangle
        effectChannel.play(clickSound) #play the click sound
        return 'menu' #return menu (switching the mode)
    
    if manRect.collidepoint(mx,my) and release:
        hero='man'
        musicChannel.fadeout(2000) #fade the music out
        effectChannel.play(clickSound) #play the click sound
        return 'game' #return game (switching the mode)
    if girlRect.collidepoint(mx,my) and release:
        hero='girl'
        musicChannel.fadeout(2000) #fade the music out
        effectChannel.play(clickSound) #play the click sound
        return 'game' #return game (switching the mode)
    clock.tick(45) #slow down the frame rate for the walking animation
    return 'playNow' #return playNow (keeping the same mode)

def instructions():
    screen.fill((0,0,0)) #fill the screen black
    screen.blit(titleTwoPic,(0,0)) #blit the title pic
    screen.blit(instructionsPic, (300, 40)) #blit the  instructions pic
    screen.blit(keyImage, (75 - keyImage.get_width()//2, 170)) #blit the key pic
    screen.blit(healthImage, (75 - healthImage.get_width()//2, 225)) #blit the key pic
    screen.blit(swordImage, (75 - swordImage.get_width()//2, 290)) #blit the sword pic
    screen.blit(portalImage, (75 - portalImage.get_width()//2, 370)) #blit the portal pic
    screen.blit(levelGate, (75 - levelGate.get_width()//2, 480)) #blit the gate pic
    screen.blit(spikePic, (75 - spikePic.get_width()//2, 590))  #blit the spike pic

    keyText = mediumFont.render("Collect all keys to unlock the final level.", True, (255, 255, 255)) #making fonts for each image
    heartText = mediumFont.render("Pickup hearts to heal yourself.", True, (255, 255, 255))
    swordText = mediumFont.render("Pickup swords to increase your damage to enemies.", True, (255, 255, 255))
    portalText = mediumFont.render("Walk into portals to advance to the next level.", True, (255, 255, 255))
    gateText = mediumFont.render("Kill all enemies in a level to unlock the gates.", True, (255, 255, 255))
    spikeText = mediumFont.render("Stepping on spikes will damage you. Avoid them!", True, (255, 255, 255))

    keyControl = mediumFont.render("Use the WASD keys to move.", True, (255, 255, 255)) #making fonts for keyboard controls
    spaceControl = mediumFont.render("Press space to attack.", True, (255, 255, 255))
    shiftControl = mediumFont.render("Hold shift to sprint.", True, (255, 255, 255))

    screen.blit(keyText, (150, 180)) #blitting each text on the screen
    screen.blit(heartText, (150, 235))
    screen.blit(swordText, (150, 300))
    screen.blit(portalText, (150, 400))
    screen.blit(gateText, (150, 510))
    screen.blit(spikeText, (150, 620))
    screen.blit(keyControl, (760, 180))
    screen.blit(spaceControl, (800, 380))
    screen.blit(shiftControl, (810, 580))

    screen.blit(keyControlPic, (800, 220)) #blit the keyboard control pic
    screen.blit(spaceControlPic, (800, 420))
    
    if backRect.collidepoint(mx,my): #if the mouse hovers over the back rectangle
        screen.blit(backWhitePic,(950+backWhitePic.get_width()//2,20)) #blit the white version of the image
    else:
        screen.blit(backYellowPic,(950+backYellowPic.get_width()//2,20)) #blit the yellow version of the image
    if backRect.collidepoint(mx,my) and release: #if the mouse is released on the back rectangle
        effectChannel.play(clickSound) #play the click sound
        return 'menu' #return menu (switching the mode)
    return 'instructions' #return instructions (keeping the same mode)

def options():
    global musicVolume, musicSliderRect, effectVolume, effectSliderRect, sliding #setting global variables
    screen.fill((0,0,0)) #filling the screen
    screen.blit(titleTwoPic,(0,0)) #blit the title pic
    screen.blit(musicVolumePic, (650 - musicVolumePic.get_width()//2, 250 )) #blit the music text pic
    screen.blit(effectVolumePic, (650 - effectVolumePic.get_width()//2, 550  )) #blit the effectrt text pic
    if backRect.collidepoint(mx,my): #if the mouse hovers over the back rectangle
        screen.blit(backWhitePic,(950+backWhitePic.get_width()//2,20)) #blit the white version of the image
    else:
        screen.blit(backYellowPic,(950+backYellowPic.get_width()//2,20)) #blit the yellow version of the image
    if backRect.collidepoint(mx,my) and release: #if the mouse is released on the the back rect
        effectChannel.play(clickSound) #play the click sound
        return 'menu' #return menu (switching the mode)
    
    if musicVolumeRect.collidepoint(mx,my) and sliding and mb[0]==1: #if the mouse is clicked on the music slider rect
        if mx < 460: #if the mouse is less than 460 pixels
            musicSliderRect.x = 450 #set the slider rect y coordinate at 450
            musicVolume = 0 #music volume variable is set to 0
            musicSliderRect = Rect(450, 180, 20, 60) #reset the music rectangle
        elif mx > 840: #if the mouse is more than 460 pixels
            musicSliderRect.x = 850 #set the slider rect y coordinate at 850
            musicVolume = 1 #music volume variable is set to 1
            musicSliderRect = Rect(830, 180, 20, 60) #reset the music rectangle
        else:
            musicSliderRect.x = mx - 10 #set the slider rectangle based on the mouse
            musicVolume = (musicSliderRect.x - 350)/500 #set the music volume
            musicSliderRect = Rect(musicVolume*500 + 350, 180, 20, 60) #reset the music rectangle based on the slider coordinates
            
    musicChannel.set_volume(musicVolume) #set the music channel volume based on the variable
    bossChannel.set_volume(musicVolume) #set the boss channel volume based on the variable
    draw.rect(screen,((180, 187, 198)), musicBarRect) #draw the music rect
    draw.rect(screen,((232, 232, 27)), musicSliderRect) #draw the slider rect

    if effectVolumeRect.collidepoint(mx,my) and sliding and mb[0]==1: #if the mouse is clicked on the music slider rect
        if mx < 460: #if the mouse is less than 460 pixels
            effectSliderRect.x = 450 #set the slider rect y coordinate at 450
            effectVolume = 0 #effect volume variable is set to 0
            effectSliderRect = Rect(450, 480, 20, 60) #reset the effect rectangle
        elif mx > 840: #if the mouse is more than 460 pixels
            effectSliderRect.x = 850 #set the slider rect y coordinate at 850
            effectVolume = 1 #effect volume variable is set to 1
            effectSliderRect = Rect(830, 480, 20, 60) #reset the effect rectangle
        else:  #if the mouse is between 460 and 840 pixels
            effectSliderRect.x = mx - 10 #set the slider rectangle based on the mouse
            effectVolume = (effectSliderRect.x - 350)/500 #set the effect volume
            efectSliderRect = Rect(effectVolume*500 + 350, 80, 20, 60) #reset the effect rectangle based on the slider coordinates
     
    effectChannel.set_volume(effectVolume) #set the effect channel volume based on the variable
    draw.rect(screen,((180, 187, 198)), effectBarRect) #draw the effect rect
    draw.rect(screen,((232, 232, 27)), effectSliderRect) #draw the slider rect
    return 'options' #return options (keeping the same mode)

def credits():
    screen.fill((0,0,0)) #filling the screen black each frame
    screen.blit(titleTwoPic,(0,0)) #blit the title pic
    screen.blit(creditsText,((width-creditsText.get_width())//2,150)) #blit the credits pic
    if backRect.collidepoint(mx,my): #if the mouse hovers over the back rect
        screen.blit(backWhitePic,(950+backWhitePic.get_width()//2,20)) #blit the white version of the image
    else:
        screen.blit(backYellowPic,(950+backYellowPic.get_width()//2,20)) #blit the yellow version of the image
    if backRect.collidepoint(mx,my) and release: #if the mouse is released on the rectangle
        effectChannel.play(clickSound) #play the click sound
        return 'menu' #return menu (switching the mode)
    return 'credits' #return credits (keeping the same mode)

def pause():
    global pauseTimes #setting global variables
    if pauseTimes == 0: #if the pause variable is 0 (stops the translucent surface from blitting many times to make an opaque surface)
        optionsChannel.play(pauseSound) #play the pause sound
        musicChannel.pause() #pause the music
        effectChannel.pause() #pause the effects
        bossChannel.pause() #pause the boss music
        draw.rect(endSurface,(1,1,1,150), endRect) #draw the rectangle for the translucent surface
        screen.blit(endSurface, (0,0)) #blit the translucent surface
        draw.rect(gameOverSurface,(255,255,255,175), gameOverRect) #draw the rectangle for the 2nd translucent surface
        screen.blit(gameOverSurface, (300,200)) #blit the second translucent surface
        pauseTimes +=1 #add to the pause variable so this part of the function does not repeat
    screen.blit(pausedPic, (600 - pausedPic.get_width()//2, 275)) #blit the pause picture
    if resumeRect.collidepoint(mx,my): #if the mouse hovers over the resume rectangle
        screen.blit(resumeBlackPic, (500,410)) #blit the black version of the image
    else:
         screen.blit(resumeYellowPic, (500,410)) #blit the yellow version of the image
    if pauseQuitRect.collidepoint(mx,my): #if the mouse hovers over the quit rectangle
        screen.blit(diedQuitBlack, (600 - diedQuitYellow.get_width()//2, 500)) #blit the black version of the image
    else:
        screen.blit(diedQuitYellow, (600 - diedQuitYellow.get_width()//2, 500)) #blit the yellow version of the image
    if resumeRect.collidepoint(mx,my) and release: #if the mouse is released on the resume rectangle
        pauseTimes = 0 #reset the pause times variable
        musicChannel.unpause() #unpause the music
        effectChannel.unpause() #unpause the effects
        bossChannel.unpause() #unpause the boss music
        return 'game' #return game (switching the mode back to the game)
    if pauseQuitRect.collidepoint(mx,my) and release: #if the mouse is released on the quit rectangle
        return 'quit' #return quit (switching the modes)
    return 'pause' #return pause (keeping the same mode)

def gameOver():
    global mode, endTimes #setting global variables
    if endTimes == 0: #if the end variable is 0 (stops the translucent surface from blitting many times to make an opaque surface)
        draw.rect(endSurface,(1,1,1,150), endRect) #draw the rectangle for the translucent surface
        screen.blit(endSurface, (0,0)) #blit the translucent surface
        draw.rect(gameOverSurface,(255,255,255,175), gameOverRect) #draw the rectangle for the 2nd translucent surface
        screen.blit(gameOverSurface, (300,200)) #blit the 2nd translucent surface
        musicChannel.stop() #stop the music
        effectChannel.stop() #stop the effects
        bossChannel.stop() #stop the boss music
        optionsChannel.play(deathSound) #play the death sound
        endTimes +=1 #add to the end variable so this part of the function does not repeat
    screen.blit(diedText, (425,230)) #blit the dies text picture
    if diedQuitRect.collidepoint(mx,my): #if the mouse hovers over the quit rectangle
        screen.blit(diedQuitBlack, (600 - diedQuitYellow.get_width()//2, 470)) #blit the black version of the image
    else:
        screen.blit(diedQuitYellow, (600 - diedQuitYellow.get_width()//2, 470)) #blit the yellow version of the image
    if diedQuitRect.collidepoint(mx,my) and release: #if the mouse is released on the quit rectangle
        return 'quit' #return quit (switching the mode)
    return 'game over' #return game over (keeping the same mode)

def gameComplete():
    global completeTimes #setting global variables
    if completeTimes == 0: #if the complete variable is 0 (stops the translucent surface from blitting many times to make an opaque surface)
        draw.rect(endSurface,(1,1,1,150), endRect) #draw the rectangle for the translucent surface
        screen.blit(endSurface, (0,0)) #blit the translucent surface
        draw.rect(gameOverSurface,(255,255,255,175), gameOverRect) #draw the rectangle for the 2nd translucent surface
        screen.blit(gameOverSurface, (300,200)) #blit the 2nd translucent surface
        musicChannel.stop() #stop the music 
        bossChannel.stop() #stop the boss music
        completeTimes +=1 #add to the complete variable so this part of the function does not repeat
    screen.blit(winnerPic, (320, 230)) #blit the winner pic
    if not musicChannel.get_busy(): #if the music if not already playing
        musicChannel.play(winnerSong) #play the winner song
    if diedQuitRect.collidepoint(mx,my): #if the mouse hovers over the quit rectangle 
        screen.blit(diedQuitBlack, (600 - diedQuitYellow.get_width()//2, 470)) #blit the black version of the image
    else:
        screen.blit(diedQuitYellow, (600 - diedQuitYellow.get_width()//2, 470)) #blit the yellow version of the image
    if diedQuitRect.collidepoint(mx,my) and release: #if the mouse is released on the quit rectangle
        return 'quit'  #return quit (switching the mode)
    return 'gameComplete' #return gameComplete (keeping the same mode)

#####################################################################
#GAME ANIMATION FUNCTIONS
def handleInput(keys):
    x_m = 0 #net x movement
    y_m = 0 #net y movement

    x_dict = {-1: 'left', #dictionairies for net movement (getting the state)
               1: 'right'}
    y_dict = {-1: 'up',
               1: 'down'}

    if keys[K_a]: #if a is pressed
        x_m -= 1
    if keys[K_d]: #if d is pressed
        x_m += 1
    if keys[K_w]: #if w is pressed
        y_m -= 1
    if keys[K_s]: #if s is pressed
        y_m += 1

    if (x_m and y_m) or x_m: #if there is movement right to left
        return x_dict[x_m] #return the state 
    elif y_m: #if there is movement up or down
        return y_dict[y_m] #return the state 


def animate(frames, keys):
    global frame, attacking #setting global variables
    action = False #setting the action variable to false

    for key in [K_w, K_a, K_s, K_d]: #for each key for movement
        if keys[key]: #if a key is pressed
            action = True #action is true (movement)
            break #stop this part of the function

    if action or attacking: #if there is movement or the user is attacking
        if player.sprinting == False: #if sprinting is false
            frame += 0.20 #increase the frame slowly
        else:
            frame += 0.40 #increase the frame quickly
        if int(frame) == len(frames[state]): #once the attacking animation finished
            attacking = False #set attacking to false
        frame %= len(frames[state]) #making sure the frame does not go over and resets it

    if state == 'left': #is the state is left
        screen.blit(frames[state][int(frame)], (player.rect.x - (frames[state][int(frame)].get_width()) + 20, player.rect.y)) #blit the images a certain way
    elif state == 'up': #if the state is up
        screen.blit(frames[state][int(frame)], (player.rect.x, player.rect.y - (frames[state][int(frame)].get_height()) + 50)) #blit the images a certain way
    else:
        screen.blit(frames[state][int(frame)], player.rect) #blit the image normally
        
#################################################
#Class for blocks (walls)
class Block:
    def __init__(self, x, y, w, h, index):
        self.rect = Rect(x, y, w, h)#create rect for each object
        if not levelsblocksList or self not in levelsblocksList[index]: 
            levelsblocksList[index].append(self)#append each object to a list of blocks
        
    def update(self):#method to create block
        if 0 <= index < 3:#if in the first 3 levels
            self.outline = grassOutline#grass wall
        elif 3 <= index < 6:#if in levels 3-5
            self.outline = dirtOutline#dirt wall
        elif 6<= index < 9:#if in levels 6-8
            self.outline = sandOutline#sand wall
        elif index == 9:#if in level 9
            self.outline = darkOutline#dark wall
        else:#if in boss level
            self.outline = bossOutline#boss level wall

        screen.blit(self.outline, (self.rect))#blit image where the block's rect is
#################################################
#class for spikes
class Spike:
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create rect for each object
        if not spikeList or self not in spikeList[index]:
            spikeList[index].append(self)#append each object to a list of spikes

    def update(self):#method to create spike
        screen.blit(spikeImage, (self.rect))#blit image where the spike's rect is
#################################################
#class for gates in between levels
class Gate:
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create rect for each object
        if not gatesList or self not in gatesList[index]:
            gatesList[index].append(self)#append each object to a list of gates

    def update(self):#method to create gates
        screen.blit(levelGate, (self.rect))#blit image where the gate's rect is

#################################################
#class for gate blocking boss level
class BossGate:
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create rect for each object
        if not bossgateList or self not in bossgateList[index]:
            bossgateList[index].append(self)#append each object to a list of bossgates

    def update(self):#method to create bossgate
        screen.blit(finalGate, (self.rect))#blit image where rect it
#################################################
#class for hitboxes
class HitRect:
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create a rect for hitboxes

#################################################
#class for player
class Player:
    def __init__(self, x, y, w, h, hp, stamina):
        self.rect = Rect(x, y, w, h)#create a rect for player
        self.hp = hp#set object's hp to inputted number
        self.stamina = stamina#set object's stamina to inputted number
        self.sprinting = False#set sprinting to false
        
    def take_damage(self):#create method for player taking damage
        global mode, endTimes
        self.hp -= damage#subtract damage from player's health
        if self.hp < 0:#if player's health is less than 0
            self.hp = 0#set player's health to 0
            mode = 'game over'#game over screen
                
    def move(self):#create method for moving
        if not attacking:
            if key.get_pressed()[K_w]:#if player presses w
                self.rect.y -= 1#move up by 1 pixel
            if key.get_pressed()[K_s]:#if player presses s
                self.rect.y += 1#move down by 1 pixel
            self.collide_y(key.get_pressed()[K_w], key.get_pressed()[K_s])#call function for collision
            
            if key.get_pressed()[K_a]:#if player presses a
                self.rect.x -= 1#move left 1 pixel
            if key.get_pressed()[K_d]:#if player presses d
                self.rect.x += 1#move right 1 pixel
            self.collide_x(key.get_pressed()[K_a], key.get_pressed()[K_d])#call function for collision

        if not attacking and key.get_pressed()[K_LSHIFT] and self.stamina > 0 or not attacking and key.get_pressed()[K_RSHIFT] and self.stamina > 0:#if pressing left or right shift key and stamina > 0
            if key.get_pressed()[K_w]:#if player presses w
                self.rect.y -= 2#move up by 2 MORE pixels
            if key.get_pressed()[K_s]:#if player presses s
                self.rect.y += 2#move down by 2 MORE pixels
            self.collide_y(key.get_pressed()[K_w], key.get_pressed()[K_s])#call function for collision
            
            if key.get_pressed()[K_a]:#if player presses a
                self.rect.x -= 2#move left by 2 MORE pixels
            if key.get_pressed()[K_d]:#if player presses d
                self.rect.x += 2#move right by 2 MORE pixels
            self.collide_x(key.get_pressed()[K_a], key.get_pressed()[K_d])#call function for collision
            self.stamina -= 1#subtract 1 from stamina
            self.sprinting = True#set sprinting variable to True
        else:
            self.sprinting = False#set sprinting variable to False
                
             
    def collide_y(self, up, down):#up down collision
        for block in levelsblocksList[index]:#for all blocks in level
            if self.rect.colliderect(block.rect):#if player rect collides with block rect
                if up:#if moving up
                    self.rect.top = block.rect.bottom#set player rect top equal to block rect bottom
                if down:#if moving down
                    self.rect.bottom = block.rect.top#set player rect bottom equal to block rect top
        for gate in gatesList[index]:#for all gates in level
            if self.rect.colliderect(gate.rect):#if player rect collides with gate rect
                if up:#if moving up
                    self.rect.top = gate.rect.bottom#set player rect top equal to gate rect bottom
                elif down:#if moving down
                    self.rect.bottom = gate.rect.top#set player rect bottom equal to gate rect top

    def collide_x(self, left, right):#left right collision
        for block in levelsblocksList[index]:#for all blocks in level
            if self.rect.colliderect(block.rect):#if player rect collides with block rect
                if left:#if moving left
                    self.rect.left = block.rect.right#set player left equal to block right
                if right:#if moving right
                    self.rect.right = block.rect.left#set player right equal to block left
        for gate in gatesList[index]:#for all gates in level
            if self.rect.colliderect(gate.rect):#if player rect collides with gate rect
                if left:#if moving left
                    self.rect.left = gate.rect.right#set player left equal to gate right
                if right:#if moving right
                    self.rect.right = gate.rect.left#set player right equal to gate left
        for bossgate in bossgateList[index]:#for all bossgates
            if self.rect.colliderect(bossgate.rect):#if player rect collides with bossgate rect
                if left:#if moving left
                    self.rect.left = bossgate.rect.right#set player left equal to bossgate right
                if right:#if moving right
                    self.rect.right = bossgate.rect.left#set player right equal to bossgate left

    def update(self):#function for updating player
        if self.hp < 100:#if health is less than 100
            self.hp += 0.01#passive regen of 0.01
        if self.stamina < 100:#if stamina is less than 100
            self.stamina += 0.3#passive regen of 0.3
########################################################
class Sword:#class for better swords
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create rect for object
        if not swordList or self not in swordList[index]:
            swordList[index].append(self)#append object to list

    def collide(self):#function for when player picks up sword
        swordList[index] = []#empty swordlist[index]
        levelsList[index][4][6] = 'o'#change level map to remove sword

    def update(self):#function for creating sword
        screen.blit(swordImage, (self.rect))#blit image of sword at sword rect

########################################################
#class for orc enemy
class Orc:
    def __init__(self, x, y, w, h, hp):
        self.rect = Rect(x, y, w, h)#create rect for object
        self.hp = hp#set orc hp to inputted number
        self.frame = 0#set frame to 0
        self.attacking = False#set attacking to false
        self.direction = 'none'#set direction to none
        self.dict = orcFrameDict#set dictionary to orcFrameDict
        self.hpRect = Rect(x, y-50, self.hp * 0.5, 3)#create rectangle to display hp
        self.hpbackRect = Rect (x-2, y-52, self.hp * 0.5 + 4, 5)#create rectangle as background for hp
        if not orcList or self not in orcList[index]:
            orcList[index].append(self)#append object to orcList
            enemiesList[index].append(self)#append object to enemiesList

    def healthbar(self):#function for enemy healthbar
        draw.rect(screen, (222, 222, 222), self.hpbackRect)#draw healthbar background
        draw.rect(screen, (255, 0, 0), self.hpRect)#draw healthbar

    def move(self):#function for moving enemy
        if player.rect.y < self.rect.y:#if player is above enemy
            self.rect.y -= 1#move enemy up one pixel
            self.direction = 'up'#direction is up
        if player.rect.y > self.rect.y:#if player is below enemy
            self.rect.y += 1#move enemy down one pixel
            self.direction = 'down'#direction is down
        self.collide_y('up', 'down')#enemy collision
        if player.rect.x < self.rect.x:#if player is left of enemy
            self.rect.x -= 1#move enemy left one pixel
            self.direction = 'left'#direction is left
        if player.rect.x > self.rect.x:#if player is right of enemy
            self.rect.x += 1#move enemy right one pixel
            self.direction = 'right'#direction is right
        self.collide_x('left', 'right')#enemy collision
        if self.rect.colliderect(player.rect):#if orc's rect collides with player rect
            self.attacking = True#set attacking to true
        if self.attacking == False:#if attacking is false:
            self.dict = orcWalkFrameDict#use walking dictionary
        else:#if attacking
            self.dict = orcAttackFrameDict#use attacking dictionary

    def animate(self):
        self.frame += 0.15 #increase the frame
        if int(self.frame) == len(self.dict[self.direction]): #if the animation finished
            self.attacking = False #set attcking to false
        self.frame %= len(self.dict[self.direction])  #making sure the frame does not go over and resets it

        screen.blit(self.dict[self.direction][int(self.frame)], self.rect)

    def take_damage(self):#function for enemy damage
        if swordlevel == 0:#if player has 0 sword upgrades
            self.hp -= 0.4#subtract 0.4 from orc health
        if swordlevel == 1:#if player has 1 sword upgrade
            self.hp -= 0.6#subtract 0.6 from orc health
        if swordlevel == 2:#if player has 2 sword upgrades
            self.hp -= 0.9#subtract 0.9 from orc health
        if self.hp < 0:#if orc has less than 0 health (die)
            orcList[index].remove(self)#remove orc from orcList
            enemiesList[index].remove(self)#remove orc from enemiesList
                

    def collide_y(self, up, down):#collision for orc with objects(same as player collision)
        for block in levelsblocksList[index]:
            if self.rect.colliderect(block.rect):
                if self.direction == 'up':
                    self.rect.top = block.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = block.rect.top
        for gate in gatesList[index]:
            if self.rect.colliderect(gate.rect):
                if self.direction == 'up':
                    self.rect.top = gate.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = gate.rect.top

    def collide_x(self, left, right):#collision for orc with objects(same as player collision)
        for block in levelsblocksList[index]:
            if self.rect.colliderect(block.rect):
                if self.direction == 'left':
                    self.rect.left = block.rect.right
                elif self.direction == 'right':
                    self.rect.right = block.rect.left
        for gate in gatesList[index]:
            if self.rect.colliderect(gate.rect):
                if self.direction == 'left':
                    self.rect.left = gate.rect.right
                elif self.direction == 'right':
                    self.rect.right = gate.rect.left

    def update(self):#function for updating orc
        self.hpRect.center = self.rect.centerx, self.rect.centery - 25#update healthbar rect
        self.hpbackRect.center = self.rect.centerx, self.rect.centery - 25#update healthbarbackrect
        self.hpRect.w = self.hp * 0.5#update width of healthbar
        
###############################################################
class Skeleton:#create class for skeleton enemy
    def __init__(self, x, y, w, h, hp):
        self.rect = Rect(x, y, w, h)#create rect for object
        self.hp = hp#set health for skeleton
        self.frame = 0#set frame to 0
        self.attacking = False#set attacking to false
        self.direction = 'none'#set direction to none
        self.hpRect = Rect(x, y-25, self.hp * 0.5, 3)#create rect for health
        self.hpbackRect = Rect (x-2, y-27, self.hp * 0.5 + 4, 5)#create background rect for health
        if not skeletonList or self not in skeletonList[index]: 
            skeletonList[index].append(self)#append object to skeletonList
            enemiesList[index].append(self)#append object to enemiesList

    def healthbar(self):
        draw.rect(screen, (222, 222, 222), self.hpbackRect)#draw health backgroundrect
        draw.rect(screen, (255, 0, 0), self.hpRect)#draw healthbar

    def move(self):#same movement as orc
        if player.rect.y < self.rect.y:
            self.rect.y -= 1
            self.direction = 'up'
        elif player.rect.y > self.rect.y:
            self.rect.y += 1
            self.direction = 'down'
        self.collide_y('up', 'down')
        if player.rect.x < self.rect.x:
            self.rect.x -= 1
            self.direction = 'left'
        elif player.rect.x > self.rect.x:
            self.rect.x += 1
            self.direction = 'right'
        self.collide_x('left', 'right')
        if self.rect.colliderect(player.rect):
            self.attacking = True
        if self.attacking == False:
            self.dict = skeletonWalkFrameDict
        else:
            self.dict = skeletonAttackFrameDict

    def animate(self): #same animation as orc
        self.frame += 0.25
        if int(self.frame) == len(self.dict[self.direction]):
            self.attacking = False
        self.frame %= len(self.dict[self.direction])

        screen.blit(self.dict[self.direction][int(self.frame)], self.rect)

    def collide_y(self, up, down):#same collision as orc
        for block in levelsblocksList[index]:
            if self.rect.colliderect(block.rect):
                if self.direction == 'up':
                    self.rect.top = block.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = block.rect.top
        for gate in gatesList[index]:
            if self.rect.colliderect(gate.rect):
                if self.direction == 'up':
                    self.rect.top = gate.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = gate.rect.top

    def collide_x(self, left, right):#same collision as orc
        for block in levelsblocksList[index]:
            if self.rect.colliderect(block.rect):
                if self.direction == 'left':
                    self.rect.left = block.rect.right
                if self.direction == 'right':
                    self.rect.right = block.rect.left
        for gate in gatesList[index]:
            if self.rect.colliderect(gate.rect):
                if self.direction == 'left':
                    self.rect.left = gate.rect.right
                elif self.direction == 'right':
                    self.rect.right = gate.rect.left

    def take_damage(self):#function for enemy damage
        if swordlevel == 0:#if player has 0 sword upgrades
            self.hp -= 1#subtract 1 from enemy health
        if swordlevel == 1:#if player has 1 sword upgrade
            self.hp -= 1.3#subtract 1.3 from enemy health
        if swordlevel == 2:#if player has 2 sword upgrades
            self.hp -= 1.7#subtract 1.7 from enemy health
        if self.hp < 0:#if enemy health is less than 0 (die)
            skeletonList[index].remove(self)#remove from skeletonList
            enemiesList[index].remove(self)#remove from enemiesList

    def update(self):#update skeleton
        self.hpRect.center = self.rect.centerx, self.rect.centery - 25
        self.hpbackRect.center = self.rect.centerx, self.rect.centery - 25#update healthbarback
        self.hpRect.w = self.hp * 0.5#update healthbar

#####################################################################
class Keeper:#class for keeper enemy
    def __init__(self, x, y, w, h, hp):
        self.rect = Rect(x, y, w, h)#create rect for object
        self.hp = hp#set health
        self.frame = 0#set frame to 0
        self.attacking = False#set attacking to false
        self.direction = 'none'#set direction to none
        self.hpRect = Rect(x, y-25, self.hp * 0.5, 3)#create healthbar
        self.hpbackRect = Rect (x-2, y-27, self.hp * 0.5 + 4, 5)#create healthbar background
        if not keeperList or self not in keeperList[index]: 
            keeperList[index].append(self)#append self to keeperList
            enemiesList[index].append(self)#append self to enemiesList

    def healthbar(self):#function for healthbar
        draw.rect(screen, (222, 222, 222), self.hpbackRect)#draw healthbar background
        draw.rect(screen, (255, 0, 0), self.hpRect)#draw healthbar

    def move(self):#same movement as skeleton and orc
        if player.rect.y < self.rect.y:
            self.rect.y -= 1
            self.direction = 'up'
        elif player.rect.y > self.rect.y:
            self.rect.y += 1
            self.direction = 'down'
        self.collide_y('up', 'down')
        if player.rect.x < self.rect.x:
            self.rect.x -= 1
            self.direction = 'left'
        elif player.rect.x > self.rect.x:
            self.rect.x += 1
            self.direction = 'right'
        self.collide_x('left', 'right')
        if self.rect.colliderect(player.rect):
            self.attacking = True
        if self.attacking == False:
            self.dict = keeperWalkFrameDict
        else:
            self.dict = keeperAttackFrameDict

    def animate(self): #same animation as skeleton and orc
        self.frame += 0.25
        if int(self.frame) == len(self.dict[self.direction]):
            self.attacking = False
        self.frame %= len(self.dict[self.direction])

        screen.blit(self.dict[self.direction][int(self.frame)], self.rect)

    def collide_y(self, up, down):#same collision as skeleton and orc
        for block in levelsblocksList[index]:
            if self.rect.colliderect(block.rect):
                if self.direction == 'up':
                    self.rect.top = block.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = block.rect.top
        for gate in gatesList[index]:
            if self.rect.colliderect(gate.rect):
                if self.direction == 'up':
                    self.rect.top = gate.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = gate.rect.top

    def collide_x(self, left, right):#same collision as skeleton and orc
        for block in levelsblocksList[index]:
            if self.rect.colliderect(block.rect):
                if self.direction == 'left':
                    self.rect.left = block.rect.right
                elif self.direction == 'right':
                    self.rect.right = block.rect.left
        for gate in gatesList[index]:
            if self.rect.colliderect(gate.rect):
                if self.direction == 'left':
                    self.rect.left = gate.rect.right
                elif self.direction == 'right':
                    self.rect.right = gate.rect.left

    def take_damage(self):#function for enemy damage
        if swordlevel == 0:#if player has 0 sword upgrades
            self.hp -= 0.3#subtract 0.3 from health
        if swordlevel == 1:#if player has 1 sword upgrade
            self.hp -= 0.4#subtract 0.4 from health
        if swordlevel == 2:#if player has 2 sword upgrades
            self.hp -= 0.6#subtract 0.6 from health
        if self.hp < 0:#if enemy has less than 0 health (die)
            keeperList[index].remove(self)#remove self from keeperList
            enemiesList[index].remove(self)#remove self from enemiesList

    def update(self):#function for updating keeper
        self.hpRect.center = self.rect.centerx, self.rect.centery - 25#center healthbar
        self.hpbackRect.center = self.rect.centerx, self.rect.centery - 25#update healthbar background
        self.hpRect.w = self.hp * 0.5#update healthbar

#################################################################
class Boss:#class for boss
    def __init__(self, x, y, w, h, hp):
        self.rect = Rect(x, y, w, h)#rect for boss
        self.hp = hp#set boss health to hp
        self.frame = 0#set frame to 0
        self.attacking = False#set attacking to false
        self.direction = 'none'#set direction to none
        self.hpRect = Rect(310, 730, self.hp * 3, 25)#create healthbar
        self.hpbackRect = Rect (308, 728, self.hp * 3 + 4, 29)#create background for healthbar
        if not bossList or self not in bossList[index]: 
            bossList[index].append(self)#append self to bossList
            enemiesList[index].append(self)#append self to enemiesList

    def healthbar(self):#healthbar for boss
        draw.rect(screen, (222, 222, 222), self.hpbackRect)#draw background for healthbar
        draw.rect(screen, (255, 0, 0), self.hpRect)#draw healthbar
        bossHealthText = mediumFont.render("Boss Health: %i" %(self.hp), True, (0, 0, 0))#render text for boss healthbar
        screen.blit(bossHealthText, (540, 727))#blit text for boss healthbar

    def move(self):#boss movement(same as keeper, skeleton, and orc)
        if player.rect.y < self.rect.y:
            self.rect.y -= 1
            self.direction = 'up'
        elif player.rect.y > self.rect.y:
            self.rect.y += 1
            self.direction = 'down'
        self.collide_y('up', 'down')
        if player.rect.x < self.rect.x:
            self.rect.x -= 1
            self.direction = 'left'
        elif player.rect.x > self.rect.x:
            self.rect.x += 1
            self.direction = 'right'
        self.collide_x('left', 'right')
        if self.rect.colliderect(player.rect):
            self.attacking = True
        if self.attacking == False:
            self.dict = bossWalkFrameDict
        else:
            self.dict = bossAttackFrameDict

    def animate(self): #same animation as skeleton, keeper and orc
        self.frame += 0.25
        if int(self.frame) == len(self.dict[self.direction]):
            self.attacking = False
        self.frame %= len(self.dict[self.direction])

        screen.blit(self.dict[self.direction][int(self.frame)], self.rect)

    def collide_y(self, up, down):#same collision as keeper, skeleton, orc
        for block in levelsblocksList[index]:
            if self.rect.colliderect(block.rect):
                if self.direction == 'up':
                    self.rect.top = block.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = block.rect.top
        for gate in gatesList[index]:
            if self.rect.colliderect(gate.rect):
                if self.direction == 'up':
                    self.rect.top = gate.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = gate.rect.top

    def collide_x(self, left, right):#same collision as keeper, skeleton, orc
        for block in levelsblocksList[index]:
            if self.rect.colliderect(block.rect):
                if self.direction == 'left':
                    self.rect.left = block.rect.right
                elif self.direction == 'right':
                    self.rect.right = block.rect.left
        for gate in gatesList[index]:
            if self.rect.colliderect(gate.rect):
                if self.direction == 'left':
                    self.rect.left = gate.rect.right
                elif self.direction == 'right':
                    self.rect.right = gate.rect.left

    def take_damage(self):#function for boss damage
        if swordlevel == 0:#if player has 0 sword upgrades
            self.hp -= 0.1#subtract 0.1 from boss health
        if swordlevel == 1:#if player has 1 sword upgrade
            self.hp -= 0.2#subtract 0.2 from boss health
        if swordlevel == 2:#if player has 2 sword upgrades
            self.hp -= 0.3#subtract 0.3 from boss health
        if self.hp < 0:#if boss health is less than 0(die)
            bossList[index].remove(self)#remove from bossList
            enemiesList[index].remove(self)#remove from enemiesList

    def update(self):
        self.hpRect.w = self.hp * 3

#################################################################
class LeftMoveBlock:#class for moving left block
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create rect for object
        if not leftmoveList or self not in leftmoveList[index]: 
            leftmoveList[index].append(self)#append to list

    def update(self):
        screen.blit(portalImage,(self.rect.x + 10, self.rect.y))#blit image on rect

class RightMoveBlock:#class for moving right block
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create rect for object
        if not rightmoveList or self not in rightmoveList[index]: 
            rightmoveList[index].append(self)#append to list

    def update(self):
        screen.blit(portalImage, (self.rect.x - 10, self.rect.y))#blit image on rect

########################################################
class ExtraHealth:#class for healthboost
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create rect for object
        if not extrahealthList or self not in extrahealthList[index]:
            extrahealthList[index].append(self)#append self to list

    def use(self):#function for using health boost
        extrahealthList[index] = []#empty list
        levelsList[index][4][4] = 'o'#change map to remove extrahealth

    def update(self):
        screen.blit(healthImage, (self.rect.x, self.rect.y))#blit image on rect

########################################################
class Key:#class for keys
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)#create rect for object
        if not keysList or self not in keysList[index]:
            keysList[index].append(self)#append self to list

    def collide(self):#function for collecting keys
        keysList[index] = []#empty list
        levelsList[index][3][10] = 'o'#change map to remove key

    def update(self):
        screen.blit(keyImage, (self.rect))#blit key image on rect        

########################################################
#LEVELS 1
#LEVEL 1
level1=[['x','x','x','x','x','x','x','x','x','x','x','x'], #creating level
        ['x','o','o','o','o','o','o','e','o','o','g','r'],
        ['x','o','o','o','o','o','o','o','o','o','x','x'],
        ['x','o','o','o','o','o','o','o','o','o','o','x'],
        ['x','x','o','o','h','o','o','o','o','p','o','x'],
        ['l','b','o','o','o','o','o','o','o','p','o','x'],
        ['x','x','o','o','o','o','o','e','o','o','o','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]

level1blocks = [] #list for block in this level
level1orcs = [] #list for orcs in this level
level1skeletons = [] #list for skeletons in this level
level1rightmove = [] #list for right move block in this level
level1leftmove = [] #list for left move block in this level
level1extrahealth = [] #list for health in this level
level1keys = [] #list for keys in this level
level1enemies = [] #list for enemies in this level
level1gates = [] #list for gates in this level
level1keepers = [] #list for keepers in this level
level1bossgate = [] #list for gates in this level
level1sword = [] #list for swords in this level
level1spikes = [] #list for spikes in this level
level1boss = [] #list for boss in this level

#LEVEL 2
level2=[['x','x','x','x','x','x','x','x','x','x','x','x'],
        ['l','g','o','p','o','o','o','o','o','o','e','x'],
        ['x','x','o','p','o','o','o','o','o','o','o','x'],
        ['x','o','o','p','o','o','o','o','o','o','e','x'],
        ['x','o','o','o','o','o','o','o','o','o','x','x'],
        ['x','o','o','o','o','o','o','o','o','e','g','r'],
        ['x','o','o','o','o','o','o','o','o','o','x','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]

level2blocks = []
level2orcs = []
level2skeletons = []
level2rightmove = []
level2leftmove = []
level2extrahealth = []
level2keys = []
level2enemies = []
level2gates = []
level2keepers = []
level2bossgate = []
level2sword = []
level2spikes = []
level2boss = []

#LEVEL 3
level3=[['x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x','o','o','o','o','o','p','o','o','o','o','x'],
        ['x','o','o','o','o','o','p','o','o','o','o','x'],
        ['x','o','o','o','o','o','o','o','o','K','k','x'],
        ['x','x','o','o','h','o','o','o','o','o','o','x'],
        ['l','g','o','o','o','o','p','o','o','o','x','x'],
        ['x','x','o','o','o','o','p','o','o','o','g','r'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]

level3blocks = []
level3orcs = []
level3skeletons = []
level3rightmove = []
level3leftmove = []
level3extrahealth = []
level3keys = []
level3enemies = []
level3gates = []
level3keepers = []
level3bossgate = []
level3sword = []
level3spikes = []
level3boss = []

#LEVEL 4
level4=[['x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x','o','o','o','s','o','o','o','s','o','o','x'],
        ['x','o','o','o','p','o','p','o','p','o','x','x'],
        ['x','o','o','o','s','o','s','o','s','o','g','r'],
        ['x','o','o','o','p','o','p','o','p','o','x','x'],
        ['x','x','o','o','s','o','s','o','s','o','o','x'],
        ['l','g','o','o','o','o','o','o','o','o','s','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]

level4blocks = []
level4orcs = []
level4skeletons = []
level4rightmove = []
level4leftmove = []
level4extrahealth = []
level4keys = []
level4enemies = []
level4gates = []
level4keepers = []
level4bossgate = []
level4sword = []
level4spikes = []
level4boss = []

#LEVEL 5
level5=[['x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x','o','o','o','o','o','s','o','o','o','o','x'],
        ['x','x','o','e','p','o','o','o','o','o','x','x'],
        ['l','g','o','p','o','o','s','o','o','o','g','r'],
        ['x','x','o','p','h','o','o','o','o','o','x','x'],
        ['x','o','o','e','p','o','s','o','o','o','o','x'],
        ['x','o','o','o','o','o','o','o','o','o','o','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]
        

level5blocks = []
level5orcs = []
level5skeletons = []
level5rightmove = []
level5leftmove = []
level5extrahealth = []
level5keys = []
level5enemies = []
level5gates = []
level5keepers = []
level5bossgate = []
level5sword = []
level5spikes = []
level5boss = []

#LEVEL 6
level6=[['x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x','o','p','o','o','o','o','o','o','o','o','x'],
        ['x','x','p','o','o','o','o','o','o','o','o','x'],
        ['l','g','o','o','K','o','o','o','o','K','k','x'],
        ['x','x','p','o','h','o','S','o','o','o','o','x'],
        ['x','o','p','o','o','o','o','o','o','o','x','x'],
        ['x','o','p','o','o','o','o','o','o','o','g','r'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]

level6blocks = []
level6orcs = []
level6skeletons = []
level6rightmove = []
level6leftmove = []
level6extrahealth = []
level6keys = []
level6enemies = []
level6gates = []
level6keepers = []
level6bossgate = []
level6sword = []
level6spikes = []
level6boss = []

#LEVEL 7
level7=[['x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x','o','o','o','o','o','o','o','o','o','o','x'],
        ['x','o','o','o','o','e','o','o','o','e','o','x'],
        ['x','o','o','p','o','p','o','o','o','o','x','x'],
        ['x','o','o','o','o','o','o','o','o','o','g','r'],
        ['x','x','o','p','o','p','o','e','o','o','x','x'],
        ['l','g','o','o','o','o','o','o','o','o','o','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]

level7blocks = []
level7orcs = []
level7skeletons = []
level7rightmove = []
level7leftmove = []
level7extrahealth = []
level7keys = []
level7enemies = []
level7gates = []
level7keepers = []
level7bossgate = []
level7sword = []
level7spikes = []
level7boss = []

#LEVEL 8
level8=[['x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x','s','o','o','o','p','o','o','o','o','e','x'],
        ['x','s','o','p','o','p','o','p','p','o','o','x'],
        ['x','x','o','p','o','p','o','p','o','o','x','x'],
        ['l','g','o','p','h','o','o','p','o','o','g','r'],
        ['x','x','o','p','o','p','o','p','o','p','x','x'],
        ['x','s','o','o','o','p','o','o','o','p','o','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]

level8blocks = []
level8orcs = []
level8skeletons = []
level8rightmove = []
level8leftmove = []
level8extrahealth = []
level8keys = []
level8enemies = []
level8gates = []
level8keepers = []
level8bossgate = []
level8sword = []
level8spikes = []
level8boss = []

#LEVEL 9
level9=[['x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x','s','o','o','o','o','o','o','o','p','s','x'],
        ['x','o','o','o','o','o','o','p','p','p','K','x'],
        ['x','x','o','o','o','o','o','o','o','o','k','x'],
        ['l','g','o','o','h','o','o','p','o','o','x','x'],
        ['x','x','o','o','o','o','o','p','p','o','g','r'],
        ['x','s','o','o','o','o','o','o','p','p','x','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x']]

level9blocks = []
level9orcs = []
level9skeletons = []
level9rightmove = []
level9leftmove = []
level9extrahealth = []
level9keys = []
level9enemies = []
level9gates = []
level9keepers = []
level9bossgate = []
level9sword = []
level9spikes = []
level9boss = []

#LEVEL 10
level10=[['x','x','x','x','x','x','x','x','x','x','x','x'],
         ['x','x','x','x','x','x','x','x','x','x','x','x'],
         ['x','o','o','o','o','o','o','o','o','o','e','x'],
         ['x','o','o','p','p','p','p','p','p','p','o','x'],
         ['x','o','o','o','o','o','S','o','K','o','o','x'],
         ['l','o','o','p','p','p','p','p','p','p','o','x'],
         ['x','o','o','o','o','o','o','o','o','o','e','x'],
         ['x','x','x','x','x','x','x','x','x','x','x','x']]

level10blocks = []
level10orcs = []
level10skeletons = []
level10rightmove = []
level10leftmove = []
level10extrahealth = []
level10keys = []
level10enemies = []
level10gates = []
level10keepers = []
level10bossgate = []
level10sword = []
level10spikes = []
level10boss = []

#LEVEL 11 BOSS LEVEL
level11=[['x','x','x','x','x','x','x','x','x','x','x','x'],
         ['x','o','o','p','o','o','p','o','o','o','e','x'],
         ['x','o','o','p','o','o','p','o','o','o','o','x'],
         ['x','B','o','p','o','o','p','o','o','o','o','x'],
         ['x','o','o','o','h','o','o','o','o','o','o','x'],
         ['x','o','o','p','o','o','p','o','o','o','o','x'],
         ['x','o','o','p','o','o','p','o','o','o','e','x'],
         ['x','x','x','x','x','x','x','x','x','x','x','x']]

level11blocks = []
level11orcs = []
level11skeletons = []
level11rightmove = []
level11leftmove = []
level11extrahealth = []
level11keys = []
level11enemies = []
level11gates = []
level11keepers = []
level11bossgate = []
level11sword = []
level11spikes = []
level11boss = []
        

########################################################
#LISTS
orcList = [level1orcs, level2orcs, level3orcs, level4orcs, level5orcs, level6orcs, level7orcs, level8orcs, level9orcs, level10orcs, level11orcs]
skeletonList = [level1skeletons, level2skeletons, level3skeletons, level4skeletons, level5skeletons, level6skeletons, level7skeletons, level8skeletons, level9skeletons, level10skeletons, level11skeletons]
keeperList = [level1keepers, level2keepers, level3keepers, level4keepers, level5keepers, level6keepers, level7keepers, level8keepers, level9keepers, level10keepers, level11keepers]
enemiesList = [level1enemies, level2enemies, level3enemies, level4enemies, level5enemies, level6enemies, level7enemies, level8enemies, level9enemies, level10enemies, level11enemies]
rightmoveList = [level1rightmove, level2rightmove, level3rightmove, level4rightmove, level5rightmove, level6rightmove, level7rightmove, level8rightmove, level9rightmove, level10rightmove, level11rightmove]
leftmoveList = [level1leftmove, level2leftmove, level3leftmove, level4leftmove, level5leftmove, level6leftmove, level7leftmove, level8leftmove, level9leftmove, level10leftmove, level11leftmove]
levelsblocksList = [level1blocks, level2blocks, level3blocks, level4blocks, level5blocks, level6blocks, level7blocks, level8blocks, level9blocks, level10blocks, level11blocks]
levelsList = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11]
bossList = [level1boss, level2boss, level3boss, level4boss, level5boss, level6boss, level7boss, level8boss, level9boss, level10boss, level11boss]
gatesList = [level1gates, level2gates, level3gates, level4gates, level5gates, level6gates, level7gates, level8gates, level9gates, level10gates, level11gates]
keysList = [level1keys, level2keys, level3keys, level4keys, level5keys, level6keys, level7keys, level8keys, level9keys, level10keys, level11keys]
swordList = [level1sword, level2sword, level3sword, level4sword, level5sword, level6sword, level7sword, level8sword, level9sword, level10sword, level11sword]
spikeList = [level1spikes, level2spikes, level3spikes, level4spikes, level5spikes, level6spikes, level7spikes, level8spikes, level9spikes, level10spikes, level11spikes]
extrahealthList = [level1extrahealth, level2extrahealth, level3extrahealth, level4extrahealth, level5extrahealth, level6extrahealth, level7extrahealth, level8extrahealth, level9extrahealth, level10extrahealth, level11extrahealth]
bossgateList = [level1bossgate, level2bossgate, level3bossgate, level4bossgate, level5bossgate, level6bossgate, level7bossgate, level8bossgate, level9bossgate, level10bossgate, level11bossgate]
########################################################
#FONT
comicFont = font.SysFont("comic sans ms", 15) #creating small font
mediumFont = font.SysFont("comic sans ms", 20) #creating medium dont
largeFont = font.SysFont("comic sans ms", 40) #creating large font
########################################################
#VARIABLES
index = 0 #index
keyCount = 0 #count for keys
swordlevel = 0 #amount of sword upgrades
attack = False #attack variable
release = False #release variable for mouse
sliding = False #sliding variable
attacking = False #attacking variable for player
mb = mouse.get_pressed()
mx, my = mouse.get_pos()
keys = key.get_pressed()
mode = 'menu' #mode variable
hero = 'none' #hero variable (for choosing character)
frame = 0 #frame counter for character
endTimes = 0 #end counter
pauseTimes = 0 #pause counter
completeTimes = 0 #complete counter
state = 'down' #player state variable
pics = [] #pictures list
move = 0 #moving variable
manFrame = 0 #title screen man frame counter
girlFrame = 0 #title screen girl frame counter
ANIMATEEVENT = USEREVENT + 1 #user event for animating
animate_timer = time.set_timer(ANIMATEEVENT, 60) #timer for animation

def drawMap(level, index):#function for creating map(takes in 2D List)
    bx = by = 0#set bx and by to 0
    for r in level:
        for c in r:#run through every item and check string, certain strings create certain objects using classes
            if c == 'x':
                Block(bx, by, 100, 100, index)
            if c == 'e':
                Orc(bx, by, 23, 40, 100)
            if c == 'l':
                LeftMoveBlock(bx, by, 100, 100)
            if c == 'r':
                RightMoveBlock(bx, by, 100, 100)
            if c == 's':
                Skeleton(bx, by, 27, 48, 80)
            if c == 'h':
                ExtraHealth(bx, by, healthImage.get_width(), healthImage.get_height())
            if c == 'k':
                Key(bx, by, keyImage.get_width(), keyImage.get_height())
            if c == 'g':
                Gate(bx, by, 100, 100)
            if c == 'K':
                Keeper(bx, by, 27, 48, 150)
            if c == 'b':
                BossGate(bx, by, 100, 100)
            if c == 'S':
                Sword(bx, by, swordImage.get_width(), swordImage.get_height())
            if c == 'p':
                Spike(bx, by, 100, 100)
            if c == 'B':
                Boss(bx, by, 27, 50, 200)
            
            bx += 100#after each item add 100 to x value
        by += 100#after every list inside the 2D List add 100 to y value
        bx = 0#set x value to 0

drawMap(levelsList[index], index)#draw map

player = Player(250, 250, 30, 50, 100, 100)#create player

running=True#set running to true

while running:#game loop
    for e in event.get():
        display.set_caption("RISE OF CHAMPIONS // FPS = {0:.0f}".format(clock.get_fps()))#create caption for game
        if e.type == QUIT:#if quit
            running=False#set running to false
        if e.type == MOUSEBUTTONDOWN: #mous button is down
            release = False #release is set to false
            if musicVolumeRect.collidepoint(mx,my): #if mouse is on the music slider rect
                sliding = True #set sliding to true
            if effectVolumeRect.collidepoint(mx,my): #if mouse is on the effect slider rect
                sliding = True #set sliding to true
        if e.type == MOUSEBUTTONUP: #if mouse button is up
            release = True #released is set to true
            sliding = False #slidind is set to false
        if e.type == KEYDOWN: #if a key is pressed
            if e.key==K_ESCAPE and mode == 'game': #if the key pressed is espace and the game is playing
                mode = 'pause' #set the mode to pause
            if e.key==K_RETURN and mode == 'pause': #if the key pressed is enter and the game is paused
                pauseTimes = 0 #set the pause variable to 0
                musicChannel.unpause() #unpause the music
                effectChannel.unpause() #unpause the effects
                bossChannel.unpause() #unpause the boss music
                mode = 'game'
        if e.type in [KEYDOWN, KEYUP]: #for each key
            if e.key in [K_w, K_a, K_s, K_d]: #if w, a, s, or d is pressed
                frame = 0 #set thr frame count to zero
            if e.type == KEYDOWN and e.key == K_SPACE and not attacking and player.stamina >= 5:#if trying to attack and player has more stamina than 5
                player.stamina -= 5#subtract 5 from player stamina
                attacking = True#attacking = True
            if e.key == K_LSHIFT and player.stamina > 0 or e.key == K_RSHIFT and player.stamina > 0:#if pressing sprint and stamina > 0
                player.sprinting = True#player.sprinting = True
        if e.type == KEYUP: #if the key is released
            attack = False #set attack to false
            player.sprinting = False #set sprinting to false

    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    keys = key.get_pressed()
    
    if mode == 'menu': #if mode is menu
        mode = menu() #call the menu function
    elif mode == 'playNow': #if mode is playNow
        mode = playNow() #call the playNow function
    elif mode == 'instructions': #if mode is instrcutions
        mode = instructions() #call the instructions function
    elif mode == 'options': #if mode is options
        mode = options() #call the options function
    elif mode == 'credits': #if mode is credits
        mode = credits() #call the credits function
    elif mode == 'game': #if mode is game
        if not musicChannel.get_busy(): #if music is not already playing
            musicChannel.play(gameOneMusic) #play the game music
        if 0 <= index < 3: #if index is 0, 1 or 2
            background = grassBackground #background is grass
        elif 3 <= index < 6: #if index is 3, 4 or 5
            background = dirtBackground #background is dirt
        elif 6<= index < 9: #if index is 6, 7 or 8
            background = sandBackground #background is sand
        elif index == 9: #if index is 9
            background = darkBackground #background is dark
        else:
            background = bossBackground  #background is boss
        screen.blit(background,(0,0)) #blit the background
        ########################################
        #boss music
        if index == -1: #if the user is on the boss level
            musicChannel.fadeout(2000) #fade the music out
            if not effectChannel.get_busy(): #once the portal sound finished
                if not bossChannel.get_busy(): #if there is not boss music already playing
                    bossChannel.play(bossMusic) #play the boss music
        ########################################
        #Draw Map
        for block in levelsblocksList[index]:#for all blocks
            block.update()#update block
        
        for rightmoveblock in rightmoveList[index]:#for all rightmoveblocks
            rightmoveblock.update()#update rightmoveblocks

        for leftmoveblock in leftmoveList[index]:#for all leftmoveblocks
            leftmoveblock.update()#update leftmoveblocks
        ########################################
        #Hitboxes
        hitRect1 = HitRect(player.rect.x - 60, player.rect.y, 75, 50) #defining hit boxes
        hitRect2 = HitRect(player.rect.x - 10, player.rect.y - 30, 50, 70)
        hitRect3 = HitRect(player.rect.x - 10, player.rect.y + 30, 50, 60)
        hitRect4 = HitRect(player.rect.x + 20, player.rect.y, 75, 50)
        #################################################  
        #health bar
        hpRect=[5, 15, int(player.hp*3), 20]#create rect for player health
        hpborderRect=[4, 14, 302, 22]#create border rect for player health
        hpText=comicFont.render("Health: %i" %(player.hp),True,(0, 0, 0))#create text for health
        draw.rect(screen, (255, 255, 255), hpborderRect)#draw border rect
        draw.rect(screen, (255, 0, 0), hpRect)#draw healthbar
        screen.blit(hpText, (115, 15))#blit health text
        #################################################
        #stamina bar
        staminaRect = [5, 39, int(player.stamina*3), 20]#create rect for player stamina
        staminaborderRect = [4, 38, 302, 22]#create border rect for stamina
        staminaText = comicFont.render("Stamina: %i" %(player.stamina), True, (0, 0, 0))#create text for stamina
        draw.rect(screen, (255, 255, 255), staminaborderRect)#draw border rect
        draw.rect(screen, (0, 255, 0), staminaRect)#draw staminabar
        screen.blit(staminaText, (110, 39))#blit stamina text
        #################################################
        #boss text
        bossText = largeFont.render("FINAL LEVEL UNLOCKED!", True, (0, 0, 0))#create text for after player collects all the keys
        #################################################
        #sword counter
        if swordlevel == 1: #if the sword level is 1
            screen.blit(swordImage, (600, 10)) #blit one sword on the screen
        elif swordlevel == 2: #if the sword level is 2
            screen.blit(swordImage, (600, 10)) #blit 2 swords on the screen
            screen.blit(swordImage, (640, 10))
        #################################################
        #key counter
        if keyCount == 1: #if the key counter is 1
            screen.blit(keyImage, (320, 15)) #blit 1 key
        elif keyCount == 2: #if the key counter is 1
            screen.blit(keyImage, (320, 15)) #blit 2 keys
            screen.blit(keyImage, (420, 15))
        elif keyCount >= 3: #if the key counter is 1
            screen.blit(keyImage, (320, 15)) #blit 2 keys
            screen.blit(keyImage, (420, 15))
            screen.blit(keyImage, (520, 15))
            if 0 <= index < 3: #if index is 0, 1 or 2
                bossText = largeFont.render("FINAL LEVEL UNLOCKED!", True, (255, 255, 255)) #create the font either white or black
            elif 3 <= index < 6: #if index is 3, 4 or 5
                bossText = largeFont.render("FINAL LEVEL UNLOCKED!", True, (255, 255, 255))
            elif 6<= index < 9: #if index is 6, 7 or 8
                bossText = largeFont.render("FINAL LEVEL UNLOCKED!", True, (0, 0, 0))
            elif index == 9: #if index is 9
                bossText = largeFont.render("FINAL LEVEL UNLOCKED!", True, (255, 255, 255))
            else:
                bossText = largeFont.render("FINAL LEVEL UNLOCKED!", True, (255, 255, 255))
            if index != -1: #as long as the user us not on the boss level
                screen.blit(bossText, (690, 10)) #blit the boss text
                
        #################################################
        for extrahealth in extrahealthList[index]:#for all healthboosts
            extrahealth.update()#update all healthbosts
            if extrahealth.rect.colliderect(player.rect):#if player rect collides with 
                if player.hp + 50 > 100:#if player + health boost is greater than max health (100)
                    player.hp = 100#set player health to 100(max health)
                else:#if not greater than 100
                    player.hp += 50#add 50 to player health
                extrahealth.use()#call use method from class
                if not effectChannel.get_busy():
                    effectChannel.play(healthSound)#sound effect for health
                    
        ##################################################
        for gate in gatesList[index]:#for all gates
            gate.update()#update gates
            if enemiesList[index] == []:#if player has killed all enemies
                effectChannel.play(doorSound)#call door sound effect
                gatesList[index] = []#remove gates in level

        for bossgate in bossgateList[index]:#for all bossgates
            bossgate.update()#update bossgate
            if keyCount == 3:#if player collected all keys
                bossgateList[index] = []#remove bossgate

        for sword in swordList[index]:#for all swords
            sword.update()#update object
            if sword.rect.colliderect(player.rect):#if player rect collides with sword rect
                sword.collide()#call collide method from sword class
                effectChannel.play(swordPickupSound)#sound effect for sword
                swordlevel += 1#increase sword upgrade level

        for Keys in keysList[index]:#for all keys
            Keys.update()#update keys
            if Keys.rect.colliderect(player.rect):#if key rect collides with player rect
                Keys.collide()#call collide method from key class
                effectChannel.play(keySound)#key sound effect
                keyCount += 1#increase keyCount

        for spike in spikeList[index]:#for all spikes
            spike.update()#update spikes
            if spike.rect.colliderect(player.rect):#if player collides with spike
                damage = 0.35#set damage to 0.35
                player.take_damage()#call take_damage method from player class

        player.move()#move player
        player.update()#update player
        ########################################
        #PLAYER ANIMATION
        if hero=='man': #if the user chose a man
            currentDict = manFrameDict #set the dictionairy the man standing
        else:
            currentDict = girlFrameDict #set the dictionairy the girl standing

        if attacking: #if the user is attacking
            if not effectChannel.get_busy(): #if the effect channel is not playing anything
                effectChannel.play(swordSwooshSound) #play the sword swing sound
            if hero=='man':
                currentDict = manAttackFrameDict #set the dictionairy to the man attacking
            else:
                currentDict = girlAttackFrameDict #set the dictionairy to the girl attacking
        
        if not attacking: #if the user is not attacking
            test_state = handleInput(keys) #make the test_state the same as the key pressed

            if test_state is not None: #if there was input
                state = test_state #make the state the same as the test_state which was set in a function
                if hero=='man':
                    currentDict = manWalkFrameDict #set the dictionairy to the man walking
                else:
                    currentDict = girlWalkFrameDict #set the dictionairy to the man walking
        
        animate(currentDict, keys) #animate the character based on key pressed and dictionairy    
        ########################################
        #ENEMY ANIMATION AND ATTACKING
        for orc in orcList[index]:#for all orcs
            orc.move()#move orc
            orc.update()#update orc
            orc.healthbar()#create orc healthbar
            orc.animate()#animate orc
            if orc.rect.colliderect(player.rect):#if player collides with orc rect
                damage = 0.4#set damage to 0.4
                player.take_damage()#call take_damage method for player
            if attacking == True:#if player attacking variable = True
                if orc.rect.colliderect(hitRect1) and state == 'left':#if player attacking left and orc touching left attack hitbox
                    orc.take_damage()#orc takes damage
                if orc.rect.colliderect(hitRect2) and state == 'up':#if player attacking up and orc touching up attack hitbox
                    orc.take_damage()#orc takes damage
                if orc.rect.colliderect(hitRect3) and state == 'down':#if player attacking down and orc touching down attack hitbox
                    orc.take_damage()#orc takes damage
                if orc.rect.colliderect(hitRect4) and state == 'right':#if player attacking right and orc touching right attack hitbox
                    orc.take_damage()#orc takes damage

        for skeleton in skeletonList[index]:#for all skeletons
            skeleton.move()#move skeleton
            skeleton.update()#update skeleton
            skeleton.healthbar()#create skeleton healthbar
            skeleton.animate()#animate skeleton
            if skeleton.rect.colliderect(player.rect):#if player collides with skeleton rect
                damage = 0.2#set damage to 0.2
                player.take_damage()#call take_damage 
            if attacking == True:#if player attacking variable = True
                if skeleton.rect.colliderect(hitRect1) and state == 'left':#if player attacking left and skeleton touching left attack hitbox
                    skeleton.take_damage()#skeleton takes damage
                if skeleton.rect.colliderect(hitRect2) and state == 'up':#if player attacking up and skeleton touching up attack hitbox
                    skeleton.take_damage()#skeleton takes damage
                if skeleton.rect.colliderect(hitRect3) and state == 'down':#if player attacking down and skeleton touching down attack hitbox
                    skeleton.take_damage()#skeleton takes damage
                if skeleton.rect.colliderect(hitRect4) and state == 'right':#if player attacking right and skeleton touching right attack hitbox
                    skeleton.take_damage()#skeleton takes damage
                    
        for keeper in keeperList[index]:#for all keepers
            keeper.move()#move keeper
            keeper.update()#update keeper
            keeper.healthbar()#create keeper healthbar
            keeper.animate()#animate keeper
            if keeper.rect.colliderect(player.rect):#if keeper collides with player rect
                damage = 0.8#set damage to 0.8
                player.take_damage()#make player take damage
            if attacking == True:#if attacking is True 
                if keeper.rect.colliderect(hitRect1) and state == 'left':#if player attacking left and keeper touching left attack hitbox
                    keeper.take_damage()#keeper takes damage
                if keeper.rect.colliderect(hitRect2) and state == 'up':#if player attacking up and keeper touching up attack hitbox
                    keeper.take_damage()#keeper takes damage
                if keeper.rect.colliderect(hitRect3) and state == 'down':#if player attacking down and keeper touching down attack hitbox
                    keeper.take_damage()#keeper takes damage
                if keeper.rect.colliderect(hitRect4) and state == 'right':#if player attacking right and keeper touching right attack hitbox
                    keeper.take_damage()#keeper takes damage
                    
        for boss in bossList[index]:#for boss
            boss.move()#move boss
            boss.update()#update boss
            boss.healthbar()#create boss healthbar
            boss.animate()#animate boss
            if boss.rect.colliderect(player.rect):#if boss collides with player
                damage = 1.5#damage = 1.5
                player.take_damage()#player takes damage
            if attacking == True:#if attacking is True
                if boss.rect.colliderect(hitRect1) and state == 'left':#if player attacking left and boss touching left attack hitbox
                    boss.take_damage()#boss takes damage
                if boss.rect.colliderect(hitRect2) and state == 'up':#if player attacking up and boss touching up attack hitbox
                    boss.take_damage()#boss takes damage
                if boss.rect.colliderect(hitRect3) and state == 'down':#if player attacking down and boss touching down attack hitbox
                    boss.take_damage()#boss takes damage
                if boss.rect.colliderect(hitRect4) and state == 'right':#if player attacking right and boss touching right attack hitbox
                    boss.take_damage()#boss takes damage
            if boss.hp <= 0:#if the boss health dies
                mode = 'gameComplete' #switch to the game complete screen
        #################################################
        #Torches
        if index == 0:#if at first level
            #blit all torch images
            screen.blit(torchImage, (80, 400))
            screen.blit(torchImage, (80, 600))
            screen.blit(torchImage, (115, 400))
            screen.blit(torchImage, (115, 600))
                
        display.update()
        ########################################
        #Change levels
        if player.rect.colliderect(rightmoveblock.rect):#if player collides with rightmoveblock
            effectChannel.play(portalSound)#play portal sound effect
            spikeList[index] = []#empty spikeList[index]
            extrahealthList[index] = []#empty extrahealthList[index]
            index += 1#add 1 to index
            drawMap(levelsList[index], index)#call draw map function for new 2D List
            player.rect.x -= 850#subtract 850 from player rect x value
            display.flip()

        if player.rect.colliderect(leftmoveblock.rect):#if player collides with leftmoveblock
            effectChannel.play(portalSound)#play portal sound effect
            spikeList[index] = []#empty spikeList[index]
            extrahealthList[index] = []#empty extrahealthList[index]
            index -= 1#subtract 1 from index
            drawMap(levelsList[index], index)#call draw map function for new 2D List
            player.rect.x += 850#add 850 to player rect x value
            display.flip()
        #################################################
    elif mode == 'pause': #if mode is pause
        mode = pause() #call the pause function
    elif mode == 'game over': #if mode is game over
        mode = gameOver() #call the gameOver function
    elif mode == 'gameComplete': #if mode is gameComplete
        mode = gameComplete() #call the gameComplete function
    elif mode == 'quit': #if mode is quit
        break #break the game loop
        quit() #quit the game
        
    display.flip() #blit everything on the screen
    clock.tick(60) #frame rate is 60
    release = False #release is set to false
display.flip() #blit everything on the screen
quit() #quit the game
