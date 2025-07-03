from constant.constants import GeneralConstants, ModelConstants


class SkillBucketModel:
    def __init__(self, id, name, category, description):
        self.id = id
        self.name = name
        self.category = category
        self.description = description

    def __repr__(self):
        return f"{ModelConstants.SKILL_BUCKET_MODEL}({GeneralConstants.ID}={self.id}, {GeneralConstants.NAME}='{self.name}', {GeneralConstants.CATEGORY}='{self.category}', {GeneralConstants.DESCRIPTION}='{self.description}')\n"
