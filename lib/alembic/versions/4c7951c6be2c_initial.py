"""initial

Revision ID: 4c7951c6be2c
Revises: d720ad470dc5
Create Date: 2023-09-13 15:25:13.075736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c7951c6be2c'
down_revision: Union[str, None] = 'd720ad470dc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'task_category_association',
        sa.Column('task_id', sa.Integer(), sa.ForeignKey('tasks.id'), primary_key=True),
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id'), primary_key=True)
    )

def downgrade():
    op.drop_table('task_category_association')
