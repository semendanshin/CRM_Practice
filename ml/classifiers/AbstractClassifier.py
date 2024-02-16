from abc import ABC, abstractmethod
from .types import Response


class AbstractClassifier(ABC):
    @abstractmethod
    async def predict(self, text: str) -> Response:
        pass
