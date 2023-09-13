"""initial

Revision ID: 8e50e5934b87
Revises: b80d967555d6
Create Date: 2023-09-13 15:23:03.615732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e50e5934b87'
down_revision: Union[str, None] = 'b80d967555d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        
    )

def downgrade():
    op.drop_table('users')
