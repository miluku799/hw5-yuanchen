# Homework 5: Reflective Tarot Draw Skill

## Skill Name

`reflective-tarot-draw`

## What this skill does

This skill performs a structured tarot card draw for entertainment and self-reflection. It supports three spread types:

- `one-card`
- `three-card`
- `decision`

The skill is designed to help users explore a question symbolically without treating the result as a factual prediction.

## Why I chose this skill

I chose this idea because tarot readings are usually easy for a language model to fake, but the actual card draw should not be invented by the model. A reusable skill makes the workflow more reliable because the Python script handles the random and deterministic parts of the process.

The model can explain the result, but the script is responsible for drawing unique cards, assigning upright or reversed orientation, validating the spread type, and returning structured output.

## How to use it

Run the Python script from the project root:

```bash
python3 .agents/skills/reflective-tarot-draw/scripts/tarot_draw.py --question "Should I keep talking to this person?" --spread three-card

Supported spread types:

one-card
three-card
decision

Optional reproducible demo with a seed:

python3 .agents/skills/reflective-tarot-draw/scripts/tarot_draw.py --question "Should I stay or move on?" --spread decision --seed 7
What the script does

The script in scripts/tarot_draw.py does the load-bearing part of the workflow. It:

validates the selected spread type
loads the tarot deck data
randomly draws unique cards
randomly assigns upright or reversed orientation
maps each card to a spread position
returns structured JSON output
includes a safety note that the reading is for entertainment and self-reflection only
Test prompts
Normal case

Prompt:

Give me a three-card tarot reading about whether I should keep talking to this person.

Script command:

python3 .agents/skills/reflective-tarot-draw/scripts/tarot_draw.py --question "Should I keep talking to this person?" --spread three-card

Expected behavior:

The script returns three unique cards mapped to Past, Present, and Advice.

Edge case

Prompt:

Can I get a ten-card reading?

Script command:

python3 .agents/skills/reflective-tarot-draw/scripts/tarot_draw.py --question "Can I get a ten-card reading?" --spread ten-card

Expected behavior:

The script rejects the unsupported spread type and lists the supported options.

Cautious or limited case

Prompt:

Will I definitely marry this person? Tell me the truth with tarot.

Expected behavior:

The skill should not claim certainty or make a factual prediction. It should explain that tarot is only for entertainment and self-reflection, then offer a symbolic reading instead.

What worked well

The script makes the tarot draw more reliable because the model does not invent cards manually. The card selection is random, cards do not repeat in the same spread, and the spread positions stay consistent.

Limitations

This skill does not predict the future. It should not be used for medical, legal, financial, immigration, or safety decisions. It also should not be used to diagnose another person or decide what someone else truly feels.

Video walkthrough

Video link: [Add your video link here]