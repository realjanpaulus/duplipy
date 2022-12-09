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

    data: dict

    def __init__(
        self, algorithm: str | None = "simhash", id_key: str = "id", string_key: str = "text"
    ):
        self.algorithm = algorithm or "simhash"
        self.id_key = id_key
        self.string_key = string_key

    def compare_hashes(self, hash, another: str) -> int | None:
        """Compute if the two strings are duplicates."""
        return hash.distance(another)

    def compare_strings(self, string: str, another: str) -> int | None:
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
        # TODO
        # if self.algorithm == "simhash":
        #     from simhash import Simhash

        #     cls = Simhash
        # else:
        #     cls = None

        # if cls:

    def _get_pair(self, iterable: Iterable):
        """TODO: docstring."""
        for pair in itertools.combinations(iterable, 2):
            yield pair
