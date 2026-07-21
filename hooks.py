import re


def on_page_markdown(markdown, page, config, files):
    site_url = config.get('site_url', '').rstrip('/')
    return markdown.replace('{{ site_url }}', site_url)
