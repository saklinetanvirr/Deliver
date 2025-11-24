import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from customer.models import Customer

client = APIClient()

@pytest.mark.django_db
def test_get_customers():
    Customer.objects.create(name="Test", email="test@example.com")

    response = client.get("/customers/")
    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_create_customer():
    data = {"name": "Tanvir", "email": "tanvir@example.com"}

    response = client.post("/customers/", data, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Tanvir"
