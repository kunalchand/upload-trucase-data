from config.db_config import DatabaseConnection
from repository.skill_bucket_repository import SkillBucketRepository


def display_skill_buckets(users):
    for user in users:
        print(user)


def main():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        skill_bucket_repo = SkillBucketRepository(conn)
        skill_buckets = skill_bucket_repo.fetch_all()
        display_skill_buckets(skill_buckets)
    finally:
        db.close()


if __name__ == "__main__":
    main()
