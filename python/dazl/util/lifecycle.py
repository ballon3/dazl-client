# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from asyncio import AbstractEventLoop, Future, get_event_loop, InvalidStateError
from concurrent.futures import Executor, ThreadPoolExecutor
from threading import RLock
from typing import Awaitable, Callable, List, Optional, TypeVar, cast, overload


T = TypeVar('T')


class Lifecycle:
    """
    Manages scheduling, execution, and lifecycle concerns. Unless otherwise stated, all methods are
    thread-safe.
    """
    def __init__(self):
        self._lock = RLock()
        self._loop = None  # type: Optional[AbstractEventLoop]
        self._executor = None  # type: Optional[Executor]
        self._tracked_futures = []  # type: List[Future]

    def set_context_as_current(self) -> None:
        """
        Adopt the current event loop as the loop for this :class:`Invoker`, and additionally define
        a default executor if one has not yet been set. This method is NOT thread safe and should
        only be called once.
        """
        self._loop = get_event_loop()
        self._executor = ThreadPoolExecutor()

    def get_loop(self) -> Optional[AbstractEventLoop]:
        return self._loop

    def set_loop(self, loop):
        self._loop = loop

    def get_executor(self) -> Optional[Executor]:
        return self._executor

    def set_executor(self, executor):
        self._executor = executor

    def set_global_exception(self, ex: BaseException) -> None:
        """
        Terminate all pending Futures with the specified exception. Subsequent calls to
        ``create_future`` and ``ensure_future`` associated with the same lifecycle will also
        immediately return exceptions that have failed with this exception.

        This call does NOT block in order to avoid potential deadlocks, so it is NOT guaranteed
        that all outstanding futures will have failed yet. However, it IS guaranteed that any
        subsequent future created from this :class:`Lifecycle` will be in a failed state.
        """
        with self._lock:
            for fut in self._tracked_futures:
                try:
                    loop = fut._loop
                    if loop is not None:
                        loop.
                    fut._loop
                    fut.set_exception(ex)
                except InvalidStateError:


    def create_future(self) -> Future:
        """
        Create a :class:`Future` that is responsive to :meth:`set_global_exception` to provide a
        centralized way of failing any outstanding futures.
        """

    def ensure_future(self, coro) -> Future:
        """
        Wrap the coroutine or task in a ``Future``. Futures returned from this method are also
        responsive to :meth:`set_global_exception` to provide a centralized way of failing any
        outstanding futures.

        :param coro: The coroutine, task, or future to wrap.
        :return: A future.
        """

    @overload
    def run_in_loop(self, func: Callable[[], Awaitable[None]], timeout: float = 30) -> None: ...

    @overload
    def run_in_loop(self, func: Callable[[], None], timeout: float = 30) -> None: ...

    @overload
    def run_in_loop(self, func: Callable[[], Awaitable[T]], timeout: float = 30) -> T: ...

    @overload
    def run_in_loop(self, func: Callable[[], T], timeout: float = 30) -> T: ...

    def run_in_loop(self, func, timeout: float = 30.0):
        """
        Schedule a normal function or coroutine function to be run on the event loop, and block
        until the function has returned.
        """
        # TODO: the awful awful witchcraft required to remove these checks
        if self._loop is None:
            raise InvalidStateError('loop must be set before calling these methods')
        return execute_in_loop(self._loop, func, timeout=timeout)

    def run_in_executor(self, func: 'Callable[[], T]') -> Awaitable[T]:
        """
        Schedule a normal function to be run on a background thread, and yield until the function
        has returned.
        """
        # TODO: the awful awful witchcraft required to remove these checks
        if self._loop is None or self._executor is None:
            raise InvalidStateError('loop must be set before calling these methods')

        # for some reason, PyCharm doesn't seem to like this type so make an explicit cast
        return cast(Awaitable[T], self._loop.run_in_executor(self._executor, func))
