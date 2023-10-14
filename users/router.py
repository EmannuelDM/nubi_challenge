from typing import List
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from auth.oauth2 import get_current_user
from db.database import get_db
from users.schemas import UserBase, UserDisplay, UserUpdate
import users.services as services
from utils.pagination import PaginatedParams

router = APIRouter(
  prefix='/user',
  tags=['user']
)

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
  return services.create_user(db, request)

# Read all users
@router.get('/' ) #response_model=List[UserDisplay]
def get_all_users(pagination: PaginatedParams = Depends(), db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return services.get_all_users(db, pagination)

# Read one user
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return services.get_user(db, id)

# Update user
@router.post('/{id}/update')
def update_user(id: int, request: UserUpdate, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return services.update_user(db, id, request)

# Delete user
@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return services.delete_user(db, id)
