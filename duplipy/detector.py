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
        if self.algorithm == "simhash":
            from simhash import Simhash

            return hash.distance(another)
        else:
            return None

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
        if self.algorithm == "simhash":
            from simhash import Simhash

            cls = Simhash
        else:
            cls = None

        if cls:
            if isinstance(iterable, dict) and self._check_dict_keys(iterable):
                self.data = {
                    i: cls(s) for i, s in zip(iterable[self.id_key], iterable[self.string_key])
                }
            elif isinstance(iterable, list):
                if isinstance(iterable[0], dict):
                    # keep original ID's
                    self.data = {
                        list(dic.keys())[0]: cls(list(dic.values())[0]) for dic in iterable
                    }
                else:
                    self.data = {idx: cls(element) for idx, element in enumerate(iterable)}

    def _check_dict_keys(self, iterable: Iterable) -> bool:
        """TODO: docstring."""
        if self.id_key not in iterable:
            raise KeyError(
                f"'{self.id_key}' is not in the given dictionary. Change the `id_key` parameter "
                "or rename the id entry in your data."
            )
        else:
            if self.string_key not in iterable:
                raise KeyError(
                    f"'{self.string_key}' is not in the given dictionary. Change the "
                    "`string_key` parameter or rename the string entry in your data."
                )
            else:
                return True

    def _get_pair(self, iterable: Iterable):
        """TODO: docstring."""
        for pair in itertools.combinations(iterable, 2):
            yield pair
