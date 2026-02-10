from typing import Any, Generator


def chunked(iterable: Any, size: int = 1000) -> Generator[Any, None, None]:
    for i in range(0, len(iterable), size):
        yield iterable[i : i + size]
