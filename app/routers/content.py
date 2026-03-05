from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/api/content", tags=["content"])

@router.get("/items", response_model=List[schemas.ContentItem])
def read_content_items(
    skip: int = 0,
    limit: int = 100,
    status: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    """Get all content items"""
    items = crud.get_content_items(db, skip=skip, limit=limit, status=status)
    return items

@router.get("/items/{item_id}", response_model=schemas.ContentItem)
def read_content_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific content item"""
    item = crud.get_content_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Content item not found")
    return item

@router.post("/items", response_model=schemas.ContentItem)
def create_content_item(item: schemas.ContentItemCreate, db: Session = Depends(get_db)):
    """Create a new content item"""
    return crud.create_content_item(db=db, item=item)

@router.put("/items/{item_id}", response_model=schemas.ContentItem)
def update_content_item(
    item_id: int,
    item: schemas.ContentItemUpdate,
    db: Session = Depends(get_db)
):
    """Update a content item"""
    db_item = crud.update_content_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Content item not found")
    return db_item

@router.delete("/items/{item_id}")
def delete_content_item(item_id: int, db: Session = Depends(get_db)):
    """Delete a content item"""
    db_item = crud.delete_content_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Content item not found")
    return {"message": "Content item deleted successfully"}
