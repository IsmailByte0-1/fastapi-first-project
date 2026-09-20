from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas,utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)
@router.post('/', status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_users(user : schemas.UserCreate ,db : Session = Depends(get_db)):


    #hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.Users(**user.model_dump()) # model_dump() to make it as dictonary
                                                    # i should serach about it more

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db : Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"user with this {id} not existed")
    return user