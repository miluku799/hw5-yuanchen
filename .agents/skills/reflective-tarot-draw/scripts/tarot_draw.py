#!/usr/bin/env python3

import argparse
import json
import random
from datetime import datetime

SPREADS = {
    "one-card": ["Reflection"],
    "three-card": ["Past", "Present", "Advice"],
    "decision": ["Option A", "Option B", "Hidden Factor"],
}

TAROT_DECK = [
    {"name": "The Fool", "upright": "new beginnings, openness, possibility", "reversed": "recklessness, hesitation, unclear direction"},
    {"name": "The Magician", "upright": "agency, focus, turning intention into action", "reversed": "scattered energy, manipulation, unused potential"},
    {"name": "The High Priestess", "upright": "intuition, inner knowing, patience", "reversed": "confusion, secrets, ignoring intuition"},
    {"name": "The Empress", "upright": "care, growth, emotional warmth", "reversed": "overgiving, dependence, blocked growth"},
    {"name": "The Emperor", "upright": "structure, boundaries, stability", "reversed": "control, rigidity, lack of grounding"},
    {"name": "The Hierophant", "upright": "tradition, guidance, shared values", "reversed": "questioning rules, misalignment, independence"},
    {"name": "The Lovers", "upright": "connection, choice, alignment", "reversed": "misalignment, difficult choices, mixed values"},
    {"name": "The Chariot", "upright": "direction, willpower, movement", "reversed": "loss of control, pressure, stalled progress"},
    {"name": "Strength", "upright": "courage, patience, emotional control", "reversed": "self-doubt, force, emotional exhaustion"},
    {"name": "The Hermit", "upright": "reflection, solitude, inner clarity", "reversed": "isolation, avoidance, loneliness"},
    {"name": "Wheel of Fortune", "upright": "change, cycles, turning point", "reversed": "resistance to change, repeated patterns, instability"},
    {"name": "Justice", "upright": "fairness, truth, accountability", "reversed": "avoidance, imbalance, unclear responsibility"},
    {"name": "The Hanged Man", "upright": "pause, surrender, new perspective", "reversed": "stagnation, resistance, feeling stuck"},
    {"name": "Death", "upright": "ending, transformation, release", "reversed": "fear of change, delayed closure, holding on"},
    {"name": "Temperance", "upright": "balance, moderation, healing", "reversed": "imbalance, impatience, emotional extremes"},
    {"name": "The Devil", "upright": "attachment, temptation, unhealthy patterns", "reversed": "release, awareness, breaking patterns"},
    {"name": "The Tower", "upright": "disruption, truth revealed, sudden change", "reversed": "avoiding conflict, delayed collapse, quiet realization"},
    {"name": "The Star", "upright": "hope, renewal, trust", "reversed": "discouragement, doubt, loss of faith"},
    {"name": "The Moon", "upright": "uncertainty, illusion, emotional fog", "reversed": "clarity emerging, truth surfacing, reduced confusion"},
    {"name": "The Sun", "upright": "joy, openness, confidence", "reversed": "temporary doubt, hidden worries, delayed happiness"},
    {"name": "Judgement", "upright": "awakening, reflection, decision", "reversed": "self-criticism, avoidance, unfinished lessons"},
    {"name": "The World", "upright": "completion, integration, fulfillment", "reversed": "unfinished business, delay, lack of closure"},
]


def draw_cards(spread_type, question, seed=None):
    if spread_type not in SPREADS:
        raise ValueError(
            f"Unsupported spread type: {spread_type}. "
            f"Supported types are: {', '.join(SPREADS.keys())}."
        )

    rng = random.Random(seed)
    positions = SPREADS[spread_type]

    if len(positions) > len(TAROT_DECK):
        raise ValueError("Spread requires more cards than the deck contains.")

    selected_cards = rng.sample(TAROT_DECK, len(positions))

    cards = []
    for position, card in zip(positions, selected_cards):
        orientation = rng.choice(["upright", "reversed"])
        cards.append({
            "position": position,
            "name": card["name"],
            "orientation": orientation,
            "keywords": card[orientation],
        })

    return {
        "question": question,
        "spread_type": spread_type,
        "drawn_at": datetime.now().isoformat(timespec="seconds"),
        "seed": seed,
        "cards": cards,
        "note": "For entertainment and self-reflection only. Not a factual prediction or professional advice."
    }


def main():
    parser = argparse.ArgumentParser(
        description="Draw unique tarot cards for a reflective tarot spread."
    )
    parser.add_argument(
        "--question",
        required=True,
        help="The user's reflection question."
    )
    parser.add_argument(
        "--spread",
        default="three-card",
        choices=list(SPREADS.keys()),
        help="Spread type: one-card, three-card, or decision."
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducible demo results."
    )

    args = parser.parse_args()

    result = draw_cards(
        spread_type=args.spread,
        question=args.question,
        seed=args.seed
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

    