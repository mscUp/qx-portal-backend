from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Banner Schemas
class BannerBase(BaseModel):
    title: str
    subtitle: Optional[str] = None
    description: Optional[str] = None
    badge: Optional[str] = None
    button1_text: Optional[str] = None
    button2_text: Optional[str] = None
    stat1_value: Optional[str] = None
    stat1_label: Optional[str] = None
    stat2_value: Optional[str] = None
    stat2_label: Optional[str] = None
    stat3_value: Optional[str] = None
    stat3_label: Optional[str] = None
    image_url: Optional[str] = None
    link: Optional[str] = None
    order: int = 0
    status: bool = True

class BannerCreate(BannerBase):
    pass

class BannerUpdate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    description: Optional[str] = None
    badge: Optional[str] = None
    button1_text: Optional[str] = None
    button2_text: Optional[str] = None
    stat1_value: Optional[str] = None
    stat1_label: Optional[str] = None
    stat2_value: Optional[str] = None
    stat2_label: Optional[str] = None
    stat3_value: Optional[str] = None
    stat3_label: Optional[str] = None
    image_url: Optional[str] = None
    link: Optional[str] = None
    order: Optional[int] = None
    status: Optional[bool] = None

class Banner(BannerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Content Item Schemas
class ContentItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    cover: Optional[str] = None
    category: Optional[str] = None
    views: str = "0"
    likes: str = "0"
    comments: str = "0"
    author: Optional[str] = None
    order: int = 0
    status: bool = True

class ContentItemCreate(ContentItemBase):
    pass

class ContentItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    category: Optional[str] = None
    views: Optional[str] = None
    likes: Optional[str] = None
    comments: Optional[str] = None
    author: Optional[str] = None
    order: Optional[int] = None
    status: Optional[bool] = None

class ContentItem(ContentItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Feature Schemas
class FeatureBase(BaseModel):
    title: str
    description: Optional[str] = None
    icon: Optional[str] = None
    gradient: Optional[str] = None
    order: int = 0
    status: bool = True

class FeatureCreate(FeatureBase):
    pass

class FeatureUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    gradient: Optional[str] = None
    order: Optional[int] = None
    status: Optional[bool] = None

class Feature(FeatureBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Ad Banner Schemas
class HighlightItem(BaseModel):
    icon: str
    title: str
    desc: str
    color: str

class AdBannerBase(BaseModel):
    title: str
    subtitle: Optional[str] = None
    description: Optional[str] = None
    cta_text: Optional[str] = None
    cta_link: Optional[str] = None
    highlights: Optional[List[HighlightItem]] = None
    status: bool = True

class AdBannerCreate(AdBannerBase):
    pass

class AdBannerUpdate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    description: Optional[str] = None
    cta_text: Optional[str] = None
    cta_link: Optional[str] = None
    highlights: Optional[List[HighlightItem]] = None
    status: Optional[bool] = None

class AdBanner(AdBannerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
