# 🧠 AI Blog Generator

A Python-based tool that uses OpenAI’s GPT-4o to generate new blog posts in your personal writing style. It analyzes your past Markdown blog posts, learns your tone and structure, and produces fresh content that feels like you — but doesn’t copy you.

---

## ✨ Features

- 🧵 Learns your tone and structure from existing blog posts
- 🧠 Generates *new*, non-repetitive content using GPT-4o-mini
- 💾 Saves the output as Markdown, ready to publish
- 🔧 Fully customizable prompts and topics
- 🪶 Retains your voice — not just your keywords

---

## 🖥️ Demo

![OpenAI](https://res.cloudinary.com/dcqfs6lkg/image/upload/v1747941203/mariia-shalabaieva-fluoEjpdj60-unsplash_r9gnds.jpg)

---

## 📦 Requirements

- Python 3.8+
- [OpenAI API key](https://platform.openai.com/)
- Packages:
  ```bash
  pip install openai
  ```

---

## 🗂 Folder Structure

```bash
.
├── blog_generator.py       # Main script
├── /current                # Place your existing .md / .mdx files here
├── /generated              # Output folder for AI-generated posts
└── README.md
```

---

## 🛠️ How It Works

1. **Load Old Posts**: Scans `./current` and reads your Markdown files.
2. **Set Your Style**: You define a written "style guide" to shape the AI's voice.
3. **Prompt the AI**: Your style and sample content are fed into GPT-4o-mini.
4. **Generate & Save**: A new blog is created on your chosen topic and saved to `./generated`.

---

## ⚙️ Configuration

Edit the following in `blog_generator.py`:

```python
# Add your OpenAI API key here
openai.api_key = "sk-..."

# Define available blog topics
TOPICS = {
    "bitcoin": "bitcoin",
    "fiat": "fiat money",
    "ai": "AI and the future of tech"
}

# Customize your writing style
STYLE_GUIDE = """
You are a tech-forward blogger with a sharp, principled, anti-hype tone...
"""
```

---

## 🚀 Usage

```bash
python blog_generator.py
```

Follow the prompt to pick a topic, then let the AI cook.

---

## 🧾 License

MIT — free to use, modify, and build on.


## 🙌 Contributions

Pull requests welcome! Open an issue or fork and build.
