# 🧠 AI-Powered Student Psychological Health Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=flat&logo=tensorflow)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red?style=flat&logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=flat)

**An intelligent mental health support chatbot leveraging NLP and BERT-based sentiment analysis to provide instant psychological support to students.**

[Live Demo](https://mental-health-ai.vercel.app) · [Report Bug](https://github.com/muhammad-saad-sohail/mental-health-chatbot/issues) · [Request Feature](https://github.com/muhammad-saad-sohail/mental-health-chatbot/issues)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technical Architecture](#technical-architecture)
- [Performance Metrics](#performance-metrics)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Overview

The **AI-Powered Student Psychological Health Chatbot** is my final year project designed to address the growing mental health crisis among university students. This intelligent system uses advanced NLP techniques and transformer models to provide immediate, empathetic support to students experiencing psychological challenges.

### Problem Statement

- Traditional counseling services have **24+ hour wait times**
- Many students hesitate to seek help due to stigma
- Limited availability of mental health professionals on campuses

### Solution

An AI chatbot that:
- Provides **instant, 24/7 support** to students
- Analyzes sentiment and emotional state with **85% accuracy**
- Offers personalized, evidence-based coping strategies
- Maintains complete **privacy and anonymity**

---

## ✨ Key Features

### 🤖 **Intelligent Conversation**
- **BERT-based Sentiment Analysis**: Accurately detects emotional states in student messages
- **Intent Recognition**: Understands specific mental health concerns (anxiety, stress, depression, etc.)
- **Context-Aware Responses**: Maintains conversation history for coherent, personalized interactions

### 🎯 **Personalized Support**
- **Evidence-Based Recommendations**: Suggests coping strategies based on psychological research
- **Adaptive Response System**: Adjusts communication style based on user's emotional state
- **Crisis Detection**: Identifies high-risk situations and provides emergency resources

### 📊 **Analytics & Insights**
- **Conversation Pattern Analysis**: Tracks common concerns among students
- **Sentiment Trends**: Monitors emotional well-being over time
- **Effectiveness Metrics**: Measures user satisfaction and engagement

### 🔒 **Privacy & Security**
- **End-to-End Encryption**: All conversations are securely encrypted
- **Anonymous Usage**: No personal information required
- **GDPR Compliant**: Follows data protection regulations

---

## 🏗️ Technical Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│              (React.js + Streamlit)                      │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  API Gateway                             │
│                  (Flask REST API)                        │
└────────────────────┬────────────────────────────────────┘
                     │
          ┌──────────┴──────────┐
          │                     │
┌─────────▼──────────┐  ┌──────▼──────────────────────────┐
│  Sentiment Model   │  │   Intent Recognition Model      │
│   (BERT-based)     │  │   (Transformer-based)           │
└─────────┬──────────┘  └──────┬──────────────────────────┘
          │                     │
          └──────────┬──────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│           Response Generation System                     │
│    (Custom Transformer + Template-based)                │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              Recommendation Engine                       │
│         (Collaborative Filtering + Rule-based)          │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                   Database                               │
│           (MongoDB + Firebase)                           │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 Performance Metrics

| Metric | Value | Dataset |
|--------|-------|---------|
| **Sentiment Analysis Accuracy** | 85% | 2,000+ conversations |
| **Intent Recognition F1-Score** | 0.82 | Multi-class classification |
| **Response Time** | <2 seconds | Average per message |
| **User Satisfaction** | 20% improvement | 100+ participants |
| **Active Users** | 500+ | University pilot program |
| **Conversation Completion Rate** | 78% | Full session engagement |

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- MongoDB (local or cloud instance)
- 8GB+ RAM recommended for model inference

### Step 1: Clone the Repository

```bash
git clone https://github.com/muhammad-saad-sohail/mental-health-chatbot.git
cd mental-health-chatbot
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download Pre-trained Models

```bash
# Download BERT model and tokenizer
python scripts/download_models.py
```

### Step 5: Configure Environment Variables

Create a `.env` file in the root directory:

```env
MONGODB_URI=your_mongodb_connection_string
FLASK_SECRET_KEY=your_secret_key
MODEL_PATH=./models/bert_sentiment
HUGGINGFACE_TOKEN=your_hf_token
ENVIRONMENT=development
```

### Step 6: Initialize Database

```bash
python scripts/init_database.py
```

---

## 💻 Usage

### Running the Flask API Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Running the Streamlit Frontend

```bash
streamlit run frontend/app.py
```

The web interface will open at `http://localhost:8501`

### API Endpoints

#### 1. Send Message
```bash
POST /api/chat
Content-Type: application/json

{
  "user_id": "anonymous_123",
  "message": "I've been feeling really anxious about my exams",
  "session_id": "session_456"
}
```

**Response:**
```json
{
  "response": "I understand exam anxiety can be overwhelming. Let's work through this together...",
  "sentiment": "negative",
  "intent": "anxiety",
  "recommendations": [
    "Try the 5-4-3-2-1 grounding technique",
    "Practice deep breathing exercises"
  ],
  "confidence": 0.87
}
```

---

## 📁 Project Structure

```
mental-health-chatbot/
│
├── app.py                      # Flask API server
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── README.md                  # This file
│
├── models/                    # Trained models
│   ├── bert_sentiment/        # BERT sentiment analysis model
│   ├── intent_classifier/     # Intent recognition model
│   └── recommendation_engine/ # Recommendation system
│
├── src/                       # Source code
│   ├── __init__.py
│   ├── sentiment_analysis.py  # Sentiment detection module
│   ├── intent_recognition.py  # Intent classification module
│   ├── response_generator.py  # Response generation logic
│   ├── recommendation.py      # Recommendation engine
│   └── database.py           # Database operations
│
├── frontend/                  # Web interface
│   ├── app.py                # Streamlit app
│   ├── components/           # UI components
│   └── static/               # CSS, images
│
├── notebooks/                 # Jupyter notebooks
│   ├── data_exploration.ipynb
│   ├── model_training.ipynb
│   └── evaluation.ipynb
│
├── scripts/                   # Utility scripts
│   ├── download_models.py
│   ├── init_database.py
│   └── train_model.py
│
├── data/                      # Dataset
│   ├── raw/                  # Original conversation data
│   ├── processed/            # Preprocessed data
│   └── annotations/          # Labeled data
│
├── tests/                     # Unit tests
│   ├── test_sentiment.py
│   ├── test_intent.py
│   └── test_api.py
│
└── docs/                      # Documentation
    ├── API_DOCUMENTATION.md
    ├── MODEL_ARCHITECTURE.md
    └── DEPLOYMENT_GUIDE.md
```

---

## 🛠️ Technologies Used

### Machine Learning & NLP
- **TensorFlow 2.x** - Deep learning framework
- **PyTorch** - Neural network training
- **Hugging Face Transformers** - Pre-trained BERT models
- **Scikit-learn** - Classical ML algorithms
- **NLTK & SpaCy** - Text preprocessing

### Backend
- **Flask** - REST API framework
- **MongoDB** - NoSQL database for conversations
- **Firebase** - Real-time data sync
- **Redis** - Caching layer

### Frontend
- **Streamlit** - Interactive web interface
- **React.js** - Alternative UI framework
- **Chart.js** - Data visualization

### Deployment & DevOps
- **Docker** - Containerization
- **AWS EC2** - Cloud hosting
- **AWS S3** - Model storage
- **GitHub Actions** - CI/CD pipeline

---

## 📈 Future Enhancements

### Short-term Goals
- [ ] Multi-language support (Urdu, Arabic)
- [ ] Voice input/output capabilities
- [ ] Integration with university counseling services
- [ ] Mobile app development (React Native)

### Medium-term Goals
- [ ] Fine-tune GPT-3/4 for more natural conversations
- [ ] Implement active learning for continuous improvement
- [ ] Add group therapy chat rooms
- [ ] Develop therapist dashboard for oversight

### Long-term Vision
- [ ] Expand to other universities across Pakistan
- [ ] Research publication on effectiveness
- [ ] Partnership with mental health organizations
- [ ] Open-source community around mental health AI

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Contact

**Muhammad Saad Sohail**

- Email: rajasaadsohail646@gmail.com
- LinkedIn: [linkedin.com/in/saadsohail](https://linkedin.com/in/saadsohail)
- GitHub: [@muhammad-saad-sohail](https://github.com/muhammad-saad-sohail)

**Project Link:** [https://github.com/muhammad-saad-sohail/mental-health-chatbot](https://github.com/muhammad-saad-sohail/mental-health-chatbot)

---

## 🙏 Acknowledgments

- Arid Agriculture University for support and resources
- INEXOR Artificial Intelligence for professional guidance
- DeepLearning.AI for educational resources
- Open-source community for amazing tools

---

<div align="center">

**⭐ If this project helped you, please consider giving it a star! ⭐**

*Made with ❤️ for student mental health*

</div>
