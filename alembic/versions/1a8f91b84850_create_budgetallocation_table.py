"""Create BudgetAllocation table

Revision ID: 1a8f91b84850
Revises: ce35fee10a1e
Create Date: 2024-05-03 17:33:07.377421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a8f91b84850'
down_revision: Union[str, None] = 'ce35fee10a1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'budget_allocation',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('groceries', sa.Float),
        sa.Column('fuel', sa.Float),
        sa.Column('bills', sa.Float),
        sa.Column('travel', sa.Float),
        sa.Column('apparel', sa.Float),
        sa.Column('utilities', sa.Float),
        sa.Column('other', sa.Float),
    )

def downgrade():
    op.drop_table('budget_allocation')
