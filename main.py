import pygame, asyncio
from urllib.request import *
pygame.init()
secret_word = ""
from random import *
import os

poe_poe = []
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
link = "https://randomword.com/"
'''
for e in range(150):
    four_zero_three = Request(link, headers={"User-Agent": user_agent})
    four_zero_three = urlopen(four_zero_three)
    web = four_zero_three.read()
    web = web.decode("utf-8")
    index = web.find("random_word") + len("random_word") + 2
    end_index = index
    while web[end_index] != "<":
            end_index += 1
    poe_poe.append(web[index: end_index])
print(poe_poe)
'''
#fff_name = "Bigass_list.txt"
#absolute_path = os.path.abspath(fff_name)
async def main():
    forever = True
    kasper = True
    start = False
    always = True
    health = 6
    lboy = open("Bigass_list.txt")
    lboy = lboy.read()
    lboy = lboy.split(" ")
    shuffle(lboy)
    lboy.append("tryhard")
    width = 1000
    height = 1000
    screen = pygame.display.set_mode((width, height))
    a = randint(50, 255)
    b = randint(50, 255)
    c = randint(50, 255)
    heart = pygame.image.load("Poe_Heart.png")
    turn_counter = 0
    fondue = pygame.font.SysFont("bodoni",50,italic = False, bold = True)
    score_fondue = pygame.font.SysFont("bodoni",50,italic = False, bold = True)
    text = fondue.render("", True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (450, 500)
    text_2 = fondue.render("Press any key to start", True, (0,0,0))
    text_rect_2 = text_2.get_rect()
    text_rect_2.center = (500, 100)
    high_score = fondue.render("SCORE: " + str(turn_counter), True, (0,0,0))
    score_rect = high_score.get_rect()
    score_rect.center = (500, 100)
    lose_screen = pygame.image.load("lose_screen.png")
    lose_screen = pygame.transform.scale(lose_screen, (1000, 1800))
    one_piece = True
    store = []
    fonts = pygame.font.get_fonts()
    while forever:
        screen.fill((a, b, c))
        if kasper:
                screen.blit(text_2, text_rect_2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                forever = False
            if event.type == pygame.KEYDOWN:
                start = True
                kasper = False
        if start:
            if health > 0:
                screen.blit(heart, (0, 50))
            else:
                screen.blit(lose_screen, (0,0))
                high_score = score_fondue.render("SCORE: " + str(turn_counter - 1), True, (0,0,0))
                screen.blit(high_score, score_rect)
                always = False
            if health > 1:
                screen.blit(heart, (250, 50))
            if health > 2:
                screen.blit(heart, (500, 50))
            if health > 3:
                screen.blit(heart, (0, 500))
            if health > 4:
                screen.blit(heart, (250, 500))
            if health > 5:
                screen.blit(heart, (500, 500))
            if always:
                if one_piece:
                    something = randint(1, 2) 
                    if turn_counter == 0:
                        da_word = lboy[turn_counter]
                    else:
                        if something == 1 and store:
                            shuffle(store)
                            da_word = store[0]
                        if something == 2:
                            da_word = lboy[turn_counter]
                    if something == 2:
                        store.append(lboy[turn_counter])
                    fondue = pygame.font.SysFont(choice(fonts),50,italic = False, bold = True)
                    text = fondue.render(da_word, True, (0,0,0))
                    one_piece = False
                screen.blit(text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        forever = False
                    elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_o:
                                one_piece = True
                                if something == 2 or turn_counter == 0:
                                    health -= 1
                                turn_counter += 1
                            elif event.key == pygame.K_n:
                                one_piece = True
                                if something == 1 and turn_counter > 0:
                                    health -= 1
                                turn_counter += 1
        pygame.display.update()
        await asyncio.sleep(0)
asyncio.run(main())