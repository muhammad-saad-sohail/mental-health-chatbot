"""
Mental Health Chatbot - Flask API Server
Main application entry point
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import custom modules (these will be created)
# from src.sentiment_analysis import SentimentAnalyzer
# from src.intent_recognition import IntentRecognizer
# from src.response_generator import ResponseGenerator
# from src.database import Database

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')
app.config['DEBUG'] = os.getenv('DEBUG', 'True') == 'True'

# Initialize components (placeholder - will be implemented)
# sentiment_analyzer = SentimentAnalyzer()
# intent_recognizer = IntentRecognizer()
# response_generator = ResponseGenerator()
# db = Database()


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Mental Health Chatbot API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'chat': '/api/chat',
            'history': '/api/history/<session_id>',
            'recommendations': '/api/recommendations/<user_id>',
            'health': '/health'
        }
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint
    
    Expected JSON:
    {
        "user_id": "anonymous_123",
        "message": "I'm feeling anxious",
        "session_id": "session_456"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        user_message = data['message']
        user_id = data.get('user_id', 'anonymous')
        session_id = data.get('session_id', 'default')
        
        # TODO: Implement actual model inference
        # For now, return a demo response
        response = {
            'response': f"I understand you're saying: '{user_message}'. I'm here to help. This is a demo response - full AI model coming soon!",
            'sentiment': 'neutral',
            'intent': 'general_conversation',
            'recommendations': [
                'Take a few deep breaths',
                'Try mindfulness exercises'
            ],
            'confidence': 0.75,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/history/<session_id>', methods=['GET'])
def get_history(session_id):
    """Get conversation history for a session"""
    try:
        # TODO: Implement database query
        return jsonify({
            'session_id': session_id,
            'messages': [],
            'message': 'History retrieval - coming soon'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    """Get personalized recommendations for a user"""
    try:
        # TODO: Implement recommendation logic
        recommendations = [
            {
                'type': 'breathing_exercise',
                'title': 'Deep Breathing Technique',
                'description': 'Breathe in for 4 seconds, hold for 4, exhale for 4'
            },
            {
                'type': 'grounding',
                'title': '5-4-3-2-1 Technique',
                'description': 'Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste'
            }
        ]
        
        return jsonify({
            'user_id': user_id,
            'recommendations': recommendations
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/sentiment', methods=['POST'])
def analyze_sentiment():
    """Analyze sentiment of a message"""
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        # TODO: Implement actual sentiment analysis
        return jsonify({
            'message': message,
            'sentiment': 'neutral',
            'confidence': 0.85,
            'note': 'Using demo sentiment analysis'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv('API_PORT', 5000))
    host = os.getenv('API_HOST', '0.0.0.0')
    
    print(f"""
    ╔══════════════════════════════════════════════╗
    ║   Mental Health Chatbot API Server          ║
    ║   Version: 1.0.0                             ║
    ║   Running on: http://{host}:{port}           ║
    ╚══════════════════════════════════════════════╝
    """)
    
    app.run(host=host, port=port, debug=app.config['DEBUG'])
