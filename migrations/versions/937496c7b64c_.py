"""empty message

Revision ID: 937496c7b64c
Revises: b80b555a167e
Create Date: 2018-12-28 04:55:32.115183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '937496c7b64c'
down_revision = 'b80b555a167e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('city', sa.String(length=50), nullable=True))
    op.add_column('member', sa.Column('country', sa.String(length=50), nullable=True))
    op.add_column('member', sa.Column('province', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('member', 'province')
    op.drop_column('member', 'country')
    op.drop_column('member', 'city')
    # ### end Alembic commands ###