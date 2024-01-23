from app.ciim.client import ClientAPI
from django.conf import settings


def get_records_client():
    return ClientAPI(
        base_url=settings.KONG_API_URL,
        api_key=settings.KONG_API_KEY,
        verify_certificates=settings.KONG_API_VERIFY_CERTIFICATES,
    )


records_client = get_records_client()
