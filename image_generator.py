from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_card(word_data, filename="images/daily_post.png"):
    img = Image.new("RGB", (1080, 1080), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    y = 100
    lines = [
        "📖 Word of the Day",
        "",
        f"Word: {word_data['word']}",
        f"Part of Speech: {word_data['part_of_speech']}",
        f"Meaning: {word_data['meaning']}",
        f"Example: {word_data['example']}"
    ]
    for line in lines:
        wrapped = textwrap.fill(line, width=40)
        draw.text((50, y), wrapped, fill="black", font=font)
        y += 60
    img.save(filename)
