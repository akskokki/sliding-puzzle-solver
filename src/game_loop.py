import pygame


class GameLoop:
    def __init__(self, board, ui, renderer, event_queue, clock, solver):
        self.board = board
        self.ui = ui
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock

        self.solver = solver
        self.solver_move_index = 0
        self.solver_moves = []

        self.running = True

    def start(self):
        while self.running:
            self._handle_events()
            self.ui.update()
            self.renderer.render()
            self.clock.tick(60)

    def _handle_events(self):
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         self.board.click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.board.scramble()
                elif event.key == pygame.K_UP:
                    self.board.move(self.board.UP)
                elif event.key == pygame.K_LEFT:
                    self.board.move(self.board.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.board.move(self.board.RIGHT)
                elif event.key == pygame.K_DOWN:
                    self.board.move(self.board.DOWN)
                elif event.key == pygame.K_RETURN:
                    if len(self.solver_moves) == 0:
                        self.solver_moves = self.solver.run()
                        self.solver_move_index = 0
                    else:
                        self.board.move(
                            self.solver_moves[self.solver_move_index])
                        if self.board.check_win():
                            self.solver_move_index = 0
                            self.solver_moves = []
                        else:
                            self.solver_move_index += 1
