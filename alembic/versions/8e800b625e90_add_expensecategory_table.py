"""Add ExpenseCategory table

Revision ID: 8e800b625e90
Revises: 2fafbdf21fcd
Create Date: 2024-05-03 19:24:37.090787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e800b625e90'
down_revision: Union[str, None] = '2fafbdf21fcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'expense_category',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),  # Assuming 'user' table exists
    )

def downgrade():
    op.drop_table('expense_category')
