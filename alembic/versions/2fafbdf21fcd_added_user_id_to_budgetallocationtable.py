"""Added user_id to BudgetAllocationTable

Revision ID: 2fafbdf21fcd
Revises: 1a8f91b84850
Create Date: 2024-05-03 18:23:38.480377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2fafbdf21fcd'
down_revision: Union[str, None] = '1a8f91b84850'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add the user_id column to the budget_allocation table
    op.add_column('budget_allocation', sa.Column('user_id', sa.Integer(), nullable=True))

    # Create a foreign key constraint to establish the relationship with the users table
    op.create_foreign_key('fk_budget_allocation_user_id_users', 'budget_allocation', 'users', ['user_id'], ['id'])


def downgrade():
    # Remove the foreign key constraint
    op.drop_constraint('fk_budget_allocation_user_id_users', 'budget_allocation', type_='foreignkey')

    # Remove the user_id column from the budget_allocation table
    op.drop_column('budget_allocation', 'user_id')
