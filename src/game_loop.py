import pygame
from copy import deepcopy


class GameLoop:
    """ Controls the game loop and user input

    Attributes:
        board: Board that handles game logic
        ui: Pygame UI
        renderer: Pygame renderer
        event_queue: Pygame EventQueue
        clock: Pygame Clock
        solver: The IDAStar solving algorithm
        solver_moves: List of moves returned by the solver
        solver_move_index: Keeps track of solver moves used
        running: Boolean that determines whether the game is running
    """

    def __init__(self, board, ui, renderer, event_queue, clock, solver):
        """
        Class constructor

        Args:
            board: Board that handles game logic
            ui: Pygame UI
            renderer: Pygame renderer
            event_queue: Pygame EventQueue
            clock: Pygame Clock
            solver: The IDAStar solving algorithm
        """
        self.board = board
        self.ui = ui
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock

        self.solver = solver
        self.solver_moves = []
        self.solver_move_index = 0
        self.solver_board_state = None

        self.running = True

    def start(self):
        """Runs the game loop"""
        while self.running:
            self._handle_events()
            self.ui.update()
            self.renderer.render()
            self.clock.tick(60)

    def _handle_events(self):
        """Handles pygame-events in the event queue"""
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         self.board.click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self._handle_solver()
                elif event.key == pygame.K_SPACE:
                    self.board.scramble()
                elif event.key == pygame.K_UP:
                    self.board.move(self.board.UP)
                elif event.key == pygame.K_LEFT:
                    self.board.move(self.board.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.board.move(self.board.RIGHT)
                elif event.key == pygame.K_DOWN:
                    self.board.move(self.board.DOWN)
                elif event.key == pygame.K_r:
                    new_numbers = input("\nNew number grid to be used: ")
                    self.board.set_numbers(new_numbers)

    def _handle_solver(self):
        """Handles functionality of solver button"""
        # Reset solver if board state has changed since last move
        if self.board.numbers_grid != self.solver_board_state:
            self._reset_solver()

        # Run solver if move list is empty
        if len(self.solver_moves) == 0:
            self.solver_moves = self.solver.run()
            self.solver_move_index = 0
            self.solver_board_state = deepcopy(
                self.board.numbers_grid)

        # Advance solver if there are moves to be made
        else:
            self.board.move(
                self.solver_moves[self.solver_move_index])
            self.solver_board_state = deepcopy(
                self.board.numbers_grid)
            self.solver_move_index += 1
            if self.board.check_win():
                self._reset_solver()

    def _reset_solver(self):
        """Resets solver values"""
        self.solver_moves = []
        self.solver_move_index = 0
