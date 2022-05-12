"""auto-test removed columns

Revision ID: f146c460282f
Revises: 853517a43a6e
Create Date: 2022-05-12 12:41:33.389070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f146c460282f'
down_revision = '853517a43a6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('posts', sa.Column('published', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
