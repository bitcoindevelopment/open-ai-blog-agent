import openai
import os
from datetime import datetime

# === CONFIG ===
openai.api_key = "sk-XXX"  # Replace with your actual OpenAI API key

LOCAL_BLOG_DIR = "./current"
OUTPUT_DIR = "./generated"

# Map user-friendly topic keys to full topic names
TOPICS = {
    "bitcoin": "bitcoin",
    "fiat": "fiat money",
    "ai": "AI and the future of tech"
}

STYLE_GUIDE = """
You are a tech-forward blogger with a sharp, principled, anti-hype tone. 
You write like someone who values clarity, historical context, and intelligent resistance to centralized systems 
(like fiat, big tech, or biased AI). Your blog posts are structured with subheads, bullet points, music recs, and 
questions at the end. You cite sources and think in systems.
"""

def load_existing_blogs(max_words=3000):
    content = ""
    for root, dirs, files in os.walk(LOCAL_BLOG_DIR):
        for file in files:
            if file.endswith((".md", ".mdx")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content += f.read() + "\n\n"
                    if len(content.split()) >= max_words:
                        return content[:10000]  # truncate for token safety early
                except Exception as e:
                    print(f"⚠️ Could not read {filepath}: {e}")
    return content[:10000]  # truncate if loop ends naturally

def generate_blog(topic, reference_blogs):
    prompt = (
        f"{STYLE_GUIDE}\n\n"
        f"Here are some example blogs you've written:\n\n{reference_blogs}\n\n"
        f"Now write a completely new blog post about this topic: **{topic}**.\n"
        "Keep the same voice and structure. Do not reuse full paragraphs. Introduce fresh arguments or examples."
    )

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You're a sharp and principled blog-writing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.85
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ Error generating blog post: {e}")
        return None

def save_blog(title, content):
    if not content:
        print("❌ No content to save.")
        return
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{title.replace(' ', '_').lower()}_{datetime.now().strftime('%Y%m%d')}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Blog saved: {filepath}")
    except Exception as e:
        print(f"❌ Failed to save blog: {e}")

# === MAIN ===
if __name__ == "__main__":
    print("Available topics:", ", ".join(TOPICS.keys()))
    topic_input = input("Pick a topic (bitcoin / fiat / AI): ").strip().lower()
    
    if topic_input not in TOPICS:
        print("❌ Invalid topic. Please choose from:", ", ".join(TOPICS.keys()))
        exit()

    topic = TOPICS[topic_input]
    print(f"Loading reference blogs from {LOCAL_BLOG_DIR}...")
    reference_blogs = load_existing_blogs()
    print("Generating blog post...")
    new_blog = generate_blog(topic, reference_blogs)
    if new_blog:
        title = f"New Thoughts on {topic_input.title()}"
        save_blog(title, new_blog)
    else:
        print("❌ Blog generation failed.")
