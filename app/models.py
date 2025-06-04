from sqlalchemy import Column, String, DECIMAL, Integer, TIMESTAMP, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()
Metadata = Base.metadata

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