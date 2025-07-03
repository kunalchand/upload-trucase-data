import os
from model.skill_bucket_model import SkillBucketModel
from constant.constants import GeneralConstants
from utils.json_loader import JsonLoader


class SkillBucketService:
    def __init__(self, repository):
        self.repository = repository

    def load_and_insert_skill_buckets(self, file_path):
        records = JsonLoader.load_json(file_path)
        skill_buckets = [
            SkillBucketModel(
                None,
                r[GeneralConstants.NAME],
                r[GeneralConstants.CATEGORY],
                r[GeneralConstants.DESCRIPTION],
            )
            for r in records
        ]
        self.repository.insert_many(skill_buckets)
