"""create table reviews

Revision ID: 84ee5a01f0f7
Revises: 566e0bdacc9a
Create Date: 2025-06-05 05:47:17.686295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84ee5a01f0f7'
down_revision: Union[str, None] = '566e0bdacc9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('review_id', sa.UUID(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('score', sa.DECIMAL(precision=3, scale=2), nullable=False),
    sa.Column('user_pict', sa.String(length=255), nullable=True),
    sa.Column('version_app', sa.String(length=50), nullable=True),
    sa.Column('at', sa.TIMESTAMP(), nullable=False),
    sa.Column('reply_content', sa.Text(), nullable=True),
    sa.Column('reply_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('sentiment', sa.Enum('POSITIVE', 'NEGATIVE', 'NEUTRAL', name='sentiment_enum'), nullable=False),
    sa.Column('category', sa.Enum('FEATURE', 'BUG', 'UX', 'NOISE', name='category_enum'), nullable=False),
    sa.PrimaryKeyConstraint('review_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
