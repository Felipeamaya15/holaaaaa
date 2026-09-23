from typing import List, Dict, Any, Optional

from apps.catalog.infrastructure.repositories import ProductRepository


class ListPublicProductsUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, tienda_id: str) -> List[Dict[str, Any]]:
        return self.repository.list_by_store(tienda_id, activo=True)

class GetPublicProductDetailUseCase:
    """Obtiene el detalle de un producto activo, identificado por su slug."""
 
    def __init__(self, repository: ProductRepository):
        self.repository = repository
 
    def execute(self, tienda_id: str, slug: str) -> Optional[Dict[str, Any]]:
        producto = self.repository.get_by_slug(tienda_id, slug)
        if producto is None or not producto.get("activo", False):
            return None
        return producto
