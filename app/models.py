from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from .database import Base

class Banner(Base):
    __tablename__ = "banners"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    subtitle = Column(String(500))
    description = Column(Text)
    badge = Column(String(200))
    button1_text = Column(String(100))
    button2_text = Column(String(100))
    stat1_value = Column(String(50))
    stat1_label = Column(String(50))
    stat2_value = Column(String(50))
    stat2_label = Column(String(50))
    stat3_value = Column(String(50))
    stat3_label = Column(String(50))
    image_url = Column(String(500))
    link = Column(String(500))
    order = Column(Integer, default=0)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ContentItem(Base):
    __tablename__ = "content_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    cover = Column(String(500))
    category = Column(String(100))
    views = Column(String(20), default="0")
    likes = Column(String(20), default="0")
    comments = Column(String(20), default="0")
    author = Column(String(100))
    status = Column(Boolean, default=True)
    order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    icon = Column(String(100))
    gradient = Column(String(100))
    order = Column(Integer, default=0)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class AdBanner(Base):
    __tablename__ = "ad_banners"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    subtitle = Column(String(500))
    description = Column(Text)
    cta_text = Column(String(100))
    cta_link = Column(String(500))
    highlights = Column(JSON)  # Store array of highlights
    status = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(Text)
    description = Column(String(500))
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
