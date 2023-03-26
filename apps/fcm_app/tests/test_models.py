from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.common.test_data import user_data, device_data
from apps.fcm_app.models import FCMDevice, DeviceType


class FCMDeviceModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(**user_data)
        self.device = FCMDevice.objects.create(user=self.user, **device_data)

    def test_device_creation(self):
        self.assertEqual(self.device.name, device_data["name"])
        self.assertEqual(self.device.device_id, device_data["device_id"])
        self.assertEqual(self.device.registration_id, device_data["registration_id"])
        self.assertEqual(self.device.type, device_data["type"])
        self.assertTrue(self.device.active)

    def test_device_string_representation(self):
        self.assertEqual(self.device.__str__(), self.device.name)

    def test_inactive_device(self):
        device = FCMDevice.objects.create(user=self.user, **device_data, active=False)
        self.assertFalse(device.active)

    def test_device_type_choices(self):
        self.assertEqual(DeviceType.IOS, "ios")
        self.assertEqual(DeviceType.WEB, "web")
        self.assertEqual(DeviceType.ANDROID, "android")

    def test_field_indexing(self):
        self.assertQuerysetEqual(
            FCMDevice.objects.filter(device_id=self.device.device_id),
            [repr(self.device)], transform=repr)
