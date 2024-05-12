import pygame  
from pygame import mouse
from pygame import font
import sys
import random
import time
 
# Create a list of 16 options, that describe the wheel
options = [
    "x 0.75",
    "Coin Flip",
    "x 2.50 ",
    "x 0.50",
    "x 0.75",
    "x 0.50 ",
    "x 0.25",
    "x5 Rigira",
    "x 0.75 ",
    "Coin Flip",
    "x 2.5",
    "x 0.5",
    "x 0.75",
    "x 50 ",
    "x 0.25",
    "x5 Rigira"
]
 
 

user_text = ''


def coinFlip():
    gigfont = pygame.font.SysFont('Corbel',208)
    nota = gigfont.render('DECIDING...' , True , (255,255,255))
    nota2 = gigfont.render('0' , True , (0,0,0))
    nota3 = gigfont.render('X2' , True , (0,0,0))
    global punt_calc
    global punt
    global sentinel
    global sentinella2
    sentinella2=False # per non far continuamente riaprire coinFlip() ma una volta sola
    x_win=110
    y_win=110
    x_lose=110
    y_lose=110
    round=0
    #num=random.randint(0,1)
    num=0
    done=True
    start=pygame.time.get_ticks()
    diff=0
    while done:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, black, (0,0,1600, 800))
        vittoria=pygame.Rect(0,0,x_win,y_win)
        sconfitta=pygame.Rect(0,0,x_lose,y_lose)
        vittoria.center=(1600/2-150, 800/2-150)
        sconfitta.center=(1600/2+150, 800/2+150)
        pygame.draw.rect(screen, green, vittoria,border_radius=50)
        pygame.draw.rect(screen, yellow, sconfitta,border_radius=50)
        if round >=1000:
            if num==0:
                sentinel=True
                if x_win<500 and y_win<500:
                    x_win+=0.2
                    y_win+=0.2
                if x_lose >0 and y_lose>0:
                    x_lose-=0.2
                    y_lose-=0.2           
            elif num==1:
                sentinel=False
                if x_win >0 and y_win>0:
                    x_win-=0.2
                    y_win-=0.2
                if x_lose <500 and y_lose <500:
                    x_lose+=0.2
                    y_lose+=0.2
            if x_lose >=480 and y_lose>=480:
                diff=pygame.time.get_ticks()-start
                screen.blit(nota2,(1600/2+50, 800/2+70 ))

            if x_win >=480 and y_win >=480:
                diff=pygame.time.get_ticks()-start
                screen.blit(nota3,(1600/2-200, 800/2-230))

            if diff>6000:
                done=False
                
            

        if round<1000:
            screen.blit(nota, (0,0))
        pygame.display.update()
        round+=1
    return sentinel
    


        
        

 
 
 
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
 
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive
 
#var puntata
punt=1
 
 
#var usata per i calcoli
 
punt_calc=0
 
#rigira
rigira=False
 
 
#definisco un contatore
cont=0
 
 
# initializing the constructor
pygame.init()
 
# screen resolution
res = (1600,800)
 
# opens up a window
screen = pygame.display.set_mode(res)
 
# white color
color = (255,255,255)
 
#se gira è cliccato
sentinella=False
 
# yellow color
yellow=(223,202,0)
 
# textbox color
textbox_color = yellow
 
 
green=(0, 255,0)

black=(0,0,0)
 
 
#light yellow
light_yellow=(255,245,20)
 
#pink color
 
pink=( 213, 115, 131)
 
#red, green, blue
 
red=(255,0,0)
 
light_purple=(213,18,255)
 
# light shade of the button
color_light = (200,0,0)
 
white=(255,255,255)
#red, green, blue
# dark shade of the button
color_dark = (150,0,0)
 
# stores the width of the
# screen into a variable
width = screen.get_width()
 
# stores the height of the
# screen into a variable
height = screen.get_height()
 
# defining a font
smallfont = pygame.font.SysFont('Corbel',68)
bigfont = pygame.font.SysFont('BOLD',100)
goodfont=pygame.font.SysFont("Corbel",30)
 
text = smallfont.render('GIRA!' , True , color)
scritta=smallfont.render("BIENVENIDO A LA",True,yellow)
scritta4=smallfont.render("RUEDA QUE",True,yellow)
scritta5=bigfont.render("GIRA!",True,yellow)
scritta2=smallfont.render("Inserisci il budget:",True,yellow)
scritta3=smallfont.render("€",True,yellow)
square = pygame.image.load('crazyTime.png')
astolfo=pygame.image.load("astolfo2.jpg")
astolfo3=pygame.image.load("astolfo3.jpg")
freccia=pygame.image.load("freccia.png")
 
 
# Set the size for the image
DEFAULT_RUOTA_SIZE = (500, 500)
DEFAULT_FRECCIA_SIZE=(100,100)
 
# Scale the image to your needed size
square = pygame.transform.scale(square, DEFAULT_RUOTA_SIZE)
freccia= pygame.transform.scale(freccia, DEFAULT_FRECCIA_SIZE)
astolfo3=pygame.transform.scale(astolfo3, (width,height))
angolo=0
 
 # create rectangle
input_rect= pygame.Rect(0, 500, 450,80)
 
#sentinella della textbox
active=False
 
verifica = True
#Schermata di set del budget
 
while verifica==True:
    #quando il budget viene eseguito, settare verifica a false
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        screen.blit(astolfo3, (0 ,0))
        screen.blit(scritta,(0,0))
        screen.blit(scritta4,(0,65))
        screen.blit(scritta5,(0,130))
 
        screen.blit(scritta2,(0,320))
        pygame.draw.rect(screen,yellow,[0, 500, 450,80], border_radius=40)
        screen.blit(scritta3,(0,580))
 
        #Textbox
       
        if ev.type == pygame.KEYDOWN:

            if ev.key==pygame.K_RETURN:
                verifica=False
 
                # Check for backspace
            if ev.key == pygame.K_BACKSPACE:
 
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
 
             # Unicode standard is used for string
                # formation
            else:
                if ev.key >= pygame.K_0 and ev.key <= pygame.K_9:    #funzione per ammettere solo numeri nel budget
                    user_text += ev.unicode
                    textbox_color=yellow
                else:
                    print("only numbers allowed!")
 
            budget=user_text

			
       
 
         
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, textbox_color, input_rect, border_radius=40)
 
        text_surface = smallfont.render(user_text, True, (255, 255, 255))
     
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
     
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
     
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()
 
pygame.display.update()
 
 
 
 
#nel momento in cui il budget viene fatta, verifica viene settato a false e si entra nel While della ruota
   
 
 
tick=pygame.time.get_ticks()
while True:
    for ev in pygame.event.get():
         
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
       
           
        #checks if a mous is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mous=pygame.mouse.get_pos()
            #if the button is clicked
            if width/2+100 <= mous[0] <= width/2+100+180 and height/2+100 <= mous[1] <= height/2+100+80:
                angolo=0 #setta l'immagine nuovamente a zero
                verifica=True
               
                budget_double=budget_double-punt
                if rigira==True:
                    budget_double=budget_double+punt
                    rigira=False
 
                budget=str(budget_double)
                sentinella=True
                sentinella2=True
                temp=random.randint(500,1300)
 
 
                #while della rotazione della ruota
                while cont<temp and verifica==True:   #per vedere se il buttone funziona sempre mettere che ogni volta che si clicca il bottone succede qualcosa
 
                    #tasto quit nel ciclo
                    pygame.event.get()
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        mous = pygame.mouse.get_pos()  #mi da su mouse[0] la width e mouse[1] la height
                        if width/16 <= mous[0] <= width/16+ 160 and height /16  <= mous[1] <= height/6 + 160:
                                tupla=mouse.get_pressed()
                                if tupla==(True, False, False):
                                    pygame.quit()
                                    sys.exit()
                    if width/16 <= mous[0] <= width/16+160 and height/16 <= mous[1] <= height/16+160: #coordinate del bottone + la lunghezza/altezza del bottone
                        pygame.draw.rect(screen, white, [width/16, height/16 , 178, 178],border_radius=100)
                        pygame.draw.rect(screen, light_yellow, [width/16, height/16 , 160, 160],border_radius=100)
 
                    else:
                        pygame.draw.rect(screen, white, [width/16, height/16 , 170, 170],border_radius=100)
                        pygame.draw.rect(screen, yellow, [width/16, height/16 , 160, 160],border_radius=100)    
 
                    screen.blit(testo2 , (width/16+15 ,height/16+44))          
 
 
                   
                   
                    cont+=1
                    if cont>temp/1.12:
                        angolo+=0.4      
                    elif cont>temp/1.15:
                        angolo+=1      
                    elif cont>temp/1.19:
                        angolo+=3      
                    elif cont>temp/1.2:
                        angolo+=4      
                    elif cont>temp/1.225:
                        angolo+=5      
                    elif cont>temp/1.250:
                        angolo+=8      
                    elif cont>temp/1.3:
                        angolo+=10      
                    elif cont>temp/1.35:
                        angolo+=12      
                    elif cont>temp/1.475:
                        angolo+=15      
                    elif cont>temp/1.6:
                        angolo+=20      
                    elif cont>temp/2:
                        angolo+=25      
                    else:
                        angolo+=30        #velocità normale
 
 
                    square2 = pygame.transform.rotate(square, angolo)  #crea l'oggetto immagine ruotata
                    rettangolo = square2.get_rect() #prende il perimetro della rotazione dell'immagine
                    rettangolo.center = (300+square.get_width()/2, 200+square.get_height()/2) #trova il centro dell'immagine
                    screen.blit(square2, rettangolo)
                    screen.blit(freccia, (502,140))
                    pygame.display.update()
                    pygame.time.delay(0)
                    if angolo>359: angolo=0 #quando angolo arriva a 360 resettaù
 
 
                    #diminuisce la possiblitò di x50
                    if cont>temp-20 and 292.5 < angolo < 315:
                        temporaneo=random.randint(1,2)
                        if temporaneo==1:
                            temp=temp+22.5
 
                       
                     #zona scrittura budget
                    pygame.draw.rect(screen, white,[width/2, height-(height/8),710,87],border_radius=40)
                    pygame.draw.rect(screen, light_purple,[width/2, height-(height/8),700,80],border_radius=40)
                    #scrivere la var budget
 
                    budget1=smallfont.render(budget+"€",True,white)
                    screen.blit(budget1 , (width/2+20 ,height-height/8+8))
 
                    #fine zona scrittura budget
         
                       
         
 
    # fills the screen with a color
    screen.fill((150,50,160))
    #red, green, blue
     
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mous = pygame.mouse.get_pos()  #mi da su mouse[0] la width e mouse[1] la height
       
    # if mouse is hovered on a button it
    # changes to lighter shade
 
 
 #tasto quit. in modo che funzioni anche fuori dal ciclo
    if ev.type == pygame.MOUSEBUTTONDOWN:
        mous = pygame.mouse.get_pos()  #mi da su mouse[0] la width e mouse[1] la height
        if width/16 <= mous[0] <= width/16+ 160 and height /16  <= mous[1] <= height/6 + 160:
            tupla=mouse.get_pressed()
            if tupla==(True, False, False):
                pygame.quit()
                sys.exit()
 
 
    screen.blit(astolfo, (-50,-100))
    #bottone GIRA!
    if width/2+100 <= mous[0] <= width/2+100+180 and height/2+100 <= mous[1] <= height/2+100+80: #coordinate del bottone + la lunghezza/altezza del bottone
        pygame.draw.rect(screen,white,[width/2+105,height/2+105,188,88], border_radius=40)
        pygame.draw.rect(screen,color_light,[width/2+100,height/2+100,180,80], border_radius=40)
 
    else:
        pygame.draw.rect(screen,white,[width/2+100,height/2+100,185,85], border_radius=40)
        pygame.draw.rect(screen,color_dark,[width/2+100,height/2+100,180,80], border_radius=40)  # [ coords, coords ,larghezza del rect, altezza del rect ]
     
    # superimposing the text onto our button
    square2 = pygame.transform.rotate(square, angolo)  #crea l'oggetto immagine ruotata
    rettangolo = square2.get_rect() #prende il perimetro della rotazione dell'immagine
    rettangolo.center = (300+square.get_width()/2, 200+square.get_height()/2) #trova il centro dell'immagine
    cont=0
    screen.blit(text , (width/2+113 ,height/2+110)) #scrivo GIRA!
    screen.blit(square2, rettangolo)
    screen.blit(freccia, (500,140))
 
    #zona puntata  
 
 
    puntata=pygame.Rect(width/2+25,height/2-255, 250,75)
    pygame.draw.rect(screen,color,puntata, border_radius=20)
    pygame.draw.rect(screen,red,puntata,5,border_radius=20)
 
    aggiunta=pygame.Rect(width/2, height/2-105,100,50)
    aggiunta2=pygame.Rect(width/2+200, height/2-105,100,50)
    aggiunta3=pygame.Rect(width/2, height/2-105,105,55)
    aggiunta4=pygame.Rect(width/2+200, height/2-105,105,55)
 
    pygame.draw.rect(screen , color ,aggiunta3,border_radius=50)
    pygame.draw.rect(screen , color ,aggiunta4,border_radius=50)
    pygame.draw.rect(screen , green ,aggiunta,border_radius=50)
    pygame.draw.rect(screen , green ,aggiunta2,border_radius=50)
 
 
 
    #testi sui bottoni puntata
    budget_double=float(budget)
    string_punt=str(punt)+"€"
    aaaa = goodfont.render('RESET' , True , color)
 
    bbbb = goodfont.render('+50' , True , color)
 
    cccc= smallfont.render(string_punt,True, red)
 
 
    screen.blit(aaaa ,(width/2+10, height/2-95) ) #scrivo RESET
 
    screen.blit(bbbb ,(width/2+225, height/2-95) ) #scrivo +50
 
    screen.blit(cccc ,(width/2+30,height/2-255) ) #scrivo +50
 
    if rigira==False:
        if aggiunta.collidepoint(mous)and ev.type==pygame.MOUSEBUTTONDOWN:
            punt=1
   
   
        diff=pygame.time.get_ticks()
   
        if diff-250> tick:
            ver=True
        if aggiunta2.collidepoint(mous)and ev.type==pygame.MOUSEBUTTONDOWN and ver==True:
                punt=punt+50
                ver=False
                tick=pygame.time.get_ticks()
       
 
 
 
 
 
 
 
 
 
        #check di che angolo è uscito
    pygame.draw.rect(screen,white,[1175,200,308,108], border_radius=40)
    if angolo < 22.5 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[0]
        punt_calc=punt*0.75
    elif 22.5 < angolo < 45 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[1]
        if sentinella2:
            sentinel=coinFlip()
            print(sentinel)
            if sentinel:
                punt_calc=punt*2
    elif 45 < angolo < 67.5 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[2]
        punt_calc=punt*2.5
    elif 67.5 < angolo < 90 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[3]
        punt_calc=punt*0.5
    elif 90 < angolo < 112.5:
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[4]
        punt_calc=punt*0.75
    elif 112.5 < angolo < 135 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[5]
        punt_calc=punt*0.5
    elif 135 < angolo < 157.5 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[6]
        punt_calc=punt*0.25
    elif 157.5 < angolo < 180 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[7]
        punt_calc=punt*5
        rigira=True
    elif 180 < angolo < 202.5 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[8]
        punt_calc=punt*0.75
    elif 202.5 < angolo < 225 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[9]
        if sentinella2:
            sentinel=coinFlip()
            print(sentinel)
            if sentinel:
                punt_calc=punt*2
    elif 225 < angolo< 247.5:
        punt_calc=punt*2.5
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[10]
    elif 247.5 < angolo < 270 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[11]
        punt_calc=punt*0.5
    elif 270 < angolo < 292.5 :
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[12]
        punt_calc=punt*0.75
    elif 292.5 < angolo < 315:
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[13]
        punt_calc=punt*50
    elif 315 < angolo < 337.5 :
        punt_calc=punt*0.25
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[14]
    elif 337.5 < angolo < 360 :
        punt_calc=punt*5
        rigira=True
        pygame.draw.rect(screen,pink,[1175,200,300,100], border_radius=40)
        testo=options[15]
       
    testo1 = smallfont.render(testo , True , color)
    testo2= smallfont.render("Quit!", True, color)
    screen.blit(testo1 , (1200 ,215))

    if sentinella==True:
        budget_double+=punt_calc
        budget=str(budget_double)
        sentinella=False
 #zona scrittura budget
    pygame.draw.rect(screen, white,[width/2, height-(height/8),710,87],border_radius=40)
    pygame.draw.rect(screen, light_purple,[width/2, height-(height/8),700,80],border_radius=40)
    #scrivere la var budget
 
    budget1=smallfont.render(budget+"€",True,white)
    screen.blit(budget1 , (width/2+20 ,height-height/8+8))
 
    #fine zona scrittura budget
   
 
 #bottone quit, grafica fuori dal ciclo
    if width/16 <= mous[0] <= width/16+160 and height/16 <= mous[1] <= height/16+160: #coordinate del bottone + la lunghezza/altezza del bottone
        pygame.draw.rect(screen, white, [width/16, height/16 , 178, 178],border_radius=100)
        pygame.draw.rect(screen, light_yellow, [width/16, height/16 , 160, 160],border_radius=100)
 
    else:
        pygame.draw.rect(screen, white, [width/16, height/16 , 170, 170],border_radius=100)
        pygame.draw.rect(screen, yellow, [width/16, height/16 , 160, 160],border_radius=100)
          # [ coords, coords ,larghezza del rect, altezza del rect ]
 
    screen.blit(testo2 , (width/16+15 ,height/16+44))
 
    #funzione del risultato della ruota
     
    # updates the frames of the game
    pygame.display.update()
    pygame.time.delay(0)