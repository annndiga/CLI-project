"""initial

Revision ID: d720ad470dc5
Revises: 8e50e5934b87
Create Date: 2023-09-13 15:24:08.246378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd720ad470dc5'
down_revision: Union[str, None] = '8e50e5934b87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
    )
def downgrade():
    op.drop_table('categories')
