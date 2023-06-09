"""adding columns date, alive, sold

Revision ID: 618c95d0af55
Revises: 62623810af74
Create Date: 2023-06-29 16:15:48.796670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '618c95d0af55'
down_revision = '62623810af74'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('records', sa.Column('date_of_birth', sa.Date(), nullable=True))
    op.add_column('records', sa.Column('date_purchased', sa.Date(), nullable=True))
    op.add_column('records', sa.Column('vaccination_info', sa.Text(), nullable=True))
    op.add_column('records', sa.Column('alive', sa.Boolean(), nullable=True))
    op.add_column('records', sa.Column('sold', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('records', 'sold')
    op.drop_column('records', 'alive')
    op.drop_column('records', 'vaccination_info')
    op.drop_column('records', 'date_purchased')
    op.drop_column('records', 'date_of_birth')
    # ### end Alembic commands ###
