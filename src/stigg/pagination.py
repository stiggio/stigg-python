# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["MyCursorIDPagePagination", "SyncMyCursorIDPage", "AsyncMyCursorIDPage"]

_T = TypeVar("_T")


class MyCursorIDPagePagination(BaseModel):
    next: Optional[str] = None

    prev: Optional[str] = None


class SyncMyCursorIDPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[MyCursorIDPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        if self._options.params.get("before"):
            prev = None
            if self.pagination is not None:
                if self.pagination.prev is not None:
                    prev = self.pagination.prev
            if not prev:
                return None

            return PageInfo(params={"before": prev})

        next = None
        if self.pagination is not None:
            if self.pagination.next is not None:
                next = self.pagination.next
        if not next:
            return None

        return PageInfo(params={"after": next})


class AsyncMyCursorIDPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[MyCursorIDPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        if self._options.params.get("before"):
            prev = None
            if self.pagination is not None:
                if self.pagination.prev is not None:
                    prev = self.pagination.prev
            if not prev:
                return None

            return PageInfo(params={"before": prev})

        next = None
        if self.pagination is not None:
            if self.pagination.next is not None:
                next = self.pagination.next
        if not next:
            return None

        return PageInfo(params={"after": next})
