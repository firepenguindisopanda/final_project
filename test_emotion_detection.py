import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]
        
        for text, expected_dominant_emotion in test_cases:
            with self.subTest(text=text, expected=expected_dominant_emotion):
                result = emotion_detector(text)
                self.assertEqual(result['dominant_emotion'], expected_dominant_emotion, 
                                 f"Expected {expected_dominant_emotion} but got {result['dominant_emotion']} for text: '{text}'")

if __name__ == "__main__":
    unittest.main()
