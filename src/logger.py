from time import time


class Logger:
    """ Prints status updates for the solver

    Attributes:
        update_interval: The time between status updates
    """

    def __init__(self):
        """Class constructor"""
        self.update_interval = 0.1
        self.nodes = 0
        self.bound = 0
        self.start_time = time()
        self.previous_update_time = 0

    def reset(self):
        """Resets the logger state to zeros"""
        self.nodes = 0
        self.bound = 0
        self.start_time = time()
        self.previous_update_time = 0

    def _update(self):
        """Prints out the current logger information up to once every 0.1 seconds

        Returns:
            elapsed_time (float): Time elapsed since starting the search
        """
        elapsed_time = time() - self.start_time
        if self.previous_update_time == 0:
            print('\n\n')
        elif elapsed_time - self.previous_update_time <= self.update_interval:
            return elapsed_time
        self.previous_update_time = elapsed_time
        print("\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K")
        print(f'Time elapsed: {round(elapsed_time, 1)}')
        print(f'Current bound: {self.bound}')
        print(f'Nodes checked: {self.nodes}')
        return elapsed_time

    def add_node(self):
        """Adds a node to the count and calls for an update

        Returns: Return value of update()
        """
        self.nodes += 1
        return self._update()

    def set_bound(self, new_bound):
        """Sets a new bound and calls for an update

        Returns: Return value of update()
        """
        self.bound = new_bound
        return self._update()

    def get_elapsed_time(self):
        elapsed_time = time() - self.start_time
        print(elapsed_time)
        print('')
        return elapsed_time
