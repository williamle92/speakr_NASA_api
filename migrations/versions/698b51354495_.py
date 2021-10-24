"""empty message

Revision ID: 698b51354495
Revises: b1a16eb1429b
Create Date: 2021-10-24 02:28:52.290729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '698b51354495'
down_revision = 'b1a16eb1429b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('picture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('picture')
    # ### end Alembic commands ###
