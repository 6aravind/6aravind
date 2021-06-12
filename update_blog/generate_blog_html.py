
# Import Libraries
import pandas as pd

# Config
DATA_FILE = 'all_posts.csv'
HTML_PLACEHOLDER = 'index placeholder.html'


# Generate blog html for a post
def get_blog_html(title, postURL, tags, date, summary, imgURL):
    return f'''
            <header class="card">
                <img src="{imgURL}" alt="" class="card-image">
                <h2 class="card-title">{title}</h2>
                <span class="card-summary">{summary}</span>
                <div class="card-details">
                    <span class="card-date">{date[:-12]}</span>
                    <a href="{postURL}" class="card-button" target="_blank">Read More</a>
                </div>

                <span class="card-tags">
                    <ul>
                        {"".join([' <li> ' + tag + ' </li> '  for tag in tags.split(",")])}
                    </ul>
                </span>
            </header>
'''

# Insert the generated html for all blog posts and place it inside HTML placeholder
def combine_blog_htmls(values, file = HTML_PLACEHOLDER):
    blogs_html = "\n".join(get_blog_html(*val) for val in values)
    with open(file, 'r') as f:
        html_base = f.read()
    final_html = html_base.replace('BLOGS', blogs_html)
    with open('../index.html', 'w') as f:
        f.write(final_html)


if __name__ == "__main__":
    # Read the post meta data
    df = pd.read_csv(DATA_FILE)
    # Generate HTML
    combine_blog_htmls(df.values)