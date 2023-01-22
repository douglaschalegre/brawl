from sqlalchemy.orm import Session

from category.models import Category

class CategoryRepository:
    @staticmethod
    def find_all(db: Session) -> list[Category]:
        return db.query(Category).all()

    @staticmethod
    def save(db: Session, Category: Category) -> Category:
        if Category.id:
            db.merge(Category)
        else:
            db.add(Category)
        db.commit()
        return Category

    @staticmethod
    def find_by_id(db: Session, id: int) -> Category:
        return db.query(Category).filter(Category.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Category).filter(Category.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        Category = db.query(Category).filter(Category.id == id).first()
        if Category is not None:
            db.delete(Category)
            db.commit()
