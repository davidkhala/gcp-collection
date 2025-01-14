from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypedDict, NotRequired


@dataclass
class ServiceAccountInfo(TypedDict):
    client_email: str
    private_key: str
    token_uri: NotRequired[str]
    project_id: NotRequired[str]


class OptionsInterface(ABC):
    @property
    @abstractmethod
    def credentials(self):
        pass

    @abstractmethod
    @property
    def projectId(self):
        pass
