# LinkReviver

A small command-line tool that checks a list of URLs and reports which ones are alive, dead, or redirecting. Dead links get a Wayback Machine fallback so you can still find an archived copy.

## Features

- Reads URLs from a text file (one per line, `#` for comments)
- Checks each link with a 10-second timeout
- Detects: alive links, dead links (4xx/5xx), redirects, and connection errors
- Reports the redirect target for 3xx responses
- Adds a Wayback Machine archive link for dead URLs
- Writes a Markdown report to `report.md`
- Prints a summary of alive vs. dead links

## Used libraries:

- requests
