"""Create usage_stats table

Revision ID: ca1ac51334ec
Revises: initial_migration
Create Date: 2024-08-05 21:50:30.028279

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "ca1ac51334ec"
down_revision = "initial_migration"  # Set the correct previous migration
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "usage_stats",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("provider_name", sa.String(), nullable=True),
        sa.Column("model", sa.String(), nullable=True),
        sa.Column("request_count", sa.Integer(), nullable=True),
        sa.Column("success_count", sa.Integer(), nullable=True),
        sa.Column("prompt_tokens", sa.Integer(), nullable=True),
        sa.Column("completion_tokens", sa.Integer(), nullable=True),
        sa.Column("error_count", sa.Integer(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_usage_stats_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_usage_stats")),
    )
    op.create_index(op.f("ix_usage_stats_id"), "usage_stats", ["id"], unique=False)
    op.create_index(
        op.f("ix_usage_stats_user_id"), "usage_stats", ["user_id"], unique=False
    )
    op.create_index(
        op.f("ix_usage_stats_provider_name"),
        "usage_stats",
        ["provider_name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_usage_stats_model"), "usage_stats", ["model"], unique=False
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_usage_stats_model"), table_name="usage_stats")
    op.drop_index(op.f("ix_usage_stats_provider_name"), table_name="usage_stats")
    op.drop_index(op.f("ix_usage_stats_user_id"), table_name="usage_stats")
    op.drop_index(op.f("ix_usage_stats_id"), table_name="usage_stats")
    op.drop_table("usage_stats")
    # ### end Alembic commands ###
