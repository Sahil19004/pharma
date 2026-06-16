import html
import re

from django import template
from django.utils.html import strip_tags

register = template.Library()

# Leading bullet markers to strip: •, ·, ‣, ◦, -, *, and stray "bull" leftovers.
_LEADING_BULLET = re.compile(r'^[\s•·‣◦⁃∙>*\-]+')


def _clean(item):
    """Unescape entities and strip any leading bullet/dash markers."""
    item = html.unescape(strip_tags(item))      # &bull; -> •, drop tags
    item = _LEADING_BULLET.sub('', item)         # remove leading bullet glyphs
    return item.strip()


@register.filter
def feature_list(value):
    """Turn a key-features field into a clean list of feature strings.

    Handles three authoring styles transparently:
      * CKEditor bullet/numbered list  -> one item per <li>
      * Paragraphs / <br> separated     -> one item per block
      * Plain text, one feature per line
    """
    if not value:
        return []

    text = str(value)
    items = []

    if '<li' in text.lower():
        for match in re.findall(r'<li[^>]*>(.*?)</li>', text, flags=re.IGNORECASE | re.DOTALL):
            clean = _clean(match)
            if clean:
                items.append(clean)
    else:
        # Normalise block tags / line breaks into newlines, then split.
        text = re.sub(r'</(p|div|h[1-6])>', '\n', text, flags=re.IGNORECASE)
        text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
        text = strip_tags(text)
        for line in text.splitlines():
            clean = _clean(line)
            if clean:
                items.append(clean)

    return items
