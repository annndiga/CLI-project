"""create_table

Revision ID: cdf5f41ad4ac
Revises: e0cb0652fc93
Create Date: 2023-09-10 22:01:06.501263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdf5f41ad4ac'
down_revision: Union[str, None] = 'e0cb0652fc93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(length=255), unique=True, nullable=False),
        sa.Column('email', sa.String(length=255), unique=True, nullable=False),
        # Add more columns as needed
    )


def downgrade():
    op.drop_table('users')
