# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging
from typing import Union

from fastapi import FastAPI

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    datefmt="%d.%m.%Y %H:%M:%S",
    format="[%(asctime)s] %(levelname)s [%(name)s:%(module)s - %(funcName)s:%(lineno)s] %(message)s")

app = FastAPI()


@app.get("/")
def read_root():
    logger.info("yolo")
    return {"Hello": "WorldZOOP "}


@app.get("/items/{item_id}")
def read_item(
        item_id: int,
        q: Union[str, None] = None
):
    return {"item_id": item_id, "q": q}
