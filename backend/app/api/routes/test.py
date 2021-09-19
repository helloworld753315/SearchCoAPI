from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_hedgehogs() -> List[dict]:
    json = [
        {"id": 1, "subject": "コラ画像概論", "teacher": "三条悟", "unit": 2},
        {"id": 1, "subject": "ほげほげ概論", "teacher": "HOGE・HOGE・HOGE", "unit": 4}
    ]

    return json
