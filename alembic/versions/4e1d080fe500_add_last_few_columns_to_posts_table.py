"""add last few columns to posts table

Revision ID: 4e1d080fe500
Revises: 5956042d3f6b
Create Date: 2024-07-16 04:07:45.285683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e1d080fe500'
down_revision: Union[str, None] = '5956042d3f6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
            ('NOW()')),)


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
