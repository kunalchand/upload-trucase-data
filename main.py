from db_config import DatabaseConnection
from repository.skill_bucket_repository import SkillBucketRepository


def display_skill_buckets(users):
    for user in users:
        print(user)


def main():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        repo = UserRepository(conn)
        skill_buckets = repo.fetch_all()
        display_skill_buckets(skill_buckets)
    finally:
        db.close()


if __name__ == "__main__":
    main()
