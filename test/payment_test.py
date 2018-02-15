import unittest
from app.payment import Payment

class TestSuite(unittest.TestCase):

  def test_payment_day_shift(self):
    payment = Payment()
    payment.hours_worked = 60
    payment.shift = "diurno"

    self.assertEqual(payment.getTotal(), 4550)

  def test_payment_night_shift(self):
    payment = Payment()
    payment.hours_worked = 50
    payment.shift = "nocturno"
    
    self.assertEqual(payment.getTotal(), 3550)

  def test_payment_mixed_shift(self):
    payment = Payment()
    payment.hours_worked = 46
    payment.shift = "mixto"
    
    self.assertEqual(payment.getTotal(), 2725)
