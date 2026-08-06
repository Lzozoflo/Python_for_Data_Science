from os import get_terminal_size
from sys import argv, stdout
from time import time, sleep

class ft_tqdm:
    def __init__(self, iterable=None):
        self.iterable = iterable
        self.start_time = None
        self.n = 0

        if iterable is not None and hasattr(iterable, "__len__"):
            self.total = len(iterable)
        else:
            self.total = None


    def __iter__(self):
        """creat an iterator how update the percent bar every/iteration.
        
        End
        ---
            clear the sdtout.

        """
        self._start()
        for item in self.iterable:
            yield item
            self._update()
        self._close()


    def _start(self):
        """Save the starting time and display de frist bar"""
        self.start_time = time()
        self._display()


    def _update(self, n=1):
        """Called at every `__iter__` to display the next percent."""
        if self.start_time is None:
            self._start()
        self.n += n
        self._display()


    def _get_available_width(self, static_text):
        """Get available terminal width without the static len.

        Args:
            static_text_len (str): the size that we deduce from the static text. 

        Returns:
            int: max between 10 (minimal size) and available (current size or 80).
        """
        try:
            terminal_width = get_terminal_size().columns
        except OSError:
            terminal_width = 80
        
        available = terminal_width - len(static_text)
        return max(10, available)


    def _display(self):
        """used to creat the string with a \\r to write and flush in the same line
        
        Print
        ---
            \"percent%| bar | n / total [time elapsed<expected time, rate iteration/s]\"\n
            \"100%|████ |4/5 [00:15<00:00, 19.90it/s]\"
        """
        elapsed = time() - self.start_time if self.start_time else 0
        rate = self.n / elapsed if elapsed > 0 else 0
        elapsed_str = self._format_time(elapsed)

        if self.total:
            eta = (self.total - self.n) / rate if rate > 0 else 0
            eta_str = self._format_time(eta)
            fristPartBar = f"\r{(self.n / self.total) * 100:3.0f}%|"
            lastPartBar = f"| {self.n:3.0f}/{self.total} [{elapsed_str}<{eta_str}, {rate:3.2f}it/s]"

            bar_length = self._get_available_width(f"{fristPartBar}{lastPartBar}")
            filled_length = int(bar_length * self.n // self.total)

            stdout.write(f"{fristPartBar}{'█' * filled_length}{' ' * (bar_length - filled_length)}{lastPartBar}")
            stdout.flush()


    def _format_time(self, seconds):
        mins, secs = divmod(int(seconds), 60)
        return f"{mins:02d}:{secs:02d}"


    def _close(self):
        """Clear stdout"""
        stdout.write("\n")
        stdout.flush()
        pass


def main():
    """
    Description
    -----------
        Start of the programme.
    """

    try:
        assert len(argv) <= 1, "he arguments are bad"

        for item in ft_tqdm(range(300)):
            sleep(0.05)

    except Exception as e:
        print(f"{type(e).__name__} : {e}")

if __name__ == '__main__':
    main()









# class Utilisateur:
#     def __init__(self, nom, permissions=None):
#         self.nom = nom
#         if permissions:
#             for perm in permissions:
#                 # On utilise setattr pour créer dynamiquement les attributs
#                 setattr(self, f"peut_{perm}", True)