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
    
class AnalysisStatusEnum(str, enum.Enum):
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"

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
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
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

class Analysis(Base):
    __tablename__ = "analyses"

    analysis_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    application_id = Column(UUID(as_uuid=True), ForeignKey("applications.application_id"), nullable=False)
    negative_wordclouds = Column(String(255), nullable=True)
    positive_wordclouds = Column(String(255), nullable=True)
    neutral_wordclouds = Column(String(255), nullable=True)
    bug_wordclouds = Column(String(255), nullable=True)
    feature_wordclouds = Column(String(255), nullable=True)
    ux_wordclouds = Column(String(255), nullable=True)
    noise_wordclouds = Column(String(255), nullable=True)
    positive_count = Column(Integer, nullable=False, default=0)
    negative_count = Column(Integer, nullable=False, default=0)
    neutral_count = Column(Integer, nullable=False, default=0)
    bug_count = Column(Integer, nullable=False, default=0)
    feature_count = Column(Integer, nullable=False, default=0)
    ux_count = Column(Integer, nullable=False, default=0)
    noise_count = Column(Integer, nullable=False, default=0)
    last_analysis_at = Column(TIMESTAMP, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    confidence_score_sentiment = Column(DECIMAL(3, 2), nullable=True)
    confidence_score_category = Column(DECIMAL(3, 2), nullable=True)
    status = Column(Enum(AnalysisStatusEnum, name="analysis_status_enum"), default=AnalysisStatusEnum.PROCESSING, nullable=False)
    
class ReviewAnalysis(Base):
    __tablename__ = "review_analyses"

    review_analysis_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    review_id = Column(UUID(as_uuid=True), ForeignKey("reviews.review_id"), nullable=False)
    analysis_id = Column(UUID(as_uuid=True), ForeignKey("analyses.analysis_id"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
