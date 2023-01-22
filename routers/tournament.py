from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from database import get_db
from tournament.repositories import TournamentRepository
from tournament.schemas import TournamentRequest, TournamentResponse

from fastapi import APIRouter

router = APIRouter()


@router.post("/api/Tournaments", response_model=TournamentResponse, status_code=status.HTTP_201_CREATED)
def create_tournament(request: TournamentRequest, db: Session = Depends(get_db)):
    Tournament = TournamentRepository.save(db, Tournament(**request.dict()))
    return TournamentResponse.from_orm(Tournament)

@router.get("/api/Tournaments", response_model=list[TournamentResponse])
def find_all_tournaments(db: Session = Depends(get_db)):
    Tournaments = TournamentRepository.find_all(db)
    return [TournamentResponse.from_orm(Tournament) for Tournament in Tournaments]

@router.get("/api/Tournaments/{id}", response_model=TournamentResponse)
def find_tournament_by_id(id: int, db: Session = Depends(get_db)):
    Tournament = TournamentRepository.find_by_id(db, id)
    if not Tournament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )
    return TournamentResponse.from_orm(Tournament)

@router.delete("/api/Tournaments/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tournament_by_id(id: int, db: Session = Depends(get_db)):
    if not TournamentRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )
    TournamentRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/api/Tournaments/{id}", response_model=TournamentResponse)
def update_tournament(id: int, request: TournamentRequest, db: Session = Depends(get_db)):
    if not TournamentRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )
    Tournament = TournamentRepository.save(db, Tournament(id=id, **request.dict()))
    return TournamentResponse.from_orm(Tournament)
