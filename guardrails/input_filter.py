import re
from colorama import Fore

def is_malicious_intent(user_input):
    user_input_lower = user_input.lower()
    
    # 1. Block command overrides
    override_keywords = ["ignore", "override", "bypass", "system", "diagnostic", "developer"]
    if any(word in user_input_lower for word in override_keywords):
        print(Fore.YELLOW + "[!] GUARDRAIL TRIGGERED: Command Override Attempt Detected.")
        return True
        
    # 2. Block targeted entity extraction 
    # In a real app, this connects to the auth session. Here we hardcode the protected entities.
    protected_entities = ["alice", "bob", "charlie"]
    if any(name in user_input_lower for name in protected_entities):
        print(Fore.YELLOW + "[!] GUARDRAIL TRIGGERED: Unauthorized Entity Query Detected.")
        return True
        
    return False