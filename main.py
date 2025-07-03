import os
from config.db_config import DatabaseConnection
from repository.skill_bucket_repository import SkillBucketRepository
from service.skill_bucket_service import SkillBucketService
from constant.constants import DataConstants


def display_skill_buckets(users):
    for user in users:
        print(user)


def main():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        skill_bucket_repo = SkillBucketRepository(conn)
        skill_bucket_service = SkillBucketService(skill_bucket_repo)

        # Insert data from JSON
        file_path = os.path.join(
            DataConstants.DATA, DataConstants.SKILL_BUCKET_DATA_JSON
        )
        skill_bucket_service.load_and_insert_skill_buckets(file_path)

        # Fetch and display inserted data
        skill_buckets = skill_bucket_repo.fetch_all()
        display_skill_buckets(skill_buckets)

    finally:
        db.close()


if __name__ == "__main__":
    main()
