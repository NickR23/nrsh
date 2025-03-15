import os
import markdown

post_dir = "posts"
output_dir = "generated_posts"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        with open(f"{post_dir}/{filename}", "r", encoding="utf-8") as f:
            md_content = f.read()
            html_content = markdown.markdown(md_content)

        new_filename = filename.replace(".md", ".html")
        with open(f"{output_dir}/{new_filename}", "w", encoding="utf-8") as f:
            f.write(f"<html><body>{html_content}</body></html>")

print("Markdown converted to HTML!")
