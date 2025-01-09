import os
import sys
import time
import random
import pygame
from pygame.locals import *

# Typing Speed Test class
class TypingSpeedTest:
    def __init__(self):
        print("Initializing game...")
        self.color_heading = (255, 213, 102)
        self.color_text = (255, 0, 0)
        self.color_results = (255, 70, 70)
        self.width = 750
        self.height = 500
        self.reset = True
        self.wpm = 0
        self.end = False
        self.active = False
        self.input_text = ''
        self.word = ''
        self.results = 'Time:0 Accuracy:0% WPM:0'
        self.start_time = 0
        self.overall_time = 0
        self.accuracy = '0%'
        self.high_score_file = "highscore.txt"
        self.high_score = self.load_high_score()

        pygame.init()
        try:
            self.image_open = pygame.image.load('assets/SpeedTestGame.jpg')
            self.image_open = pygame.transform.scale(self.image_open, (self.width, self.height))
        except pygame.error as e:
            print(f"Error loading SpeedTestGame.jpg: {e}")

        try:
            self.bg = pygame.image.load('assets/ppt.jpg')
            self.bg = pygame.transform.scale(self.bg, (750, 500))
        except pygame.error as e:
            print(f"Error loading ppt.jpg: {e}")

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Typing Speed Test')
        print("Initialization complete")

    def load_high_score(self):
        if os.path.exists(self.high_score_file):
            with open(self.high_score_file, "r") as file:
                return float(file.read())
        return 0.0

    def save_high_score(self, score):
        with open(self.high_score_file, "w") as file:
            file.write(str(score))

    def draw_text(self, screen, message, y_val, f_size, color):
        font = pygame.font.Font(None, f_size)
        text = font.render(message, 1, color)
        text_rect = text.get_rect(center=(self.width / 2, y_val))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_challenge(self):
        return random.choice(open('essay.txt').read().split('\n'))

    def results_show(self, screen):
        if not self.end:
            self.overall_time = time.time() - self.start_time
            count = sum(1 for i, c in enumerate(self.word) if i < len(self.input_text) and self.input_text[i] == c)
            self.accuracy = (count * 100) / len(self.word)
            self.wpm = (len(self.input_text) * 60) / (5 * self.overall_time)
            self.end = True

            self.results = f"Time: {round(self.overall_time)} secs   Accuracy: {round(self.accuracy)}%   WPM: {round(self.wpm)}"

            if self.wpm > self.high_score:
                self.high_score = self.wpm
                self.save_high_score(self.high_score)
                self.results += " (New High Score!)"

            self.time_img = pygame.image.load('assets/icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            screen.blit(self.time_img, (self.width / 2 - 75, self.height - 140))
            self.draw_text(screen, "Reset", self.height - 70, 26, (255, 0, 0))

    def reset_game(self):
        self.screen.blit(self.image_open, (0, 0))
        pygame.display.update()
        time.sleep(1)
        self.reset = False
        self.end = False
        self.input_text = ''
        self.word = ''
        self.start_time = 0
        self.overall_time = 0
        self.wpm = 0
        self.word = self.get_challenge()
        if not self.word:
            self.reset_game()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.draw_text(self.screen, "Typing Speed Test", 80, 80, self.color_heading)
        self.draw_text(self.screen, f"High Score: {round(self.high_score)} WPM", 120, 28, (0, 255, 0))
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)
        self.draw_text(self.screen, self.word, 200, 28, self.color_text)
        pygame.display.update()

    def run(self):
        self.reset_game()
        running = True
        while running:
            print("Game is running...") 
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.color_heading, (50, 250, 650, 50), 2)
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 650 and 250 <= y <= 300:
                        self.active = True
                        self.input_text = ''
                        self.start_time = time.time()
                    if 310 <= x <= 510 and 390 <= y <= 430 and self.end:
                        self.reset_game()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            self.results_show(self.screen)
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            self.input_text += event.unicode
            clock.tick(60)
