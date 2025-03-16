import os
from markdown_it import MarkdownIt
from mdit_py_plugins.tasklists import tasklists_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.anchors import anchors_plugin

post_dir = "posts"
output_dir = "generated_posts"

os.makedirs(output_dir, exist_ok=True)

with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

md = (
    MarkdownIt('commonmark', {'breaks': True, 'html': True})
    .use(tasklists_plugin)
    .use(footnote_plugin)
    .use(front_matter_plugin)
    .use(anchors_plugin)
    .enable('table')
    .enable('strikethrough')
)

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        with open(f"{post_dir}/{filename}", "r", encoding="utf-8") as f:
            md_content = f.read()
            html_content = md.render(md_content)
        final_html = template.replace("<!-- Markdown content will be inserted here -->", html_content)
        new_filename = filename.replace(".md", ".html")
        with open(f"{output_dir}/{new_filename}", "w", encoding="utf-8") as f:
            f.write(final_html)
