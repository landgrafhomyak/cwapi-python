from asyncio import AbstractEventLoop
from enum import Enum
from typing import ClassVar, TypeVar, Generic, Literal, NoReturn

from .requests import request

__PROTOCOL = TypeVar("__PROTOCOL", bound=str)
__HOST = TypeVar("__HOST", bound=str)
__PORT = TypeVar("__PORT", bound=int)


class Server(Enum, Generic[__PROTOCOL, __HOST, __PORT]):
    @property
    def protocol(self) -> __PROTOCOL: ...

    @property
    def host(self) -> __HOST: ...

    @property
    def port(self) -> __PORT: ...

    def build_address(self, instance_name: str, password: str) -> str: ...

    Classic: ClassVar[Server[Literal[None], Literal[None], Literal[None]]] = ...
    International: ClassVar[Server[Literal["amqps"], Literal["api.chatwars.me"], Literal[5673]]] = ...
    CW3: ClassVar[Server[Literal["amqps"], Literal["api.chtwrs.com"], Literal[5673]]] = ...


__SERVER = TypeVar("__SERVER", bound=Server)
__INSTANCE_NAME = TypeVar("__INSTANCE_NAME", bound=str)


class ChatWarsApiClient(Generic[__SERVER, __INSTANCE_NAME]):
    @property
    def instance_name(self) -> __INSTANCE_NAME: ...

    @property
    def connection_link(self) -> str: ...

    @property
    def server(self) -> __SERVER: ...

    @property
    def output_exchange_name(self) -> str: ...

    @property
    def input_queue_name(self) -> str: ...

    @property
    def routing_key(self) -> str: ...

    def __new__(cls, server: __SERVER, instance_name: __INSTANCE_NAME, password: str) -> ChatWarsApiClient[__SERVER, __INSTANCE_NAME]: ...

    def connect(self) -> NoReturn: ...

    def disconnect(self) -> NoReturn: ...

    def send(self, req: request, /) -> NoReturn: ...

    def __enter__(self) -> ChatWarsApiClient: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> Literal[False]: ...


class AsyncChatWarsApiClient(ChatWarsApiClient):
    @property
    def loop(self) -> AbstractEventLoop: ...

    async def connect(self) -> NoReturn: ...

    async def disconnect(self) -> NoReturn: ...

    async def __aenter__(self) -> AsyncChatWarsApiClient: ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> Literal[False]: ...
