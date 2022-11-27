import itertools
from typing import Iterable


class DuplicateDetector:
    """Duplicate detector class.

    Parameters
    ----------
    algorithm : str | None, optional
        Algorithm to use for calculating if two strings are a duplicate. Choices are ['simhash',
        None]. If None, 'simhas' will be used, by default 'simhash'.
    """

    data: list

    def __init__(self, algorithm: str | None = "simhash"):
        self.algorithm = algorithm or "simhash"

    def compare(self, string: str, another: str) -> int | None:
        """Compute if the two strings are duplicates."""
        if self.algorithm == "simhash":
            from simhash import Simhash

            return Simhash(string).distance(Simhash(another))
        else:
            return None

    def fit(self, iterable: Iterable):
        """Compare unique string pairs if they are duplicates.

        Notes
        -----
        - Doesn't compare a string with itself.
        """
        self.data = [
            self.compare(pair[0], pair[1]) for pair in itertools.combinations(iterable, 2)
        ]
