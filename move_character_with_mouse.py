import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

def character_move_to_mouse():
    global mouse_x, mouse_y, x, y, x1, x2, dir, frame

    if mouse_x == x and mouse_y == y:
        mouse_x, mouse_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
        mouse.clip_draw(0, 0, 50, 52, mouse_x, mouse_y)


    x1, y1 = x, y
    for i in range(0, 100 + 1, 1):
        t = i / 100
        x = (1 - t) * x1 + t * mouse_x
        y = (1 - t) * y1 + t * mouse_y

        # 이전 위치에 그려진 캐릭터를 지우기
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        mouse.clip_draw(0, 0, 50, 52, mouse_x, mouse_y)
        frame = (frame + 1) % 8
        # 캐릭터를 현재 위치에 그리기
        if mouse_x - x1 >= 0 :
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
            #character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, y, 200, 200)
        elif mouse_x - x1 < 0 :
            #character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, y, 100, 100)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        delay(0.01)
        update_canvas()

    #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mouse_x, mouse_y = random.randint(0, 1000), random.randint(0, 1000)
x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir=0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    mouse.clip_draw(0, 0, 50, 52, mouse_x, mouse_y)
    character_move_to_mouse()
    update_canvas()
    handle_events()


close_canvas()



