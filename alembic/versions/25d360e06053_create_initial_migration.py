"""create initial migration

Revision ID: 25d360e06053
Revises:
Create Date: 2025-04-30 00:31:07.987088
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '25d360e06053'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE part (
            id SERIAL PRIMARY KEY,
            name VARCHAR(256),
            sku VARCHAR(256),
            description VARCHAR(1024),
            weight_ounces INTEGER,
            is_active BOOLEAN
        );
        INSERT INTO part (name, sku, description, weight_ounces, is_active)
        VALUES
        ('Heavy coil', 'SDJDDH8223DHJ', 'Tightly wound nickel-gravy alloy spring', 22, true),
        ('Reverse lever', 'DCMM39823DSJD', 'Attached to provide inverse leverage', 9, false),
        ('Macrochip', 'OWDD823011DJSD', 'Used for heavy-load computing', 2, true);
    """)


def downgrade() -> None:
    op.execute("DROP TABLE part")
