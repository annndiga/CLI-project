"""create_table

Revision ID: e0cb0652fc93
Revises: 13624ba60ebe
Create Date: 2023-09-10 21:20:11.965523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0cb0652fc93'
down_revision: Union[str, None] = '13624ba60ebe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text),
        sa.Column('priority', sa.String),  # You can specify the appropriate data type for priority
        sa.Column('due_date', sa.String),  # You can specify the appropriate data type for due date
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'))
    )


def downgrade():
    op.drop_table('tasks')