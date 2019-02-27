from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.html': CommonMarkParser,
}

source_suffix = ['.rst', '.md', '.html']
