"""Added account_balance column to User model

Revision ID: ad63109473a8
Revises: 31a4111afe41
Create Date: 2024-05-06 23:56:06.980810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad63109473a8'
down_revision: Union[str, None] = '31a4111afe41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add account_balance column to users table
    op.add_column('users', sa.Column('account_balance', sa.Float(), nullable=False, server_default='0.0'))


def downgrade():
    # Drop account_balance column from users table
    op.drop_column('users', 'account_balance')

