from time import time


class Logger:
    """ Prints status updates for the solver

    Attributes:
        update_interval: The time between status updates
    """

    def __init__(self):
        """Class constructor"""
        self.update_interval = 0.1
        self.reset()

    def reset(self):
        """Resets the logger state to zeros"""
        self.nodes = 0
        self.bound = 0
        self.start_time = time()
        self.previous_update_time = 0

    def update(self):
        """Prints out the current logger information up to once every 0.1 seconds"""
        elapsed_time = time() - self.start_time
        if self.previous_update_time == 0:
            print('\n\n\n')
        elif elapsed_time - self.previous_update_time <= self.update_interval:
            return
        self.previous_update_time = elapsed_time
        print("\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K")
        print(f'Time elapsed: {round(elapsed_time, 1)}')
        print(f'Current bound: {self.bound}')
        print(f'Nodes checked: {self.nodes}')

    def add_node(self):
        """Adds a node to the count and calls for an update"""
        self.nodes += 1
        self.update()

    def set_bound(self, new_bound):
        """Sets a new bound and calls for an update"""
        self.bound = new_bound
        self.update()
