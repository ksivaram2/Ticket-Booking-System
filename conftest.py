import pytest
import tempfile
import shutil

from ticket_booking.services.auth_service import AuthService
from ticket_booking.services.event_service import EventService
from ticket_booking.services.booking_service import BookingService
from ticket_booking.services.report_service import ReportService
from ticket_booking.storage.file_storage import FileStorage

@pytest.fixture
def temp_data_dir():
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)

@pytest.fixture
def storage_fixture(temp_data_dir):
    return FileStorage(base_dir=temp_data_dir)

@pytest.fixture
def auth_service_fixture(storage_fixture):
    return AuthService(storage_fixture)

@pytest.fixture
def event_service_fixture(storage_fixture):
    return EventService(storage_fixture)

@pytest.fixture
def booking_service_fixture(storage_fixture, event_service_fixture, auth_service_fixture):
    return BookingService(storage_fixture, event_service_fixture, auth_service_fixture)

@pytest.fixture
def report_service_fixture(storage_fixture):
    return ReportService(storage_fixture)
