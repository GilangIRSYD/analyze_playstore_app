from sqlalchemy import Column, String, DECIMAL, Integer, TIMESTAMP, Text, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
import uuid
import enum

Base = declarative_base()
Metadata = Base.metadata

class SentimentEnum(str, enum.Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL" 
    
class CategoryEnum(str, enum.Enum):
    FEATURE = "FEATURE"
    BUG = "BUG"
    UX = "UX"
    NOISE = "NOISE"

class Application(Base):
    __tablename__ = "applications"

    application_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    summary = Column(String(255))
    name = Column(String(255), nullable=False)
    icon = Column(String(255))
    url = Column(String(255))
    score = Column(DECIMAL(3,2))
    total_review = Column(Integer)
    count_review = Column(Integer)
    developer_team = Column(String(255))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    token_next_scrape = Column(Text)
    
class Review(Base):
    __tablename__ = "reviews"
    
    review_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    application_id = Column(UUID(as_uuid=True)), ForeignKey("applications.application_id", nullable=False)
    content= Column(Text, nullable=True)
    username = Column(String(100), nullable=False)
    score = Column(DECIMAL(3, 2), nullable=False)
    user_pict = Column(String(255), nullable=True)
    version_app = Column(String(50), nullable=True)
    at = Column(TIMESTAMP, nullable=False)
    reply_content = Column(Text, nullable=True)
    reply_at = Column(TIMESTAMP, nullable=True)
    url = Column(String(255), nullable=True) 
    sentiment = Column(Enum(SentimentEnum, name="sentiment_enum"), nullable=False)
    category = Column(Enum(CategoryEnum, name="category_enum"), nullable=False)
