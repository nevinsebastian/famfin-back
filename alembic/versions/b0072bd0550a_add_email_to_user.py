"""add_email_to_user

Revision ID: b0072bd0550a
Revises: 
Create Date: 2024-05-02 11:56:28.444050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0072bd0550a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, unique=True),
        sa.Column('email', sa.String, unique=True),
        sa.Column('password', sa.String),
    )


def downgrade():
    op.drop_table('users')
