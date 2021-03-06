"""translation and note fields in word model

Revision ID: a81a75426c82
Revises: 8f467faa35b8
Create Date: 2018-11-10 23:39:59.196765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a81a75426c82'
down_revision = '8f467faa35b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('word', sa.Column('note', sa.String(length=256), nullable=True))
    op.add_column('word', sa.Column('translation', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('word', 'translation')
    op.drop_column('word', 'note')
    # ### end Alembic commands ###
