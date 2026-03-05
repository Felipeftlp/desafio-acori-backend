from collections import defaultdict

sessions = defaultdict(list)

def add_message(session_id: str, message: str):
    sessions[session_id].append(message)
    if len(sessions[session_id]) > 6:
        sessions[session_id] = sessions[session_id][-6:]

def get_history(session_id: str):
    return sessions[session_id]