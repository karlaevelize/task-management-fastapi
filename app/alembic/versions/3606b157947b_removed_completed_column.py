"""Removed completed column

Revision ID: 3606b157947b
Revises: 75f4f5edb8d4
Create Date: 2023-02-03 19:06:37.123309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3606b157947b'
down_revision = '75f4f5edb8d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'completed')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
