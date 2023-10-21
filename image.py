import pygame,sys

rocket= pygame.image.load("로켓_1.png")
rocket=pygame.transform.scale(rocket,(50,80))

sunder = pygame.image.load("폭탄_안터진.png")
sunder = pygame.transform.scale(sunder,(50,50))


coinimage =  pygame.image.load("동전_1.png")
coinimage = pygame.transform.scale(coinimage,(20,20))

staryellow = pygame.image.load("큰별(노랑)_2.png")
staryellow = pygame.transform.scale(staryellow,(30,30))


starblue = pygame.image.load("큰별(파랑)_2.png")
starblue = pygame.transform.scale(starblue,(30,30))


starred = pygame.image.load("큰별(빨강)_2.png")
starred = pygame.transform.scale(starred,(30,80))


soccerball = pygame.image.load("축구공.png")
soccerball = pygame.transform.scale(soccerball,(50,80))


laser = pygame.image.load("광선검_1.png")
laser= pygame.transform.scale(laser,(30,80))


rainstar = pygame.image.load("별똥별(3)_1 (1).png")
rainstar = pygame.transform.scale(rainstar,(30,60))

charactorbg = pygame.image.load("그라데이션_1.png")
charactorbg = pygame.transform.scale(charactorbg,(900,500))


bg = pygame.image.load("wallpapertip_space-wallpaper-tumblr_369616.jpg")
bg = pygame.transform.scale(bg,(900,500))


bgo = pygame.image.load("우주(1)_1.png")
bgo = pygame.transform.scale(bgo,(900,500))

bgt = pygame.image.load("우주(2)_1.png")
bgt = pygame.transform.scale(bgt,(900,500))

bgth = pygame.image.load("우주(3)_1.png")
bgth = pygame.transform.scale(bgth,(900,500))


bgstart = pygame.image.load("밤.png")
bgstart = pygame.transform.scale(bgstart,(900,500))



#ba = pygame.image.load("pngwing.com.png")
#ba = pygame.transform.scale(ba,(100,100))



st = pygame.image.load("둥근버튼(일시정지)_1.png")
st = pygame.transform.scale(st,(30,30))



satt = pygame.image.load("둥근버튼(앞_뒤)_1.png")
satt = pygame.transform.scale(satt,(30,30))


gamebutton = pygame.image.load("start-png-44893.png")
gamebutton = pygame.transform.scale(gamebutton,(100,60))

storebg = pygame.image.load("무대_1.png")
storebg = pygame.transform.scale(storebg,(900,500))

lock = pygame.image.load("검은자물쇠_닫힘.png")
lock = pygame.transform.scale(lock,(30,50))


charactorbutton = pygame.image.load("벽돌_1.png")
charactorbutton = pygame.transform.scale(charactorbutton,(30,50))


whites = pygame.image.load("별 헤는 밤_1 (1).png")
whites = pygame.transform.scale(whites,(900,500))





  

rect_coin = coinimage.get_rect()
rect_sunders = sunder.get_rect()
rect_buttonstop = st.get_rect()
rect_buttonstart = satt.get_rect()
rect_gamebutton = gamebutton.get_rect()
rect_fire = starred.get_rect()
rect_bluefire = starblue.get_rect()
rect_power = staryellow.get_rect()
rect_powert = staryellow.get_rect()
rect_rainstar = rainstar.get_rect()
rect_soccerball = soccerball.get_rect()
rect_charactorbutton = charactorbutton.get_rect()
