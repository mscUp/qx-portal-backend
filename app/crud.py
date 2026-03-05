from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

# Banner CRUD
def get_banners(db: Session, skip: int = 0, limit: int = 100, status: Optional[bool] = None):
    query = db.query(models.Banner)
    if status is not None:
        query = query.filter(models.Banner.status == status)
    return query.order_by(models.Banner.order).offset(skip).limit(limit).all()

def get_banner(db: Session, banner_id: int):
    return db.query(models.Banner).filter(models.Banner.id == banner_id).first()

def create_banner(db: Session, banner: schemas.BannerCreate):
    db_banner = models.Banner(**banner.model_dump())
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner

def update_banner(db: Session, banner_id: int, banner: schemas.BannerUpdate):
    db_banner = get_banner(db, banner_id)
    if db_banner:
        update_data = banner.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_banner, key, value)
        db.commit()
        db.refresh(db_banner)
    return db_banner

def delete_banner(db: Session, banner_id: int):
    db_banner = get_banner(db, banner_id)
    if db_banner:
        db.delete(db_banner)
        db.commit()
    return db_banner

# Content Item CRUD
def get_content_items(db: Session, skip: int = 0, limit: int = 100, status: Optional[bool] = None):
    query = db.query(models.ContentItem)
    if status is not None:
        query = query.filter(models.ContentItem.status == status)
    return query.order_by(models.ContentItem.order).offset(skip).limit(limit).all()

def get_content_item(db: Session, item_id: int):
    return db.query(models.ContentItem).filter(models.ContentItem.id == item_id).first()

def create_content_item(db: Session, item: schemas.ContentItemCreate):
    db_item = models.ContentItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_content_item(db: Session, item_id: int, item: schemas.ContentItemUpdate):
    db_item = get_content_item(db, item_id)
    if db_item:
        update_data = item.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_content_item(db: Session, item_id: int):
    db_item = get_content_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

# Feature CRUD
def get_features(db: Session, skip: int = 0, limit: int = 100, status: Optional[bool] = None):
    query = db.query(models.Feature)
    if status is not None:
        query = query.filter(models.Feature.status == status)
    return query.order_by(models.Feature.order).offset(skip).limit(limit).all()

def get_feature(db: Session, feature_id: int):
    return db.query(models.Feature).filter(models.Feature.id == feature_id).first()

def create_feature(db: Session, feature: schemas.FeatureCreate):
    db_feature = models.Feature(**feature.model_dump())
    db.add(db_feature)
    db.commit()
    db.refresh(db_feature)
    return db_feature

def update_feature(db: Session, feature_id: int, feature: schemas.FeatureUpdate):
    db_feature = get_feature(db, feature_id)
    if db_feature:
        update_data = feature.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_feature, key, value)
        db.commit()
        db.refresh(db_feature)
    return db_feature

def delete_feature(db: Session, feature_id: int):
    db_feature = get_feature(db, feature_id)
    if db_feature:
        db.delete(db_feature)
        db.commit()
    return db_feature

# Ad Banner CRUD
def get_ad_banners(db: Session, skip: int = 0, limit: int = 100, status: Optional[bool] = None):
    query = db.query(models.AdBanner)
    if status is not None:
        query = query.filter(models.AdBanner.status == status)
    return query.offset(skip).limit(limit).all()

def get_ad_banner(db: Session, banner_id: int):
    return db.query(models.AdBanner).filter(models.AdBanner.id == banner_id).first()

def create_ad_banner(db: Session, banner: schemas.AdBannerCreate):
    banner_dict = banner.model_dump()
    if banner_dict.get('highlights'):
        banner_dict['highlights'] = [h.model_dump() if hasattr(h, 'model_dump') else h for h in banner_dict['highlights']]
    db_banner = models.AdBanner(**banner_dict)
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner

def update_ad_banner(db: Session, banner_id: int, banner: schemas.AdBannerUpdate):
    db_banner = get_ad_banner(db, banner_id)
    if db_banner:
        update_data = banner.model_dump(exclude_unset=True)
        if 'highlights' in update_data and update_data['highlights']:
            update_data['highlights'] = [h.model_dump() if hasattr(h, 'model_dump') else h for h in update_data['highlights']]
        for key, value in update_data.items():
            setattr(db_banner, key, value)
        db.commit()
        db.refresh(db_banner)
    return db_banner

def delete_ad_banner(db: Session, banner_id: int):
    db_banner = get_ad_banner(db, banner_id)
    if db_banner:
        db.delete(db_banner)
        db.commit()
    return db_banner
