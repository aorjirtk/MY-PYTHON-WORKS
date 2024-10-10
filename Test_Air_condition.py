import unittest
import ac
from ac.air_condition import Air_Condition

class Air_Condition_test(unittest.TestCase):

    def setUp(self):
        self.ac = Air_Condition()

    def test_ac_default_state_is_off(self):
        self.assertFalse(self.ac.ac_is_on())

    def test_ac_can_turn_on(self):
        self.ac.turn_on_ac()
        self.assertTrue(self.ac.ac_is_on())

    def test_ac_can_turn_off(self):
        self.ac.turn_on_ac()
        self.ac.ac_is_off()
        self.assertFalse(self.ac.ac_is_on())

    def test_default_ac_temperature_is_zero(self):
        self.ac.turn_on_ac()
        self.assertEqual(self.ac.get_temperature(), 16)

    def test_ac_can_increase_temperature(self):
        self.ac.turn_on_ac()
        self.ac.increase_temperature()
        self.ac.increase_temperature()
        self.assertEqual(self.ac.get_temperature(), 18)

    def test_ac_can_decrease_temperature(self):
        self.ac.turn_on_ac()
        self.ac.increase_temperature()
        self.ac.increase_temperature()
        self.ac.decrease_temperature()
        self.assertEqual(self.ac.get_temperature(), 17)

    def test_ac_cannot_increase_temperature_or_decrease_temperature_when_ac_is_off(self):
        self.assertFalse(self.ac.ac_is_on())
        self.ac.increase_temperature()
        self.ac.increase_temperature()
        self.ac.turn_on_ac()
        self.assertEqual(self.ac.get_temperature(),16)

    def test_ac_default_fan_speed_is_one(self):
        self.ac.turn_on_ac()
        self.assertEqual(self.ac.get_fan_speed(), 1)

    def test_ac_can_increase_fan_speed_is_one(self):
        self.ac.turn_on_ac()
        self.ac.increase_fan_speed()
        self.ac.increase_fan_speed()
        self.assertEqual(self.ac.get_fan_speed(), 3)

    def test_television_can_decrease_volume(self):
        self.ac.turn_on_ac()
        self.ac.increase_fan_speed()
        self.ac.increase_fan_speed()
        self.ac.increase_fan_speed()
        self.ac.decrease_fan_speed()
        self.assertEqual(self.ac.get_fan_speed(), 3)

    def test_ac_cannot_increase_or_decrease_fan_speed_when_ac_is_off(self):
        self.assertFalse(self.ac.ac_is_on())
        self.ac.increase_fan_speed()
        self.ac.increase_fan_speed()
        self.ac.turn_on_ac()
        self.assertEqual(self.ac.get_fan_speed(),1)

if __name__ == '__main__':
    unittest.main()


