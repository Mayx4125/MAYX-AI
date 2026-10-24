
import random

STORIES = [
    {
        "title": "The Mysterious Door",
        "story": (
            "One night, Alex found a tiny door "
            "hidden behind an old bookshelf. "
            "He opened it and saw a glowing city "
            "inside the wall. Suddenly, a little "
            "robot waved at him and whispered, "
            '"We have been waiting for you."'
        )
    },
    {
        "title": "The Last Dragon",
        "story": (
            "Mia discovered a dragon egg in the forest. "
            "When it hatched, a tiny blue dragon flew "
            "around her head. It dropped a golden key "
            "into her hand. Far away, a castle began "
            "to glow."
        )
    },
    {
        "title": "The Time Machine",
        "story": (
            "Sam found a strange watch in his attic. "
            "When he pressed its button, the whole "
            "world stopped. A message appeared: "
            '"You have sixty seconds to change history."'
        )
    }
]


def main():
    story = random.choice(STORIES)

    print("=" * 40)
    print("MAYX AI - STORY GENERATOR")
    print("=" * 40)
    print()
    print("TITLE:", story["title"])
    print()
    print(story["story"])
    print()
    print("Subtitles: OFF")
    print("Story generated successfully!")


if __name__ == "__main__":
    main()

