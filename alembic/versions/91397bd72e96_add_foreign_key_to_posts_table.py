"""add foreign key to posts table

Revision ID: 91397bd72e96
Revises: bffa4d43248d
Create Date: 2022-05-12 11:39:12.131979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91397bd72e96'
down_revision = 'bffa4d43248d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"],
                          remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
