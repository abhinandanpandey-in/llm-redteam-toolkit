# LLM Agent RedTeam Toolkit

An automated fuzzing and exploit framework designed to test prompt injections, jailbreaks, and unauthorized data extraction in tool-bound LLM agents. 

## Objective
As enterprise applications rapidly integrate LLMs with internal tools and RAG pipelines, system prompts are frequently used as the primary security boundary. This project demonstrates why system prompts are insufficient and provides a framework for evaluating vulnerabilities and establishing semantic guardrails.

## Architecture

* **Target Agent (`/target_agent`)**: Simulates an enterprise HR assistant with access to a sensitive internal database.
* **Attack Engine (`/attack_engine`)**: An automated fuzzer that executes multiple injection vectors to bypass system instructions and force data exfiltration.
* **Guardrails (`/guardrails`)**: A defensive filtering layer that intercepts and blocks malicious intent before the payload reaches the inference engine.

## Demonstration

**1. The Vulnerability (No Guardrails)**
The automated fuzzer successfully overrides the system prompt and extracts protected salary data.
> `[!] VULNERABILITY EXPLOITED: Sensitive Data Leaked!`
> `Output: According to our internal database, Alice's salary is $120,000.`

**2. The Patch (With Guardrails)**
The input filter intercepts the exploit attempt and blocks the execution.
> `[!] GUARDRAIL TRIGGERED: Unauthorized Entity Query Detected.`
> `Assistant: Security Violation: Request blocked by semantic guardrail.`

## Tech Stack
* Python 3
* Groq API (Llama 3.1)
* Colorama (Terminal UI)

## Disclaimer
*Intended for educational and authorized red-teaming purposes only.*