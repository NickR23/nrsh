import os
import re
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
            cleaned_lines = []
            img_sizes = {}
            
            # You can add html comments to markdown like
            # <!-- img:width= px -->
            # This is kind of a hacky workaround tho.
            # TODO find a better way to convert image sizes from md -> html
            # ?Is this implemented in the markdown renderer?
            lines = md_content.split('\n')
            i = 0
            while i < len(lines):
                line = lines[i]
                if '<!-- img:width=' in line and i < len(lines) - 1:
                    # Extract width from comment
                    width = line.split('<!-- img:width=')[1].split('px -->')[0]
                    # Check if the next line contains an image
                    next_line = lines[i+1]
                    if next_line.strip().startswith('!['):
                        # Extract image path
                        img_match = re.search(r'!\[.*?\]\((.*?)\)', next_line)
                        if img_match:
                            img_path = img_match.group(1)
                            img_sizes[img_path] = width
                            # Skip this comment line
                            i += 1
                            cleaned_lines.append(next_line)
                else:
                    cleaned_lines.append(line)
                i += 1
            
            clean_md_content = '\n'.join(cleaned_lines)
            clean_md_content = clean_md_content.replace('](/static/', '](../static/')
            html_content = md.render(clean_md_content)
            
            for img_path, width in img_sizes.items():
                fixed_path = img_path.replace('/static/', '../static/')
                html_content = html_content.replace(
                    f'<img src="{fixed_path}" alt=',
                    f'<img src="{fixed_path}" width="{width}" alt='
                )

        final_html = template.replace("<!-- MARKDOWN HTML MUTATOR PLACEHOLDER -->", html_content)
        new_filename = filename.replace(".md", ".html")
        with open(f"{output_dir}/{new_filename}", "w", encoding="utf-8") as f:
            f.write(final_html)
