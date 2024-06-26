"""empty message

Revision ID: 4f20385f17dc
Revises: e5f78226965b
Create Date: 2024-06-24 00:24:26.590094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f20385f17dc'
down_revision = 'e5f78226965b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=100), nullable=False))
        batch_op.drop_column('city')
        batch_op.drop_column('country')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('city', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
        batch_op.drop_column('location')

    # ### end Alembic commands ###
