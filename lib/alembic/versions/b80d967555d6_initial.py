"""initial

Revision ID: b80d967555d6
Revises: 
Create Date: 2023-09-13 15:21:38.530592

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b80d967555d6'
down_revision: Union[str, None] = None
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
    )



def downgrade():
    op.drop_table('tasks')