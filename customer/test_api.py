import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from customer.models import Customer

@pytest.mark.django_db
def test_get_customers():
    Customer.objects.create(name="Test User", email="test@example.com")
    
    client = APIClient()
    response = client.get("/api/customers/")

    assert response.status_code == 200
    assert len(response.data) == 1

