# TODO: Make window resizeable
# TODO: Adjust lamps' size and position to window's size
import sys
from datetime import datetime
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

WINDOW_SIZE = (500, 500)
FILL_COLOR_ACTIVE_HOUR = (255, 0, 0)
FILL_COLOR_ACTIVE_MINUTE = (0, 255, 0)
FILL_COLOR_ACTIVE_SECOND = (0, 0, 255)
FILL_COLOR_INACTIVE = (45, 45, 45)
DIGITAL_TIME_COLOR = (150, 150, 150)
OUTLINE_COLOR = (0, 0, 0)
CLOCK_LAMP_SIZE = 20
CLOCK_LAMP_OUTLINE_THICKNESS = 3
CLOCK_START_POS = (50, 0)

display = pygame.display.set_mode(WINDOW_SIZE)

def convertinttobinlist(part, length=0):
    result = ""
    if part == 0:
        result = "0"

    while part > 0:
        result = str(part % 2) + result
        part = part // 2

    result = ("0"*length + result)[-length:]

    return [int(char) for char in result]


def convertimetobinary(time):
    binary_clock = []
    for i, section in enumerate(time.strftime("%H:%M:%S").split(":")):
        binary_clock_section = []
        for j, part in enumerate(section):
            # convert part to binary
            # append part to our list
            bin_part = convertinttobinlist(int(part), 5)
            binary_clock.append(bin_part)

    return binary_clock


def drawbinaryclock(display):
    # draw filled circle then draw a circle outline OVER of the same size
    now = datetime.now()
    now_in_binary = convertimetobinary(now)
    time_digit_list = now.strftime("%H%M%S")
    print(time_digit_list)

    font = pygame.font.SysFont(None, 48)


    for x in range(6):
        time_digit = font.render(time_digit_list[x], True, DIGITAL_TIME_COLOR)
        display.blit(time_digit, ((CLOCK_START_POS[0] + x * CLOCK_LAMP_SIZE * 3) - time_digit.get_width()/2, (CLOCK_START_POS[1] + 5 * CLOCK_LAMP_SIZE * 3) - time_digit.get_height()/2))

        if x < 2:
            fill_color = FILL_COLOR_ACTIVE_HOUR
        elif x < 4:
            fill_color = FILL_COLOR_ACTIVE_MINUTE
        else:
            fill_color = FILL_COLOR_ACTIVE_SECOND

        for y in range(4, 0, -1):
            if now_in_binary[x][y]:
                pygame.draw.circle(display, fill_color, (
                CLOCK_START_POS[0] + x * CLOCK_LAMP_SIZE * 3, CLOCK_START_POS[1] + y * CLOCK_LAMP_SIZE * 3),
                                   CLOCK_LAMP_SIZE)
            else:
                pygame.draw.circle(display, FILL_COLOR_INACTIVE, (
                CLOCK_START_POS[0] + x * CLOCK_LAMP_SIZE * 3, CLOCK_START_POS[1] + y * CLOCK_LAMP_SIZE * 3),
                                   CLOCK_LAMP_SIZE)

            pygame.draw.circle(display, OUTLINE_COLOR, (
            CLOCK_START_POS[0] + x * CLOCK_LAMP_SIZE * 3, CLOCK_START_POS[1] + y * CLOCK_LAMP_SIZE * 3),
                               CLOCK_LAMP_SIZE, CLOCK_LAMP_OUTLINE_THICKNESS)

            # break first hour after two "lamps"
            if x == 0 and y == 3:
                break

if __name__ == "__main__":
    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        display.fill((90, 90, 90))

        drawbinaryclock(display)

        pygame.display.flip()

        clock.tick(2)