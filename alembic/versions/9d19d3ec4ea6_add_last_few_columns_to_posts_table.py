""" add last few columns to posts table 

Revision ID: 9d19d3ec4ea6
Revises: 8b0cc1b91f57
Create Date: 2026-09-12 15:35:37.676800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d19d3ec4ea6'
down_revision: Union[str, Sequence[str], None] = '8b0cc1b91f57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column('posts', sa.Column('created_at',
    sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
