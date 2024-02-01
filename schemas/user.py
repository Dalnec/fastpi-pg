from pydantic import BaseModel


class ItemBaseSchema(BaseModel):
    title: str
    description: str | None = None


class ItemCreateSchema(ItemBaseSchema):
    pass


class ItemSchema(ItemBaseSchema):
    id: int
    owner_id: int

    class ConfigSchema:
        orm_mode = True


class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool
    items: list[ItemSchema] = []

    class ConfigSchema:
        orm_mode = True