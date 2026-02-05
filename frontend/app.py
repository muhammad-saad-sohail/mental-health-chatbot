"""
Mental Health Chatbot - Streamlit Frontend
Interactive web interface for the chatbot
"""

import streamlit as st
import requests
import json
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Mental Health Support Chatbot",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API endpoint
API_URL = "http://localhost:5000"

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'session_id' not in st.session_state:
    st.session_state.session_id = f"session_{datetime.now().timestamp()}"

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        text-align: right;
    }
    .bot-message {
        background-color: #f5f5f5;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 2px solid #ffc107;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .crisis-box {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🧠 Mental Health Support Chatbot</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("""
    This AI-powered chatbot provides mental health support for students.
    
    **Features:**
    - 24/7 availability
    - Anonymous and confidential
    - Evidence-based recommendations
    - Crisis detection
    
    **Note:** This is not a replacement for professional mental health care.
    If you're in crisis, please call 988 or contact emergency services.
    """)
    
    st.divider()
    
    st.header("Resources")
    st.write("""
    **Crisis Hotlines:**
    - 988 Suicide & Crisis Lifeline
    - Text HOME to 741741
    
    **Campus Resources:**
    - Student Counseling Center
    - Health & Wellness Office
    """)
    
    st.divider()
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.session_id = f"session_{datetime.now().timestamp()}"
        st.rerun()

# Main chat interface
st.write("### Chat with your mental health support assistant")

# Display disclaimer
st.markdown("""
<div class="warning-box">
    <strong>⚠️ Important Disclaimer:</strong> This chatbot is for informational and support purposes only. 
    It is not a substitute for professional mental health care. If you're experiencing a mental health emergency, 
    please call 988 or your local emergency services immediately.
</div>
""", unsafe_allow_html=True)

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {message['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 Assistant:</strong> {message['content']}
            </div>
            """, unsafe_allow_html=True)
            
            # Show recommendations if available
            if 'recommendations' in message and message['recommendations']:
                with st.expander("💡 Recommended Coping Strategies"):
                    for rec in message['recommendations']:
                        st.write(f"- {rec}")

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({
        'role': 'user',
        'content': user_input,
        'timestamp': datetime.now().isoformat()
    })
    
    # Call API
    try:
        response = requests.post(
            f"{API_URL}/api/chat",
            json={
                'message': user_input,
                'user_id': 'streamlit_user',
                'session_id': st.session_state.session_id
            },
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Add bot response to history
            st.session_state.messages.append({
                'role': 'assistant',
                'content': data.get('response', 'Sorry, I encountered an error.'),
                'recommendations': data.get('recommendations', []),
                'sentiment': data.get('sentiment'),
                'intent': data.get('intent'),
                'timestamp': datetime.now().isoformat()
            })
            
            # Check for crisis
            if data.get('intent') == 'crisis':
                st.markdown("""
                <div class="crisis-box">
                    <strong>🚨 CRISIS ALERT</strong><br>
                    If you are in immediate danger, please:
                    <ul>
                        <li>Call 988 (Suicide & Crisis Lifeline)</li>
                        <li>Text HOME to 741741 (Crisis Text Line)</li>
                        <li>Call 911 or go to nearest emergency room</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error(f"API Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Cannot connect to the API server. Please make sure the Flask server is running on http://localhost:5000")
    except Exception as e:
        st.error(f"Error: {str(e)}")
    
    # Rerun to update chat display
    st.rerun()

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <small>
    Mental Health Chatbot v1.0 | Developed by Muhammad Saad Sohail<br>
    Final Year Project - BS Artificial Intelligence<br>
    Arid Agriculture University, Rawalpindi
    </small>
</div>
""", unsafe_allow_html=True)
