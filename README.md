# Email Wake-Up Agent

## Project Overview
This project is an autonomous AI-powered Email Agent that initiates, manages, and sustains conversations with prospects regarding a work opportunity (gig). The agent communicates, negotiates within a defined budget, and schedules calls, maintaining context and memory across threads.

## Features
- Initiates outreach emails
- Handles multi-turn conversations
- Negotiates within a set budget
- Schedules and reschedules meetings
- Maintains conversation memory
- Integrates with OpenAI LLM (via API key)

## Directory Structure
```
email-wake-up-agent/
│
├── agent/           # LLM agent, prompt builder, intent classifier
├── config/          # Configuration loader
├── email/           # Email sender, receiver, parser
├── memory/          # Database and conversation repository
├── negotiation/     # Negotiation logic
├── orchestrator/    # Main controller
├── scheduler/       # Meeting scheduler and calendar adapter
├── tests/           # Test scripts
├── requirements.txt # Python dependencies
├── .env             # Environment variables (not committed)
└── README.md        # Project documentation
```

## Setup Instructions

### 1. Clone the Repository
```
git clone <repo-url>
cd email-wake-up-agent
```

### 2. Create and Activate a Virtual Environment (Recommended)
```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```
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
```

### 5. Run a Test
```
python tests/test_agent.py
```

## Running the Agent
- The main orchestration logic will be in `orchestrator/main_controller.py`.
- To run the full agent (after implementation):
```
python orchestrator/main_controller.py
```

## Design Overview
- See `email_wakeup_agent_assignment.txt` and `email_agent_HLD_LLD.txt` for requirements and design.
- Modular structure for easy extension and testing.

## Notes
- Use your own OpenAI API key.
- For email integration, use Gmail API or SMTP/IMAP (credentials required).
- For calendar integration, use Google Calendar API or a mock.

## Sample Commands
- Install dependencies: `pip install -r requirements.txt`
- Run agent test: `python tests/test_agent.py`
- Run main agent: `python orchestrator/main_controller.py`

---

For any issues, please refer to the code comments or contact the maintainer.
--------------------------
EMAIL 2 Auth Password

https://support.google.com/accounts/answer/185839?sjid=12493105641154969624-NC
---------------------------
Google Calander MEETING SETUP

Go to https://console.cloud.google.com/ and create a project.
Enable the Google Calendar API for your project.
Create OAuth 2.0 credentials (Desktop app or Web app).
Download the credentials.json file and place it in your project root.
-----------------------
Test Cases Step by Step
--------------------
python tests/test_agent.py    
python tests/test_email_sender.py    
python tests/test_email_receiver.py    
python tests/test_conversation_repo.py

python -m tests.test_conversation_repo
python orchestrator/main_controller.py