"""modify expense table

Revision ID: ce35fee10a1e
Revises: 1e3b257b70eb
Create Date: 2024-05-03 16:19:54.758015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce35fee10a1e'
down_revision: Union[str, None] = '1e3b257b70eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add new columns for expense categories
    op.add_column('expenses', sa.Column('groceries', sa.Float))
    op.add_column('expenses', sa.Column('fuel', sa.Float))
    op.add_column('expenses', sa.Column('bills', sa.Float))
    op.add_column('expenses', sa.Column('travel', sa.Float))
    op.add_column('expenses', sa.Column('apparel', sa.Float))
    op.add_column('expenses', sa.Column('utilities', sa.Float))
    op.add_column('expenses', sa.Column('other', sa.Float))

   

def downgrade():
    # Reverse the changes in the upgrade function
    op.drop_column('expenses', 'category')

    op.add_column('expenses', sa.Column('category', sa.String))

    op.drop_column('expenses', 'groceries')
    op.drop_column('expenses', 'fuel')
    op.drop_column('expenses', 'bills')
    op.drop_column('expenses', 'travel')
    op.drop_column('expenses', 'apparel')
    op.drop_column('expenses', 'utilities')
    op.drop_column('expenses', 'other')