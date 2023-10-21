
import pygame,sys,random,time,pickle
import image

pygame.init()

DISPAYSURF=pygame.display.set_mode((900,500))
#display = pygame.display.set_mode((900,500))

rocket = image.rocket

sunder = image.sunder
staryellow = image.staryellow
starblue = image.starblue
starred = image.starred
soccerball = image.soccerball
laser = image.laser
bg = image.bg
bgo = image.bgo
bgt = image.bgt
bgth = image.bgth
bgstart = image.bgstart
st = image.st
satt = image.satt
gamebutton = image.gamebutton
rainstar = image.rainstar
coinimage = image.coinimage
storebg = image.storebg
charactorbg = image.charactorbg
lock = image.lock
whites = image.whites
charactorbutton = image.charactorbutton

rect_coin = image.rect_coin
rect_sunders = image.rect_sunders
rect_buttonstop = image.rect_buttonstop
rect_buttonstart = image.rect_buttonstart
rect_gamebutton = image.rect_gamebutton
rect_fire = image.rect_fire
rect_bluefire = image.rect_bluefire
rect_power = image.rect_power
rect_powert = image.rect_powert
rect_rainstar = image.rect_rainstar
rect_soccerball = image.rect_soccerball




rocketX= 450
rockety = 400


WHITE = (255,255,255)
sunderx = random.randrange(20,800)
sundery = 0

stary = 400
starx = rocketX


starpowery = 0
starpoweryt = 0

rect_stars = []



#충돌감지

store_text = pygame.font.SysFont(None,50)
store_textblue = pygame.font.SysFont(None,50)
 




font_score = pygame.font.SysFont(None,30)
font_gameover = pygame.font.SysFont(None,100)
font_youwin = pygame.font.SysFont(None,100)


 


text = store_text.render("500",True,(255,255,255))
textblue = store_text.render("700",True,(255,255,255)) 


a = 0

        

   



run = True 


score = 10

stt = []

c = 0
s =0


powergo = 0

star2 = starx + 10

level = 0

sp = 0

print('난이도를 정해주십시오 (1~3까지 있음)')

level =  int(input())
if level > 3:
  print('숫자가 너무 큽니다 다시 입력해 주세요')
  level =  int(input())


charactor = 0
charactorinput = 0

  


  
   
pluspower = 0
if level == 1:
  sp = 0.2

if level == 2:
  sp = 0.3
  pluspower = 1

if level == 3:
  sp = 0.4
  pluspower = 2 


stop = 0



bx_click = 0
mb_click = 0

starpowerx = rocketX
starpowerxt = rocketX



#박스에서 랜덤으로 나올 확률 변수 저장
bxpersant = 0
mbpersant = 0
coin = 0




charactor_list = []
with open ('g.p','rb') as file:
     power = pickle.load(file)
 
with open('f.p','rb') as file:
  charactor_list = pickle.load(file)
  print(charactor_list)



charactorpick = 0
charactorcheck = 0
charactorpick = int(input())
#print(charactor_list)

if charactorpick == 1 and 'bluestar' in charactor_list:  
   charactorcheck = 1


if charactorpick == 2 and 'redstar' in charactor_list:  
   charactorcheck = 2


if charactorpick == 3 and 'soccerball' in charactor_list:  
   charactorcheck = 3


if charactorpick == 4 and 'rainstar' in charactor_list:  
   charactorcheck = 4


if charactorpick == 5 and 'coin' in charactor_list:  
   charactorcheck = 5

   



sunderstop = 0

rect_buttonstop.topleft = (750,10)
def check(pos):
    global a
    global checkmust
    global fc 
    global bc


    if rect_buttonstop.collidepoint(pos)or checkmust == 1:
     
      DISPAYSURF.blit(storebg,(0,0))
      DISPAYSURF.blit(starred,(500,200))
      DISPAYSURF.blit(rainstar,(400,200)) 
      DISPAYSURF.blit(coinimage,(300,200)) 
      DISPAYSURF.blit(soccerball,(200,200)) 
      DISPAYSURF.blit(starblue,(100,200)) 
      DISPAYSURF.blit(satt,(780,10)) 
     # DISPAYSURF.blit(whites,(0,0)) 
      #fc = 1                                     
      #bc = 1
    
      #fireclick(pos)
      bluefireclick(pos)
      soccerballclick(pos)
      rainstarclick(pos)
      fireclick(pos)
      coinclick(pos)
      
      
    
     
      display()

rect_buttonstart.topleft = (780,10)
checkmust = 0

def start(pos):
  global cc
  global sunderstop
  global checkmust

  if rect_buttonstart.collidepoint(pos) :
    cc = 1
    sunderstop = 0
    checkmust = 0







#아이템 클릭
#아이템 리스트


#아이템 살떄 필요한 point

bluestarpoint = 700
redstarpoint = 500
soccerballpoint = 800
rainstarpoint = 700
coinpoint = 300


rect_fire.topleft = (500,200)
def fireclick(pos):#starred
    global charactor
    global checkmust
    global power
    checkmust = 1
    
    if rect_fire.collidepoint(pos):
      print('redstar')
      if power >= redstarpoint:
        charactor_list.append('redstar')
        power -= redstarpoint

        
rect_soccerball.topleft = (200,200) 

def soccerballclick(pos):
  global charactor
  global checkmust
  global power
  global cc
  checkmust = 1
  print('dddffffgggg')

  if rect_soccerball.collidepoint(pos):
    print('soccerball')
    if power >= soccerballpoint:
     
     charactor_list.append('soccerball')
     print("soccerball check")
     power -= soccerballpoint 
     cc = 1
     
        

    


rect_bluefire.topleft = (100,200)

def bluefireclick(pos):#starblue

  global charactor
  global power
  global checkmust
  global sunderstop
  global cc
  checkmust = 1
  print('wwwwwwwwwwwww')

  if rect_bluefire.collidepoint(pos):
      
      if power >= bluestarpoint:
        print('bluestar')
        charactor_list.append('bluestar')
        power-=bluestarpoint
        cc = 1
        

rect_rainstar.topleft = (400,200)
def rainstarclick(pos):

  global charactor
  global power
  global checkmust
  checkmust = 1

  if rect_rainstar.collidepoint(pos):
      print('rainstar')
      if power >= rainstarpoint:
        charactor_list.append('rainstar')
        power-=rainstarpoint


rect_coin.topleft = (300,200)

def coinclick(pos):

  global charactor
  global power
  global checkmust
  checkmust = 1

  if rect_coin.collidepoint(pos):
      print('coin')
      if power >= coinpoint:
        charactor_list.append('coin')
        
        
        power-=coinpoint

  










def display():

  global sunderstop 
  sunderstop = 1
  




test = 0

sunderstop = 0

rect_gamebutton.topleft = (400,400)

def startdisplay(pos):

   display()
   gamestartbutton(pos)
   global test
   global sunderstop 

   DISPAYSURF.blit(bgstart,(0,0)) 
   DISPAYSURF.blit(gamebutton,(400,400))  
   


click = 0,0
test2= 0
cc = 0
bc = 0   
def gamestartbutton(pos):
   global test
   global sunderstop
   global click
   global test2
   global cc
   global bc
   
   
   if rect_gamebutton.collidepoint(pos):
     test2 = 1
     print('start')
     sunderstop  = 0
     
     click = 0,0
     
     cc = 2
    
     test = 1
     


def starpower():
  global starpowerx
  global starpowerxt
  DISPAYSURF.blit(staryellow,(starpowerx,starpowery))
  DISPAYSURF.blit(staryellow,(starpowerxt,starpowery)) 
  starpowerx += 0.5
  starpowerxt -= 0.5
z = 0  


 
#아이템 클릭





   
    


sundergo = 0
starpowerstop = 0

fc = 0
bc = 0 
powerstarfinish = 0

randombackground = random.randint(1,3)
#print(randombackground)
inputone = 0




while run:#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
      
  
      pygame.display.flip()

      speed = 0
      power = 1000
      #print(charactor_list)


      

      
      rect_sunders.topleft = (sunderx,sundery)
     

      
      
      
  
      if randombackground == 1:
       DISPAYSURF.blit(bgo,(0,0)) 
      if randombackground == 2:
       DISPAYSURF.blit(bgt,(0,0)) 
      if randombackground == 3:
       DISPAYSURF.blit(bgth,(0,0)) 
      

      DISPAYSURF.blit(rocket,(rocketX,rockety)) 
      DISPAYSURF.blit(sunder,(sunderx,sundery)) 
      DISPAYSURF.blit(st,(750,10)) 
      DISPAYSURF.blit(satt,(780,10))
     
     

       
      if click:

      
      
        if bc == 1:
         bluefireclick(click)
         fireclick(click)
         soccerballclick(click)
         rainstarclick(click)
         coinclick(click)

        if test2 == 1:
         start(click)
        
        if test == 0:
         startdisplay(click)
      
        
        if cc == 2:
         check(click) 

       

      
      
       
    
     
      
      for event in pygame.event.get():

       
         
       with open ('g.p','wb') as file:
         
         pickle.dump(power,file)
       with open('f.p','wb') as file:
         pickle.dump(charactor_list,file)
         
        

       if event.type == pygame.QUIT:        
         run = False
         print(power)

       if event.type == pygame.MOUSEBUTTONDOWN:
          
          click = pygame.mouse.get_pos()

     
     


      #키보드 조종
       if event.type == pygame.KEYDOWN:


                   
             
            if event.key == pygame.K_ESCAPE:
              test = 0
         
              
             
            if event.key == pygame.K_LEFT:
       
               rocketX -= 50 
         
         
            if event.key == pygame.K_RIGHT:
             
                rocketX += 50 
               
             



            
            if event.key == pygame.K_SPACE:
               starx = rocketX+22
               stt.append([starx,stary])
               #stt.append([star2,stary])
               rect_stars.append(starblue.get_rect())



            if event.key == pygame.K_UP:
              print(power)
              if power >= 10:
               
                 c = 1





            
            if event.key == pygame.K_s:
              #if c == 1:
              if power >= 10:
                if level >= 2:
                  s = 1
                  starpowerstop = 0
                  power -= 10
              
          
            
      if len(stt):
        
        
      
        
        for str in stt:
            i = stt.index(str)
            print(charactorcheck)
            
         


                                                       
            str[1]-=0.5
           

            rect_stars[i].topleft = (str[0],str[1])
            

            if charactorcheck == 1:
              DISPAYSURF.blit(starblue,(str[0],str[1]))
              
            if charactorcheck == 2:
              DISPAYSURF.blit(starred,(str[0],str[1]))
              
            if charactorcheck == 3:
              DISPAYSURF.blit(soccerball,(str[0],str[1]))
              
            if charactorcheck == 4:
              DISPAYSURF.blit(rainstar,(str[0],str[1]))
              
            if charactorcheck == 5:
              DISPAYSURF.blit(coinimage,(str[0],str[1]))
              
              
              ##################################################################################################
              
            

            if rect_stars[i].colliderect(rect_sunders):
              stt.remove(str)
              rect_stars.remove(rect_stars[i])
              print('충돌')
              sundery=0
              sunderx = random.randrange(20,800)
              print(power)
              power += 2+pluspower
              
              


            if str[1] <= 0 :
             stt.remove(str)
             rect_stars.remove(rect_stars[i])
            
            
           
     
           
           


            



      if sunderstop  == 0:
       if sundery >= 500:
        sundery=0
        sunderx = random.randrange(20,800)
        power-=5
       
       else:
        sundery+=sp
       
      rect_power.topleft =(starpowerx,starpowery)
      rect_powert.topleft =(starpowerxt,starpoweryt)

      if rect_power.colliderect(rect_sunders):
        sunderx = random.randrange(20,800)
        sundery = 0

      
      if rect_powert.colliderect(rect_sunders):
        sunderx = random.randrange(20,800)
        sundery = 0

      #s = 1
      starpowery = rockety+50
      starpoweryt = rockety+50

      if s == 1:
 
        if starpowerstop == 0:
         starpower()
         print(starpowerx)
        
 
      if starpowerx >= 900:
          starpowerstop = 1
          s = 0
          starpowerx = rocketX
          starpowerxt = rocketX

      else:
          starpowerx -=1
          starpowerx += 1

          

        #power -= 10   
  
  


starx = rocketX + 22  
 
pygame.quit()
# 캐릭터 화면 못 넘어가게



