"""create_expense_table

Revision ID: 1e3b257b70eb
Revises: b0072bd0550a
Create Date: 2024-05-02 12:40:59.271637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e3b257b70eb'
down_revision: Union[str, None] = 'b0072bd0550a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'expenses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('amount', sa.Float),
        sa.Column('category', sa.String),
        sa.Column('date', sa.Date),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
    )


def downgrade():
    op.drop_table('expenses')
