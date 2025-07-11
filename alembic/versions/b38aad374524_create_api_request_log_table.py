"""Create api_request_log table

Revision ID: b38aad374524
Revises: c50fd7be794c
Create Date: 2025-04-08 21:44:00.759874

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "b38aad374524"
down_revision = "c50fd7be794c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - START ###
    op.create_table(
        "api_request_log",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("provider_name", sa.String(), nullable=False),
        sa.Column("model", sa.String(), nullable=False),
        sa.Column("endpoint", sa.String(), nullable=False),
        sa.Column("request_timestamp", sa.DateTime(), nullable=False),
        sa.Column("input_tokens", sa.Integer(), nullable=True),
        sa.Column("output_tokens", sa.Integer(), nullable=True),
        sa.Column("total_tokens", sa.Integer(), nullable=True),
        sa.Column("cost", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_api_request_log_user_time",
        "api_request_log",
        ["user_id", "request_timestamp"],
        unique=False,
    )
    op.create_index(
        op.f("ix_api_request_log_endpoint"),
        "api_request_log",
        ["endpoint"],
        unique=False,
    )
    op.create_index(
        op.f("ix_api_request_log_model"), "api_request_log", ["model"], unique=False
    )
    op.create_index(
        op.f("ix_api_request_log_provider_name"),
        "api_request_log",
        ["provider_name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_api_request_log_request_timestamp"),
        "api_request_log",
        ["request_timestamp"],
        unique=False,
    )
    op.create_index(
        op.f("ix_api_request_log_user_id"), "api_request_log", ["user_id"], unique=False
    )
    # op.drop_constraint(None, 'usage_stats', type_='foreignkey') # REMOVED
    # op.create_foreign_key(None, 'usage_stats', 'users', ['user_id'], ['id'], ondelete='CASCADE') # REMOVED
    # op.drop_column('usage_stats', 'completion_tokens') # REMOVED
    # op.drop_column('usage_stats', 'timestamp') # REMOVED
    # op.drop_column('usage_stats', 'error_count') # REMOVED
    # op.drop_column('usage_stats', 'prompt_tokens') # REMOVED
    # op.drop_column('usage_stats', 'success_count') # REMOVED
    # op.drop_column('usage_stats', 'request_count') # REMOVED
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - START ###
    # op.add_column('usage_stats', sa.Column('request_count', sa.INTEGER(), nullable=True)) # REMOVED
    # op.add_column('usage_stats', sa.Column('success_count', sa.INTEGER(), nullable=True)) # REMOVED
    # op.add_column('usage_stats', sa.Column('prompt_tokens', sa.INTEGER(), nullable=True)) # REMOVED
    # op.add_column('usage_stats', sa.Column('error_count', sa.INTEGER(), nullable=True)) # REMOVED
    # op.add_column('usage_stats', sa.Column('timestamp', sa.DATETIME(), nullable=True)) # REMOVED
    # op.add_column('usage_stats', sa.Column('completion_tokens', sa.INTEGER(), nullable=True)) # REMOVED
    # op.drop_constraint(None, 'usage_stats', type_='foreignkey') # REMOVED
    # op.create_foreign_key(None, 'usage_stats', 'users', ['user_id'], ['id']) # REMOVED
    op.drop_index(op.f("ix_api_request_log_user_id"), table_name="api_request_log")
    op.drop_index(
        op.f("ix_api_request_log_request_timestamp"), table_name="api_request_log"
    )
    op.drop_index(
        op.f("ix_api_request_log_provider_name"), table_name="api_request_log"
    )
    op.drop_index(op.f("ix_api_request_log_model"), table_name="api_request_log")
    op.drop_index(op.f("ix_api_request_log_endpoint"), table_name="api_request_log")
    op.drop_index("ix_api_request_log_user_time", table_name="api_request_log")
    op.drop_table("api_request_log")
    # ### end Alembic commands ###
