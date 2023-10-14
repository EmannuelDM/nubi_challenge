from fastapi import  Query
from sqlalchemy import select, func, Select
from sqlalchemy.orm.session import Session


class PaginatedParams:
    def __init__(self, page: int = Query(1, ge=1), limit: int = Query(100, ge=0)):
        self.limit = limit
        self.offset = (page - 1) * limit


def paginate(db: Session, query: Select, limit: int, offset: int) -> dict:

    return {
        'count':  db.scalar(select(func.count()).select_from(query.subquery())),
        'items': [todo for todo in  db.scalars(query.limit(limit).offset(offset))]
    }