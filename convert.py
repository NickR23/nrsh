import os
import markdown

post_dir = "posts"
output_dir = "generated_posts"

os.makedirs(output_dir, exist_ok=True)

# Load the HTML template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        with open(f"{post_dir}/{filename}", "r", encoding="utf-8") as f:
            md_content = f.read()
            html_content = markdown.markdown(md_content)

        # Replace the placeholder in the template with the converted HTML
        final_html = template.replace("<!-- Markdown content will be inserted here -->", html_content)

        new_filename = filename.replace(".md", ".html")
        with open(f"{output_dir}/{new_filename}", "w", encoding="utf-8") as f:
            f.write(final_html)
