"""auto-vote

Revision ID: 6cda234f5ba8
Revises: 4e1d080fe500
Create Date: 2024-07-16 04:40:24.033203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cda234f5ba8'
down_revision: Union[str, None] = '4e1d080fe500'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
                  sa.Column('user_id', sa.Integer(), nullable=False),
                  sa.Column('post_id', sa.Integer(), nullable=False),
                  sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                  sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                  sa.PrimaryKeyConstraint('user_id', 'post_id')
                  )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
