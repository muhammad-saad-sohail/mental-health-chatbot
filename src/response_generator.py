"""
Response Generation Module
Generates empathetic responses based on sentiment and intent
"""

import random
from typing import Dict, List


class ResponseGenerator:
    """
    Generates contextual responses for mental health conversations
    Uses template-based approach combined with ML-generated variations
    """
    
    def __init__(self):
        """Initialize response templates"""
        self.response_templates = {
            'anxiety': [
                "I understand that anxiety can feel overwhelming. Let's work through this together. {coping_strategy}",
                "It's completely normal to feel anxious sometimes. {validation} Would you like to try a grounding exercise?",
                "Anxiety can be really difficult to manage. {empathy} Let me suggest some techniques that might help."
            ],
            'depression': [
                "I hear you, and I want you to know that what you're feeling is valid. {support}",
                "Depression can make everything feel heavy. {empathy} You're not alone in this.",
                "Thank you for sharing this with me. {validation} Have you considered talking to a counselor?"
            ],
            'stress': [
                "It sounds like you're dealing with a lot right now. {validation} Let's break this down together.",
                "Stress can be really overwhelming. {empathy} What specific aspect is bothering you most?",
                "I can hear that you're under a lot of pressure. {support} Let's find some ways to help you manage this."
            ],
            'academic': [
                "Academic pressure is really challenging. {validation} Have you tried breaking your study into smaller chunks?",
                "Exam stress is so common among students. {empathy} Let me share some study techniques that might help.",
                "I understand how stressful academic demands can be. {support} What subject is giving you the most trouble?"
            ],
            'crisis': [
                "I'm really concerned about what you're sharing with me. Your life is valuable. Please reach out to a crisis hotline immediately: Call 988 or text HOME to 741741.",
                "What you're feeling is serious, and I want to make sure you get the help you need. Please contact a mental health professional or crisis hotline right away.",
                "I'm here to listen, but I want to connect you with someone who can provide immediate professional help. Please call 988 - they're available 24/7."
            ],
            'general_conversation': [
                "I'm here to listen. {empathy} Can you tell me more about what's on your mind?",
                "Thank you for sharing that with me. {validation} How have you been coping with this?",
                "I appreciate you opening up. {support} What would be most helpful for you right now?"
            ]
        }
        
        self.empathy_phrases = [
            "That sounds really difficult",
            "I can imagine how challenging that must be",
            "It takes courage to share this",
            "I appreciate you trusting me with this"
        ]
        
        self.validation_phrases = [
            "Your feelings are completely valid",
            "It's okay to feel this way",
            "Many students experience similar challenges",
            "What you're going through is real and important"
        ]
        
        self.support_phrases = [
            "I'm here to support you",
            "You don't have to go through this alone",
            "We can work on this together",
            "I'm here to help in any way I can"
        ]
        
        self.coping_strategies = {
            'anxiety': [
                "Try the 5-4-3-2-1 grounding technique: Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, and 1 you taste.",
                "Practice deep breathing: Breathe in for 4 counts, hold for 4, exhale for 4, and pause for 4.",
                "Try progressive muscle relaxation - tense and relax each muscle group one at a time."
            ],
            'stress': [
                "Consider taking regular breaks using the Pomodoro technique (25 minutes work, 5 minutes break).",
                "Make a priority list and tackle one thing at a time.",
                "Practice saying 'no' to non-essential commitments."
            ],
            'depression': [
                "Try to maintain a routine, even if it's small tasks.",
                "Consider gentle exercise like a short walk - it can help boost mood.",
                "Connect with at least one person, even if it's just a text message."
            ],
            'academic': [
                "Create a study schedule and break large tasks into smaller, manageable chunks.",
                "Use active recall and spaced repetition for better retention.",
                "Form a study group with classmates for support and accountability."
            ]
        }
    
    def generate(self, intent: str, sentiment: str, context: Dict = None) -> Dict:
        """
        Generate response based on intent and sentiment
        
        Args:
            intent (str): Detected intent
            sentiment (str): Detected sentiment
            context (dict): Additional context
            
        Returns:
            dict: Generated response with recommendations
        """
        # Get template based on intent
        if intent in self.response_templates:
            template = random.choice(self.response_templates[intent])
        else:
            template = random.choice(self.response_templates['general_conversation'])
        
        # Fill in template placeholders
        response = template.format(
            empathy=random.choice(self.empathy_phrases),
            validation=random.choice(self.validation_phrases),
            support=random.choice(self.support_phrases),
            coping_strategy=random.choice(self.coping_strategies.get(intent, ['']))
        )
        
        # Get recommendations
        recommendations = self.get_recommendations(intent)
        
        # Check if crisis
        is_crisis = intent == 'crisis'
        
        return {
            'response': response,
            'recommendations': recommendations,
            'is_crisis': is_crisis,
            'follow_up_questions': self.get_follow_up_questions(intent)
        }
    
    def get_recommendations(self, intent: str) -> List[Dict]:
        """Get coping strategy recommendations"""
        if intent in self.coping_strategies:
            strategies = self.coping_strategies[intent]
            return [
                {
                    'type': intent,
                    'strategy': strategy,
                    'difficulty': 'easy'
                }
                for strategy in strategies[:2]  # Return top 2
            ]
        return []
    
    def get_follow_up_questions(self, intent: str) -> List[str]:
        """Generate follow-up questions"""
        follow_ups = {
            'anxiety': [
                "What specific situations trigger your anxiety?",
                "Have you noticed any patterns in when you feel most anxious?"
            ],
            'depression': [
                "How long have you been feeling this way?",
                "Have you talked to anyone else about how you're feeling?"
            ],
            'stress': [
                "What's the main source of your stress right now?",
                "What have you tried so far to manage this stress?"
            ],
            'academic': [
                "Which subject or assignment is causing you the most stress?",
                "What's your current study routine like?"
            ]
        }
        
        return follow_ups.get(intent, [
            "Can you tell me more about what's been going on?",
            "How have you been coping with this so far?"
        ])


# Demo usage
if __name__ == "__main__":
    generator = ResponseGenerator()
    
    test_cases = [
        ('anxiety', 'negative'),
        ('depression', 'negative'),
        ('stress', 'negative'),
        ('academic', 'neutral')
    ]
    
    print("\n=== Response Generation Demo ===\n")
    for intent, sentiment in test_cases:
        result = generator.generate(intent, sentiment)
        print(f"Intent: {intent} | Sentiment: {sentiment}")
        print(f"Response: {result['response']}")
        print(f"Recommendations: {len(result['recommendations'])} strategies")
        print(f"Follow-up questions: {result['follow_up_questions']}")
        print("-" * 70)
