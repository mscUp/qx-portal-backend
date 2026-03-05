from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/api/banners", tags=["banners"])

@router.get("", response_model=List[schemas.Banner])
def read_banners(
    skip: int = 0,
    limit: int = 100,
    status: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    """Get all banners"""
    banners = crud.get_banners(db, skip=skip, limit=limit, status=status)
    return banners

@router.get("/{banner_id}", response_model=schemas.Banner)
def read_banner(banner_id: int, db: Session = Depends(get_db)):
    """Get a specific banner"""
    banner = crud.get_banner(db, banner_id=banner_id)
    if banner is None:
        raise HTTPException(status_code=404, detail="Banner not found")
    return banner

@router.post("", response_model=schemas.Banner)
def create_banner(banner: schemas.BannerCreate, db: Session = Depends(get_db)):
    """Create a new banner"""
    return crud.create_banner(db=db, banner=banner)

@router.put("/{banner_id}", response_model=schemas.Banner)
def update_banner(
    banner_id: int,
    banner: schemas.BannerUpdate,
    db: Session = Depends(get_db)
):
    """Update a banner"""
    db_banner = crud.update_banner(db, banner_id=banner_id, banner=banner)
    if db_banner is None:
        raise HTTPException(status_code=404, detail="Banner not found")
    return db_banner

@router.delete("/{banner_id}")
def delete_banner(banner_id: int, db: Session = Depends(get_db)):
    """Delete a banner"""
    db_banner = crud.delete_banner(db, banner_id=banner_id)
    if db_banner is None:
        raise HTTPException(status_code=404, detail="Banner not found")
    return {"message": "Banner deleted successfully"}
