# Mental Health Chatbot - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- pip package manager

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/muhammad-saad-sohail/mental-health-chatbot.git
cd mental-health-chatbot
```

2. **Create virtual environment**
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your configuration
# At minimum, set:
# - MONGODB_URI (if using MongoDB)
# - FLASK_SECRET_KEY
```

5. **Run the application**

**Backend API:**
```bash
python app.py
```
Access at: http://localhost:5000

**Frontend Interface:**
```bash
streamlit run frontend/app.py
```
Access at: http://localhost:8501

## 📁 Project Structure

```
mental-health-chatbot/
├── app.py                     # Main Flask API server
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
├── .gitignore               # Git ignore rules
├── README.md                # Main documentation
│
├── src/                     # Core application code
│   ├── __init__.py
│   ├── sentiment_analysis.py   # BERT sentiment model
│   ├── intent_recognition.py   # Intent classifier
│   └── response_generator.py   # Response generation
│
├── frontend/                # Web interface
│   └── app.py              # Streamlit app
│
├── models/                  # Trained ML models
├── data/                    # Training data
├── scripts/                 # Utility scripts
├── tests/                   # Unit tests
└── docs/                    # Additional documentation
```

## 🧪 Testing the API

### Test with curl:
```bash
# Health check
curl http://localhost:5000/health

# Send a message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I am feeling anxious about my exams", "user_id": "test_user"}'
```

### Test with Python:
```python
import requests

response = requests.post(
    'http://localhost:5000/api/chat',
    json={
        'message': 'I feel stressed about my exams',
        'user_id': 'test_user',
        'session_id': 'test_session'
    }
)

print(response.json())
```

## 🎯 Current Features

✅ **Working:**
- Flask REST API with multiple endpoints
- Streamlit web interface
- Basic sentiment analysis (keyword-based demo)
- Intent recognition system
- Response generation with templates
- Coping strategy recommendations
- Crisis detection

⏳ **In Development:**
- BERT model training and integration
- MongoDB database integration
- User authentication
- Conversation history
- Advanced analytics dashboard

## 📝 Development Roadmap

### Phase 1: Foundation (Current)
- [x] Project structure
- [x] Basic API endpoints
- [x] Web interface
- [x] Demo functionality

### Phase 2: ML Integration
- [ ] Train BERT sentiment model
- [ ] Implement intent classifier
- [ ] Add conversation context
- [ ] Integrate database

### Phase 3: Advanced Features
- [ ] User profiles
- [ ] Analytics dashboard
- [ ] Mobile app
- [ ] Multi-language support

## 🤝 Contributing

This is a final year project, but suggestions and feedback are welcome!

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📞 Contact

**Muhammad Saad Sohail**
- Email: rajasaadsohail646@gmail.com
- GitHub: [@muhammad-saad-sohail](https://github.com/muhammad-saad-sohail)
- LinkedIn: [saadsohail](https://linkedin.com/in/saadsohail)

## 📄 License

MIT License - see LICENSE file for details

---

**Note:** This is an academic project for mental health awareness. It is not a substitute for professional mental health care.
