import unittest
import television
from television.television import Television

class Television_test(unittest.TestCase):

    def setUp(self):
        self.television = Television()

    def test_television_is_off(self):
        self.assertFalse(self.television.television_is_on())

    def test_television_can_turn_on(self):
        self.television.turn_on_television()
        self.assertTrue(self.television.television_is_on())

    def test_television_can_turn_off(self):
        self.television.turn_on_television()
        self.television.television_is_off()
        self.assertFalse(self.television.television_is_on())

    def test_default_television_channel_zero(self):
        self.television.turn_on_television()
        self.assertEqual(self.television.get_channel(), 0)

    def test_television_can_channel_up(self):
        self.television.turn_on_television()
        self.television.channel_up()
        self.television.channel_up()
        self.assertEqual(self.television.get_channel(), 2)

    def test_television_can_channel_down(self):
        self.television.turn_on_television()
        self.television.channel_up()
        self.television.channel_up()
        self.television.channel_down()
        self.assertEqual(self.television.get_channel(), 1)

    def test_television_cannot_channel_up_or_down_when_television_is_off(self):
        self.assertFalse(self.television.television_is_on())
        self.television.channel_up()
        self.television.channel_up()
        self.television.turn_on_television()
        self.assertEqual(self.television.get_channel(),0)

    def test_television_default_volume_is_zero(self):
        self.television.turn_on_television()
        self.assertEqual(self.television.get_volume(), 0)

    def test_television_can_increase_volume(self):
        self.television.turn_on_television()
        self.television.volume_up()
        self.television.volume_up()
        self.assertEqual(self.television.get_volume(), 2)

    def test_television_can_decrease_volume(self):
        self.television.turn_on_television()
        self.television.volume_up()
        self.television.volume_up()
        self.television.volume_up()
        self.television.volume_down()
        self.assertEqual(self.television.get_volume(), 2)

    def test_television_cannot_increase_or_decrease_volume_when_television_is_off(self):
        self.assertFalse(self.television.television_is_on())
        self.television.volume_up()
        self.television.volume_up()
        self.assertEqual(self.television.get_volume(), 0)

    def test_television_can_set_volume_to_ten_and_volume_is_ten(self):
        self.television.turn_on_television()
        self.television.set_volume(10)
        self.assertEqual(self.television.get_volume(), 10)

    def test_when_television_is_mute_volume_is_zero(self):
        self.television.turn_on_television()
        self.television.volume_up()
        self.television.volume_up()
        self.television.volume_up()
        self.television.mute()
        self.assertEqual(self.television.get_volume(), 0)

    def test_when_television_is_unmute_volume_is_back_to_previous_volume_level(self):
        self.television.turn_on_television()
        self.television.volume_up()
        self.television.volume_up()
        self.television.volume_up()
        self.television.mute()
        self.television.unmute()
        self.assertEqual(self.television.get_volume(), 3)

    def test_when_television_is_off_mute_and_unmute_cannot_function(self):
        self.assertFalse(self.television.television_is_on())
        self.television.volume_up()
        self.television.volume_up()
        self.television.volume_up()
        self.television.mute()
        self.television.unmute()
        self.assertEqual(self.television.get_volume(), 0)

if __name__ == '__main__':
    unittest.main()
