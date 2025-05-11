import json
from image_generator import generate_card
from insta_poster import post_image

def run_daily_job():
    with open("data/words.json") as f:
        words = json.load(f)
    with open("state.json") as f:
        state = json.load(f)

    word_data = words[state["index"]]
    generate_card(word_data)
    caption = f"📖 Word of the Day\n\nWord: {word_data['word']}\nMeaning: {word_data['meaning']}\nExample: {word_data['example']}"
    post_image("images/daily_post.png", caption)

    # Update state
    state["index"] = (state["index"] + 1) % len(words)
    with open("state.json", "w") as f:
        json.dump(state, f)
