from model.skill_bucket_model import SkillBucketModel
from constant.constants import SQLConstants


class SkillBucketRepository:
    def __init__(self, connection):
        self.connection = connection

    def fetch_all(self):
        cursor = self.connection.cursor()
        cursor.execute(SQLConstants.SELECT_FROM_SKILL_BUCKET)
        rows = cursor.fetchall()
        return [SkillBucketModel(*row) for row in rows]
