from typing import List, Dict, Any

from apps.catalog.infrastructure.repositories import ProductRepository


class ListPublicProductsUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, tienda_id: str) -> List[Dict[str, Any]]:
        return self.repository.list_by_store(tienda_id, activo=True)
