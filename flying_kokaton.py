import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    bg_img1 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.transform.flip(kk_img, True, False)
    tmr = 0
    x = 0
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    v = 1
    while True:
        vx = 0
        vy = 0
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            vy =  -1
        if key_lst[pg.K_DOWN]:
            vy =  1
        if key_lst[pg.K_RIGHT]:
            vx = 2
        if key_lst[pg.K_LEFT]:
            vx = -1
        kk_rct.move_ip(((-v+vx),vy))
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img1, [(x+1600), 0])
        screen.blit(bg_img, [(x+3200), 0])
        screen.blit(bg_img1, [(x+4200), 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1  
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()