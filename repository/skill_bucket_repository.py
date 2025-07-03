from model.skill_bucket_model import SkillBucketModel
from constant.constants import SQLConstants


class SkillBucketRepository:
    def __init__(self, connection):
        self.connection = connection

    def fetch_all(self):
        cursor = self.connection.cursor()
        cursor.execute(SQLConstants.SELECT_FROM_CLAIMS_CORE_SKILL_BUCKET)
        rows = cursor.fetchall()
        return [SkillBucketModel(*row) for row in rows]

    def insert_many(self, skill_buckets):
        cursor = self.connection.cursor()
        for bucket in skill_buckets:
            cursor.execute(
                SQLConstants.INSERT_INTO_CLAIMS_CORE_SKILL_BUCKET,
                (bucket.name, bucket.category, bucket.description),
            )
        self.connection.commit()
