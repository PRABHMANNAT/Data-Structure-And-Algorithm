from stringlab.api import compare
from stringlab.palindrome import longest_palindrome
from workbench.validation import text

def run(data):
    source=text(data,'text',limit=6000);pattern=text(data,'pattern',limit=1000)
    if not pattern:raise ValueError('Enter a nonempty pattern')
    results=compare(source,pattern)
    return dict(text=source,pattern=pattern,positions=list(results['kmp'].positions),
                algorithms=[result.as_dict() for result in results.values()],palindrome=longest_palindrome(source))
