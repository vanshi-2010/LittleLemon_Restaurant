from django.test import TestCase
from restaurant.models import Menu, Booking
from django.utils import timezone
from django.forms import ValidationError

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=4.25, inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 4.25")

#TestCase class
class BookingModelTests(TestCase):

    def setUp(self):
        self.booking_date = timezone.now()

    def test_create_booking(self):
        booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=4,
            booking_date=self.booking_date
        )
        self.assertEqual(booking.name, 'John Doe')
        self.assertEqual(booking.no_of_guests, 4)
        self.assertEqual(booking.booking_date, self.booking_date)
        self.assertEqual(str(booking), f'Booking for John Doe on {str(self.booking_date)} for 4')

    def test_booking_no_of_guests_validation(self):
        with self.assertRaises(ValidationError):
            booking = Booking(
                name='John Doe',
                no_of_guests=1000000,  # Exceeds MaxValueValidator
                booking_date=self.booking_date
            )
            booking.full_clean()  # This will trigger the validation

        with self.assertRaises(ValidationError):
            booking = Booking(
                name='John Doe',
                no_of_guests=-1000000,  # Exceeds MinValueValidator
                booking_date=self.booking_date
            )
            booking.full_clean()  # This will trigger the validation

    def test_booking_date_field(self):
        booking = Booking(
            name='Jane Doe',
            no_of_guests=3,
            booking_date=self.booking_date
        )
        booking.save()
        self.assertEqual(booking.booking_date, self.booking_date)