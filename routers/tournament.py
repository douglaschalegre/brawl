from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from database import get_db
from tournament.models import Tournament
from tournament.repositories import TournamentRepository
from tournament.schemas import TournamentRequest, TournamentResponse

from fastapi import APIRouter

router = APIRouter()


@router.post("/api/tournaments", response_model=TournamentResponse, status_code=status.HTTP_201_CREATED)
def create_tournament(request: TournamentRequest, db: Session = Depends(get_db)):
    tournament = TournamentRepository.save(db, Tournament(**request.dict()))
    return TournamentResponse.from_orm(tournament)

@router.get("/api/tournaments", response_model=list[TournamentResponse])
def find_all_tournaments(db: Session = Depends(get_db)):
    tournaments = TournamentRepository.find_all(db)
    return [TournamentResponse.from_orm(tournament) for tournament in tournaments]

@router.get("/api/tournaments/{id}", response_model=TournamentResponse)
def find_tournament_by_id(id: int, db: Session = Depends(get_db)):
    tournament = TournamentRepository.find_by_id(db, id)
    if not tournament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )
    return TournamentResponse.from_orm(tournament)

@router.delete("/api/tournaments/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tournament_by_id(id: int, db: Session = Depends(get_db)):
    if not TournamentRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )
    TournamentRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/api/tournaments/{id}", response_model=TournamentResponse)
def update_tournament(id: int, request: TournamentRequest, db: Session = Depends(get_db)):
    if not TournamentRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )
    tournament = TournamentRepository.save(db, Tournament(id=id, **request.dict()))
    return TournamentResponse.from_orm(tournament)
