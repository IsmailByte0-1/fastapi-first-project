"""add content column to posts table

Revision ID: a54f40679115
Revises: 54df3b489050
Create Date: 2026-09-12 13:07:20.132268

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a54f40679115'
down_revision: Union[str, Sequence[str], None] = '54df3b489050'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
