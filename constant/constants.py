class GeneralConstants:
    ID = "id"
    NAME = "name"
    CATEGORY = "category"
    DESCRIPTION = "description"


class ModelConstants:
    SKILL_BUCKET_MODEL = "SkillBucketModel"


class RepositoryConstants:
    SKILL_BUCKET_REPOSITORY = "SkillBucketRepository"


class TableConstants:
    SKILL_BUCKET_TABLE = "skill_bucket"


class SQLConstants:
    SELECT_FROM_SKILL_BUCKET = f"SELECT {GeneralConstants.ID}, {GeneralConstants.NAME}, {GeneralConstants.CATEGORY}, {GeneralConstants.DESCRIPTION} FROM {TableConstants.SKILL_BUCKET_TABLE};"
