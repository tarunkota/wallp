"""add table search_page_num

Revision ID: 25eef620cf9e
Revises: 75b54db3960d
Create Date: 2016-03-24 16:12:36.071351

"""

# revision identifiers, used by Alembic.
revision = '25eef620cf9e'
down_revision = '75b54db3960d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search_page_num',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group', sa.String(length=20), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('value', sa.String(length=512), nullable=True),
    sa.Column('type', sa.String(length=15), nullable=True),
    sa.PrimaryKeyconstraint('id'),
    sa.UniqueConstraint('group', 'name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search_page_num')
    ### end Alembic commands ###
