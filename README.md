
# Email Wake-Up Agent

## Overview
The Email Wake-Up Agent is an autonomous, AI-powered system that manages professional email conversations, negotiates work opportunities, and schedules meetings with prospects. It leverages OpenAI LLM for natural language understanding, maintains conversation memory, and integrates with Google Calendar for scheduling.

---

## Features
- Initiates and replies to emails automatically
- Handles multi-turn, context-aware conversations
- Negotiates within a defined budget
- Schedules, reschedules, and cancels meetings
- Maintains persistent conversation memory (SQLite)
- Integrates with OpenAI (via API key)
- Google Calendar integration for meeting management
- Streamlit UI dashboard for monitoring conversations
- Modular, extensible architecture

---

## Directory Structure
```
email-wake-up-agent/
│
├── agent/           # LLM agent, prompt builder, intent classifier
├── config/          # Configuration loader
├── email/           # Email sender, receiver, parser
├── memory/          # Conversation memory (SQLite)
├── negotiation/     # Negotiation logic
├── orchestrator/    # Main controller
├── scheduler/       # Meeting scheduler, Google Calendar adapter
├── tests/           # Unit and integration tests
├── ui_streamlit.py  # Streamlit UI dashboard
├── requirements.txt # Python dependencies
├── .env             # Environment variables (not committed)
└── README.md        # Project documentation
```

---

## Setup & Installation

### 1. Clone the Repository
```sh
git clone <repo-url>
cd email-wake-up-agent
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with the following keys:
```
OPENAI_API_KEY=your_openai_key_here
GIG_DESCRIPTION=Short description of the gig
BUDGET_LIMIT=1000
TONE=Professional
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
GOOGLE_CALENDAR_ID=your_calendar_id
TIMEZONE=Your/Timezone
```

---

## Google Calendar Integration Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **Google Calendar API** for your project.
4. Create OAuth 2.0 credentials (Desktop or Web app).
5. Download the `credentials.json` file and place it in your project root.
6. (Optional) For service accounts:
	- Create a Service Account
	- Go to "Keys" and create a new JSON key
	- Download and save as `calendar_credentials.json` in your project root
	- Share your Google Calendar with the service account’s `client_email`

**Email Auth Note:** For Gmail, you may need an App Password. See [Google App Passwords](https://support.google.com/accounts/answer/185839) for details.

---

## Usage

### Run the Main Agent
```sh
python orchestrator/main_controller.py
```

### Run the Streamlit UI Dashboard
```sh
streamlit run ui_streamlit.py
```
This opens a web dashboard to view and monitor conversations.

### Run Tests
```sh
python tests/test_agent.py
python tests/test_email_sender.py
python tests/test_email_receiver.py
python tests/test_conversation_repo.py
python -m tests.test_conversation_repo
```

---

## Project Design
- Modular structure for easy extension and testing
- Robust error handling and logging
- Persistent memory for conversation context
- Google Calendar and email integration
- Streamlit UI for monitoring

See `email_wakeup_agent_assignment.txt` and `email_agent_HLD_LLD.txt` for detailed requirements and design documents.

---

## Troubleshooting & Notes
- Use your own OpenAI API key and email credentials
- Ensure Google Calendar API is enabled and credentials are correct
- For email, use Gmail App Passwords if 2FA is enabled
- All sensitive data should be stored in `.env` (never commit this file)

---

## Maintainer & Support
For issues, please refer to code comments or contact the project maintainer.