from django.conf import settings


def resolver_tienda_id(request) -> str:
    """
    Determina el tienda_id correspondiente a la solicitud actual.

    """
    return settings.TIENDA_ID_DEFAULT
