"""initial migration

Revision ID: 165c1e45b251
Revises: 
Create Date: 2024-06-29 12:01:37.259644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '165c1e45b251'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
