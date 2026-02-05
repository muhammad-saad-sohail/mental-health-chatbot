"""
Sentiment Analysis Module
Uses BERT-based model for emotion detection in student messages
"""

import torch
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np


class SentimentAnalyzer:
    """
    BERT-based sentiment analyzer for mental health conversations
    Classifies messages into: positive, neutral, negative
    """
    
    def __init__(self, model_path='bert-base-uncased'):
        """Initialize the sentiment analyzer"""
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Using device: {self.device}")
        
        # Load tokenizer and model
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        # self.model = BertForSequenceClassification.from_pretrained(model_path, num_labels=3)
        # self.model.to(self.device)
        # self.model.eval()
        
        self.sentiment_labels = ['negative', 'neutral', 'positive']
        
    def preprocess(self, text):
        """Preprocess text for model input"""
        # Tokenize
        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=128,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        
        return encoding
    
    def analyze(self, text):
        """
        Analyze sentiment of input text
        
        Args:
            text (str): Input message
            
        Returns:
            dict: Sentiment analysis results
        """
        # TODO: Implement actual model inference
        # For demo purposes, return mock results
        
        # Simple keyword-based demo
        negative_keywords = ['anxious', 'sad', 'depressed', 'worried', 'stressed', 'scared']
        positive_keywords = ['happy', 'great', 'good', 'better', 'fine', 'excellent']
        
        text_lower = text.lower()
        
        if any(keyword in text_lower for keyword in negative_keywords):
            sentiment = 'negative'
            confidence = 0.85
        elif any(keyword in text_lower for keyword in positive_keywords):
            sentiment = 'positive'
            confidence = 0.82
        else:
            sentiment = 'neutral'
            confidence = 0.75
            
        return {
            'sentiment': sentiment,
            'confidence': confidence,
            'probabilities': {
                'negative': 0.33,
                'neutral': 0.33,
                'positive': 0.34
            }
        }
    
    def batch_analyze(self, texts):
        """Analyze multiple texts at once"""
        results = []
        for text in texts:
            results.append(self.analyze(text))
        return results


# Demo usage
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    
    test_messages = [
        "I'm feeling really anxious about my exams",
        "Today was a great day!",
        "I'm just okay, nothing special"
    ]
    
    print("\n=== Sentiment Analysis Demo ===\n")
    for msg in test_messages:
        result = analyzer.analyze(msg)
        print(f"Message: {msg}")
        print(f"Sentiment: {result['sentiment']} (confidence: {result['confidence']:.2f})")
        print("-" * 50)
