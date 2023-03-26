from ..emails.enums import EmailType
from ..fcm_app.models import DeviceType

user_data = {
    "username": "Test",
    "password": "pass@1234"
}

device_data = {
    "name": "Test Device",
    "device_id": "test_device_id",
    "registration_id": "test_registration_id",
    "type": DeviceType.IOS
}

email_log_data = {
    "email_type": EmailType.PASSWORD_RESET,
    "email_content": {
        "data": {},
        "subject": "Your Untapped password was successfully changed!",
        "email_body": "Your Untapped password was successfully changed"}
}
