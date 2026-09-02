"""migrate ids to uuid

Revision ID: b8d6b6c99390
Revises:
Create Date: 2026-08-25
"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b8d6b6c99390"
down_revision: Union[str, Sequence[str], None] = None
branch_labels = None
depends_on = None


def _drop_primary_key(table_name: str) -> None:
    """Drop the existing primary key without depending on pgloader's name."""
    op.execute(f"""
        DO $$
        DECLARE
            constraint_name text;
        BEGIN
            SELECT conname
            INTO constraint_name
            FROM pg_constraint
            WHERE conrelid = '{table_name}'::regclass
              AND contype = 'p';

            IF constraint_name IS NOT NULL THEN
                EXECUTE format(
                    'ALTER TABLE {table_name} DROP CONSTRAINT %I',
                    constraint_name
                );
            END IF;
        END $$;
        """)


def upgrade() -> None:
    # ================================================================
    # 1. Generate UUID mappings
    # ================================================================

    op.execute("""
        CREATE EXTENSION IF NOT EXISTS pgcrypto
    """)

    op.execute("""
        CREATE TEMP TABLE id_mapping_actors AS
        SELECT id AS old_id, gen_random_uuid() AS new_id
        FROM actors
    """)

    op.execute("""
        CREATE TEMP TABLE id_mapping_characters AS
        SELECT id AS old_id, gen_random_uuid() AS new_id
        FROM characters
    """)

    op.execute("""
        CREATE TEMP TABLE id_mapping_catchphrases AS
        SELECT id AS old_id, gen_random_uuid() AS new_id
        FROM catchphrases
    """)

    op.execute("""
        CREATE TEMP TABLE id_mapping_episodes AS
        SELECT id AS old_id, gen_random_uuid() AS new_id
        FROM episodes
    """)

    op.execute("""
        CREATE TEMP TABLE id_mapping_quotes AS
        SELECT id AS old_id, gen_random_uuid() AS new_id
        FROM quotes
    """)

    op.execute("""
        CREATE TEMP TABLE id_mapping_seasons AS
        SELECT id AS old_id, gen_random_uuid() AS new_id
        FROM seasons
    """)

    # ================================================================
    # 2. Add temporary UUID columns
    # ================================================================

    op.execute("""
        ALTER TABLE actors
        ADD COLUMN new_id UUID
    """)

    op.execute("""
        ALTER TABLE characters
        ADD COLUMN new_id UUID,
        ADD COLUMN new_actor_id UUID
    """)

    op.execute("""
        ALTER TABLE catchphrases
        ADD COLUMN new_id UUID,
        ADD COLUMN new_character_id UUID
    """)

    op.execute("""
        ALTER TABLE episodes
        ADD COLUMN new_id UUID,
        ADD COLUMN new_season_id UUID
    """)

    op.execute("""
        ALTER TABLE quotes
        ADD COLUMN new_id UUID,
        ADD COLUMN new_character_id UUID,
        ADD COLUMN new_episode_id UUID
    """)

    op.execute("""
        ALTER TABLE seasons
        ADD COLUMN new_id UUID,
        ADD COLUMN new_most_watched_episode_id UUID
    """)

    # ================================================================
    # 3. Populate UUID columns
    # ================================================================

    op.execute("""
        UPDATE actors a
        SET new_id = m.new_id
        FROM id_mapping_actors m
        WHERE a.id = m.old_id
    """)

    op.execute("""
        UPDATE characters c
        SET new_id = m.new_id
        FROM id_mapping_characters m
        WHERE c.id = m.old_id
    """)

    op.execute("""
        UPDATE catchphrases c
        SET new_id = m.new_id
        FROM id_mapping_catchphrases m
        WHERE c.id = m.old_id
    """)

    op.execute("""
        UPDATE episodes e
        SET new_id = m.new_id
        FROM id_mapping_episodes m
        WHERE e.id = m.old_id
    """)

    op.execute("""
        UPDATE quotes q
        SET new_id = m.new_id
        FROM id_mapping_quotes m
        WHERE q.id = m.old_id
    """)

    op.execute("""
        UPDATE seasons s
        SET new_id = m.new_id
        FROM id_mapping_seasons m
        WHERE s.id = m.old_id
    """)

    # ================================================================
    # 4. Convert foreign-key values
    # ================================================================

    op.execute("""
        UPDATE characters c
        SET new_actor_id = m.new_id
        FROM id_mapping_actors m
        WHERE c.actor_id = m.old_id
    """)

    op.execute("""
        UPDATE catchphrases cp
        SET new_character_id = m.new_id
        FROM id_mapping_characters m
        WHERE cp.character_id = m.old_id
    """)

    op.execute("""
        UPDATE episodes e
        SET new_season_id = m.new_id
        FROM id_mapping_seasons m
        WHERE e.season_id = m.old_id
    """)

    op.execute("""
        UPDATE quotes q
        SET new_character_id = m.new_id
        FROM id_mapping_characters m
        WHERE q.character_id = m.old_id
    """)

    op.execute("""
        UPDATE quotes q
        SET new_episode_id = m.new_id
        FROM id_mapping_episodes m
        WHERE q.episode_id = m.old_id
    """)

    op.execute("""
        UPDATE seasons s
        SET new_most_watched_episode_id = m.new_id
        FROM id_mapping_episodes m
        WHERE s.most_watched_episode_id = m.old_id
    """)

    # ================================================================
    # 5. Remove indexes on foreign keys
    #
    # pgloader generates different index names, so find them by
    # column rather than assuming a specific name.
    # ================================================================

    op.execute("""
        DO $$
        DECLARE
            index_name text;
        BEGIN
            FOR index_name IN
                SELECT indexrelname
                FROM pg_stat_user_indexes
                WHERE relname = 'characters'
                  AND indexrelname LIKE '%actor_id%'
            LOOP
                EXECUTE format('DROP INDEX IF EXISTS %I', index_name);
            END LOOP;
        END $$;
    """)

    op.execute("""
        DO $$
        DECLARE
            index_name text;
        BEGIN
            FOR index_name IN
                SELECT indexrelname
                FROM pg_stat_user_indexes
                WHERE relname = 'catchphrases'
                  AND indexrelname LIKE '%character_id%'
            LOOP
                EXECUTE format('DROP INDEX IF EXISTS %I', index_name);
            END LOOP;
        END $$;
    """)

    op.execute("""
        DO $$
        DECLARE
            index_name text;
        BEGIN
            FOR index_name IN
                SELECT indexrelname
                FROM pg_stat_user_indexes
                WHERE relname = 'episodes'
                  AND indexrelname LIKE '%season_id%'
            LOOP
                EXECUTE format('DROP INDEX IF EXISTS %I', index_name);
            END LOOP;
        END $$;
    """)

    op.execute("""
        DO $$
        DECLARE
            index_name text;
        BEGIN
            FOR index_name IN
                SELECT indexrelname
                FROM pg_stat_user_indexes
                WHERE relname = 'quotes'
                  AND (
                      indexrelname LIKE '%character_id%'
                      OR indexrelname LIKE '%episode_id%'
                  )
            LOOP
                EXECUTE format('DROP INDEX IF EXISTS %I', index_name);
            END LOOP;
        END $$;
    """)

    # ================================================================
    # 6. Remove primary keys
    #
    # IMPORTANT:
    # We do not assume pgloader's constraint names.
    # ================================================================

    _drop_primary_key("actors")
    _drop_primary_key("characters")
    _drop_primary_key("catchphrases")
    _drop_primary_key("episodes")
    _drop_primary_key("quotes")
    _drop_primary_key("seasons")

    # ================================================================
    # 7. Drop old ID/FK columns
    # ================================================================

    op.execute("""
        ALTER TABLE characters
        DROP COLUMN id,
        DROP COLUMN actor_id
    """)

    op.execute("""
        ALTER TABLE catchphrases
        DROP COLUMN id,
        DROP COLUMN character_id
    """)

    op.execute("""
        ALTER TABLE episodes
        DROP COLUMN id,
        DROP COLUMN season_id
    """)

    op.execute("""
        ALTER TABLE quotes
        DROP COLUMN id,
        DROP COLUMN character_id,
        DROP COLUMN episode_id
    """)

    op.execute("""
        ALTER TABLE seasons
        DROP COLUMN id,
        DROP COLUMN most_watched_episode_id
    """)

    op.execute("""
        ALTER TABLE actors
        DROP COLUMN id
    """)

    # ================================================================
    # 8. Rename UUID columns
    # ================================================================

    op.execute("""
        ALTER TABLE actors
        RENAME COLUMN new_id TO id
    """)

    op.execute("""
        ALTER TABLE characters
        RENAME COLUMN new_id TO id
    """)

    op.execute("""
        ALTER TABLE characters
        RENAME COLUMN new_actor_id TO actor_id
    """)

    op.execute("""
        ALTER TABLE catchphrases
        RENAME COLUMN new_id TO id
    """)

    op.execute("""
        ALTER TABLE catchphrases
        RENAME COLUMN new_character_id TO character_id
    """)

    op.execute("""
        ALTER TABLE episodes
        RENAME COLUMN new_id TO id
    """)

    op.execute("""
        ALTER TABLE episodes
        RENAME COLUMN new_season_id TO season_id
    """)

    op.execute("""
        ALTER TABLE quotes
        RENAME COLUMN new_id TO id
    """)

    op.execute("""
        ALTER TABLE quotes
        RENAME COLUMN new_character_id TO character_id
    """)

    op.execute("""
        ALTER TABLE quotes
        RENAME COLUMN new_episode_id TO episode_id
    """)

    op.execute("""
        ALTER TABLE seasons
        RENAME COLUMN new_id TO id
    """)

    op.execute("""
        ALTER TABLE seasons
        RENAME COLUMN new_most_watched_episode_id
        TO most_watched_episode_id
    """)

    # ================================================================
    # 9. Remove quotes.date
    # ================================================================

    op.execute("""
        ALTER TABLE quotes
        DROP COLUMN IF EXISTS date
    """)

    # ================================================================
    # 10. Add primary keys
    # ================================================================

    op.execute("""
        ALTER TABLE actors
        ADD CONSTRAINT actors_pkey PRIMARY KEY (id)
    """)

    op.execute("""
        ALTER TABLE characters
        ADD CONSTRAINT characters_pkey PRIMARY KEY (id)
    """)

    op.execute("""
        ALTER TABLE catchphrases
        ADD CONSTRAINT catchphrases_pkey PRIMARY KEY (id)
    """)

    op.execute("""
        ALTER TABLE episodes
        ADD CONSTRAINT episodes_pkey PRIMARY KEY (id)
    """)

    op.execute("""
        ALTER TABLE quotes
        ADD CONSTRAINT quotes_pkey PRIMARY KEY (id)
    """)

    op.execute("""
        ALTER TABLE seasons
        ADD CONSTRAINT seasons_pkey PRIMARY KEY (id)
    """)

    # ================================================================
    # 11. Add foreign keys
    # ================================================================

    op.create_foreign_key(
        "fk_characters_actor",
        "characters",
        "actors",
        ["actor_id"],
        ["id"],
    )

    op.create_foreign_key(
        "fk_catchphrases_character",
        "catchphrases",
        "characters",
        ["character_id"],
        ["id"],
    )

    op.create_foreign_key(
        "fk_episodes_season",
        "episodes",
        "seasons",
        ["season_id"],
        ["id"],
    )

    op.create_foreign_key(
        "fk_quotes_character",
        "quotes",
        "characters",
        ["character_id"],
        ["id"],
    )

    op.create_foreign_key(
        "fk_quotes_episode",
        "quotes",
        "episodes",
        ["episode_id"],
        ["id"],
    )

    op.create_foreign_key(
        "fk_seasons_most_watched_episode",
        "seasons",
        "episodes",
        ["most_watched_episode_id"],
        ["id"],
    )

    # ================================================================
    # 12. Add indexes
    # ================================================================

    op.create_index("ix_actors_id", "actors", ["id"])
    op.create_index("ix_characters_id", "characters", ["id"])
    op.create_index("ix_catchphrases_id", "catchphrases", ["id"])
    op.create_index("ix_episodes_id", "episodes", ["id"])
    op.create_index("ix_quotes_id", "quotes", ["id"])
    op.create_index("ix_seasons_id", "seasons", ["id"])

    op.create_index(
        "ix_characters_actor_id",
        "characters",
        ["actor_id"],
    )

    op.create_index(
        "ix_catchphrases_character_id",
        "catchphrases",
        ["character_id"],
    )

    op.create_index(
        "ix_episodes_season_id",
        "episodes",
        ["season_id"],
    )

    op.create_index(
        "ix_quotes_character_id",
        "quotes",
        ["character_id"],
    )

    op.create_index(
        "ix_quotes_episode_id",
        "quotes",
        ["episode_id"],
    )

    # ================================================================
    # 13. Quote uniqueness
    # ================================================================

    op.create_unique_constraint(
        "uq_quote",
        "quotes",
        ["quote", "episode_id", "character_id"],
    )


def downgrade() -> None:
    raise NotImplementedError("Downgrade from UUID to BIGINT is not supported.")
