---
name: reflective-tarot-draw
description: Performs a random tarot card draw for entertainment and self-reflection. Use this skill when the user asks for a one-card, three-card, or decision-style tarot reading and needs a structured draw with unique cards, upright/reversed orientation, and non-predictive interpretation.
---

# Reflective Tarot Draw Skill

## When to use this skill

Use this skill when the user asks for a tarot-style reading for entertainment, journaling, self-reflection, or exploring feelings around a question.

This skill is especially useful when the user wants:
- a one-card reflection
- a three-card spread
- a decision spread comparing two options
- a structured tarot draw with no duplicate cards
- a reading that is symbolic rather than predictive

## When not to use this skill

Do not use this skill to:
- make factual predictions about the future
- guarantee relationship outcomes
- make medical, legal, financial, immigration, or safety decisions
- diagnose a person or label someone’s personality
- replace professional advice

If the user asks for certainty, explain that tarot readings are symbolic and should be used only for entertainment and reflection.

## Expected inputs

The user should provide:
- a question or topic
- a spread type

Supported spread types:
- `one-card`
- `three-card`
- `decision`

If the user does not provide a spread type, default to `three-card`.

## Script role

The Python script is required because the tarot draw must be handled in a reliable and verifiable way.

The script must:
- validate the requested spread type
- load a tarot deck
- shuffle the deck
- draw unique cards
- randomly assign upright or reversed orientation
- match each card to the correct spread position
- return structured JSON output

The model should not invent cards or manually choose cards. The model should run the script and base the reading on the script output.

## Step-by-step instructions

1. Identify the user's question.
2. Identify the spread type. If none is provided, use `three-card`.
3. Run the Python script in `scripts/tarot_draw.py` with the question and spread type.
4. Read the structured output from the script.
5. Explain the cards in a reflective, non-deterministic way.
6. Include a short note that the reading is for entertainment and self-reflection only.

## Expected output format

Use this format:

```text
Reflective Tarot Reading

Question:
[user question]

Spread:
[spread type]

Cards Drawn:
1. [position]: [card name] — [upright/reversed]
2. [position]: [card name] — [upright/reversed]
3. [position]: [card name] — [upright/reversed]

Reading:
[short reflective interpretation]

Reflection Questions:
- [question 1]
- [question 2]

Note:
This reading is for entertainment and self-reflection only. It should not be treated as a factual prediction or professional advice.


