import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotion(unittest.TestCase):

    def test_joy(self):
        self.assertEqual(emotion_detector("I am happy")["dominant_emotion"], "joy")

    def test_sad(self):
        self.assertEqual(emotion_detector("I am sad")["dominant_emotion"], "sadness")

    def test_angry(self):
        self.assertEqual(emotion_detector("I am angry")["dominant_emotion"], "anger")

if __name__ == "__main__":
    unittest.main()
