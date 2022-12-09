from typing import Iterable


class DummyAlgorithm(object):
    """Dummy algorithm.

    Simply returns the input data.
    """

    def __new__(cls, data):
        """Return the input data."""
        return data


class Loader:
    """Loader class."""

    def __init__(
        self, algorithm: str | type | None = "dummy", id_key: str = "id", string_key: str = "text"
    ):
        self.algorithm = algorithm
        self.id_key = id_key
        self.string_key = string_key
        self.wrapper = self._get_wrapper(self.algorithm)

    def load(self, data: Iterable):
        """Load data."""
        if isinstance(data, dict) and self._check_dict_keys(data):
            return {i: self.wrapper(s) for i, s in zip(data[self.id_key], data[self.string_key])}
        elif isinstance(data, list):
            if isinstance(data[0], dict):
                # keep original ID's
                return {list(dic.keys())[0]: self.wrapper(list(dic.values())[0]) for dic in data}
            else:
                return {idx: self.wrapper(element) for idx, element in enumerate(data)}
        elif isinstance(data, str):
            raise NotImplementedError()

        raise Exception("Data couldn't be loaded.")

    def _get_wrapper(self, algorithm: str | type | None):
        """Get the wrapper."""
        if isinstance(algorithm, str):
            if algorithm == "simhash":
                from simhash import Simhash

                return Simhash
        elif isinstance(algorithm, type):
            return algorithm

        return DummyAlgorithm

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
