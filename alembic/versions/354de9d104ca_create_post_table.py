"""create post table

Revision ID: 354de9d104ca
Revises: 
Create Date: 2022-05-11 21:36:34.887656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '354de9d104ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
                    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
