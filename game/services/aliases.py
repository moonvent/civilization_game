from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel


class _WidgetKivyMetaInfo(BaseModel):
    title: str


class _WidgetUpdateData(BaseModel):
    widget_title: str
    value: Any


@dataclass(frozen=True)
class Alias:
    WidgetKivyMetaInfo = _WidgetKivyMetaInfo
    WidgetUpdateData = _WidgetUpdateData
