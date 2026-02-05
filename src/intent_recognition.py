"""
Intent Recognition Module
Identifies user intent from mental health conversations
"""

import re
from typing import Dict, List


class IntentRecognizer:
    """
    Classifies user intent in mental health conversations
    Intents: anxiety, depression, stress, general_conversation, crisis, etc.
    """
    
    def __init__(self):
        """Initialize intent recognizer with pattern matching"""
        self.intents = {
            'anxiety': {
                'keywords': ['anxious', 'anxiety', 'worried', 'nervous', 'panic', 'fear'],
                'patterns': [
                    r'worried about',
                    r'feeling anxious',
                    r'panic attack',
                    r'can\'t stop worrying'
                ]
            },
            'depression': {
                'keywords': ['depressed', 'sad', 'hopeless', 'worthless', 'empty', 'lonely'],
                'patterns': [
                    r'feeling down',
                    r'no motivation',
                    r'don\'t care anymore',
                    r'can\'t get out of bed'
                ]
            },
            'stress': {
                'keywords': ['stressed', 'overwhelmed', 'pressure', 'burnout', 'exhausted'],
                'patterns': [
                    r'too much work',
                    r'can\'t handle',
                    r'stressed out',
                    r'so much pressure'
                ]
            },
            'crisis': {
                'keywords': ['suicide', 'kill myself', 'end it all', 'hurt myself', 'self-harm'],
                'patterns': [
                    r'want to die',
                    r'better off dead',
                    r'end my life'
                ]
            },
            'sleep_issues': {
                'keywords': ['insomnia', 'can\'t sleep', 'nightmares', 'tired'],
                'patterns': [
                    r'trouble sleeping',
                    r'can\'t fall asleep',
                    r'wake up at night'
                ]
            },
            'relationship': {
                'keywords': ['relationship', 'breakup', 'friendship', 'family', 'conflict'],
                'patterns': [
                    r'broke up',
                    r'fight with',
                    r'friend problems'
                ]
            },
            'academic': {
                'keywords': ['exam', 'study', 'grades', 'assignment', 'homework', 'test'],
                'patterns': [
                    r'failing class',
                    r'exam stress',
                    r'too much homework'
                ]
            }
        }
        
    def recognize(self, text: str) -> Dict:
        """
        Recognize intent from user message
        
        Args:
            text (str): User message
            
        Returns:
            dict: Intent classification results
        """
        text_lower = text.lower()
        intent_scores = {}
        
        # Score each intent
        for intent_name, intent_data in self.intents.items():
            score = 0
            
            # Check keywords
            for keyword in intent_data['keywords']:
                if keyword in text_lower:
                    score += 1
                    
            # Check patterns
            for pattern in intent_data['patterns']:
                if re.search(pattern, text_lower):
                    score += 2
                    
            if score > 0:
                intent_scores[intent_name] = score
        
        # Determine primary intent
        if intent_scores:
            primary_intent = max(intent_scores, key=intent_scores.get)
            confidence = min(intent_scores[primary_intent] / 5.0, 0.95)
        else:
            primary_intent = 'general_conversation'
            confidence = 0.70
        
        # Check for crisis - always prioritize
        if 'crisis' in intent_scores:
            primary_intent = 'crisis'
            confidence = 0.99
            
        return {
            'intent': primary_intent,
            'confidence': confidence,
            'all_intents': intent_scores,
            'is_crisis': primary_intent == 'crisis'
        }
    
    def get_emergency_resources(self) -> Dict:
        """Return emergency mental health resources"""
        return {
            'crisis_hotlines': [
                {
                    'name': 'National Suicide Prevention Lifeline',
                    'number': '988',
                    'available': '24/7'
                },
                {
                    'name': 'Crisis Text Line',
                    'number': 'Text HOME to 741741',
                    'available': '24/7'
                }
            ],
            'message': 'If you are in immediate danger, please call emergency services or go to the nearest emergency room.'
        }


# Demo usage
if __name__ == "__main__":
    recognizer = IntentRecognizer()
    
    test_messages = [
        "I'm feeling really anxious about my upcoming exams",
        "I can't sleep and feel so tired all the time",
        "I broke up with my girlfriend and feel so alone",
        "I'm so stressed with all this work, it's overwhelming"
    ]
    
    print("\n=== Intent Recognition Demo ===\n")
    for msg in test_messages:
        result = recognizer.recognize(msg)
        print(f"Message: {msg}")
        print(f"Intent: {result['intent']} (confidence: {result['confidence']:.2f})")
        print(f"All detected intents: {result['all_intents']}")
        print("-" * 70)
