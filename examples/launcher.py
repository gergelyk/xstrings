import os
import xstrings
import deepl

# This code instructs Python how to parse the code with user-defined string literals.
# It must be executed before we import user-defined code.


# === Example1 ===
#
# Default encoding name ('x-string') applies here.

transforms = {
    'a': lambda t: t.lower(),
    'A': lambda t: t.upper()}

xstrings.register(transforms)


# === Example2 ===
#
# x-strings allows for registring multiple encodings and multiple prefixes.

sys_lang = os.getenv('LANG', 'en').split('.')[0].split('_')[0]

def translate(text, lang):
    if lang == 'orig':
        return text
    return deepl.translate(source_language="en", target_language=lang, text=text)

transforms = {'t': lambda text: translate(text, sys_lang)}
xstrings.register(transforms, coding="lang_auto")

# Transform below takes additional arg, `lang`, captured by the regex.
# Multiple capture groups correspond to multiple args.

transforms = {'t': lambda text, lang: translate(text, lang)}
xstrings.register(transforms, coding="lang_(.+)")


# ========================

import example1
import example2

