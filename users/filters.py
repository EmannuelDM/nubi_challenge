from typing import Optional
from fastapi_filter.contrib.sqlalchemy import Filter
from users.models import DbUser

class UserFilter(Filter):
    class Constants(Filter.Constants):
        model = DbUser
        
    order_by: Optional[list[str]] = None