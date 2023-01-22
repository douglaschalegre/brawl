from sqlalchemy.orm import Session

from tournament.models import Tournament

class TournamentRepository:
    @staticmethod
    def find_all(db: Session) -> list[Tournament]:
        return db.query(Tournament).all()

    @staticmethod
    def save(db: Session, Tournament: Tournament) -> Tournament:
        if Tournament.id:
            db.merge(Tournament)
        else:
            db.add(Tournament)
        db.commit()
        return Tournament

    @staticmethod
    def find_by_id(db: Session, id: int) -> Tournament:
        return db.query(Tournament).filter(Tournament.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Tournament).filter(Tournament.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        Tournament = db.query(Tournament).filter(Tournament.id == id).first()
        if Tournament is not None:
            db.delete(Tournament)
            db.commit()
