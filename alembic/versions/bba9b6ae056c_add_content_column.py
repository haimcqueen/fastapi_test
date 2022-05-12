"""add content column

Revision ID: bba9b6ae056c
Revises: 354de9d104ca
Create Date: 2022-05-11 21:50:54.796267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bba9b6ae056c'
down_revision = '354de9d104ca'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
