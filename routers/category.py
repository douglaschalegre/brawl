from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from database import get_db
from category.repositories import CategoryRepository
from category.schemas import CategoryRequest, CategoryResponse

from fastapi import APIRouter

router = APIRouter()


@router.post("/api/categorys", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(request: CategoryRequest, db: Session = Depends(get_db)):
    Category = CategoryRepository.save(db, Category(**request.dict()))
    return CategoryResponse.from_orm(Category)

@router.get("/api/categorys", response_model=list[CategoryResponse])
def find_all_categories(db: Session = Depends(get_db)):
    Categorys = CategoryRepository.find_all(db)
    return [CategoryResponse.from_orm(Category) for Category in Categorys]

@router.get("/api/categorys/{id}", response_model=CategoryResponse)
def find_category_by_id(id: int, db: Session = Depends(get_db)):
    Category = CategoryRepository.find_by_id(db, id)
    if not Category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )
    return CategoryResponse.from_orm(Category)

@router.delete("/api/categorys/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category_by_id(id: int, db: Session = Depends(get_db)):
    if not CategoryRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )
    CategoryRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/api/categorys/{id}", response_model=CategoryResponse)
def update_category(id: int, request: CategoryRequest, db: Session = Depends(get_db)):
    if not CategoryRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )
    Category = CategoryRepository.save(db, Category(id=id, **request.dict()))
    return CategoryResponse.from_orm(Category)
