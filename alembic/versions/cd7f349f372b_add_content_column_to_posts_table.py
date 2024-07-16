"""add content column to posts table

Revision ID: cd7f349f372b
Revises: f5ce50f5c2de
Create Date: 2024-07-16 02:40:25.005976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd7f349f372b'
down_revision: Union[str, None] = 'f5ce50f5c2de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('posts', 'content')
