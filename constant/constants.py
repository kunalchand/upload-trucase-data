class GeneralConstants:
    ID = "id"
    NAME = "name"
    CATEGORY = "category"
    DESCRIPTION = "description"


class ModelConstants:
    SKILL_BUCKET_MODEL = "SkillBucketModel"


class RepositoryConstants:
    SKILL_BUCKET_REPOSITORY = "SkillBucketRepository"


class SchemaConstants:
    CLAIMS_CORE_SCHEMA = "claims_core"


class TableConstants:
    SKILL_BUCKET_TABLE = "skill_bucket"


class SQLConstants:
    SELECT_FROM_CLAIMS_CORE_SKILL_BUCKET = f"SELECT {GeneralConstants.ID}, {GeneralConstants.NAME}, {GeneralConstants.CATEGORY}, {GeneralConstants.DESCRIPTION} FROM {SchemaConstants.CLAIMS_CORE_SCHEMA}.{TableConstants.SKILL_BUCKET_TABLE};"
