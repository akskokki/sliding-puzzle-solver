import pygame


class GameLoop:
    def __init__(self, board, renderer, event_queue, clock):
        self.board = board
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock

        self.running = True
    
    def start(self):
        while self.running:
            self._handle_events()
            self.board.update()
            self.renderer.render()
            self.clock.tick(60)
    
    def _handle_events(self):
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.board.click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.board.scramble()