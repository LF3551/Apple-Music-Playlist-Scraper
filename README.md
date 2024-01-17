# Apple Music Playlist Scraper

## Introduction
This Python script efficiently extracts song data from Apple Music's "Today's Hits" playlist. Utilizing BeautifulSoup and requests, it fetches details like song titles and artist names, organizing them into a readable JSON format. This tool is perfect for music enthusiasts and data analysts interested in music trends.

## Technology Stack
- Python
- BeautifulSoup
- requests
- JSON

## Installation
Before running the script, ensure Python is installed on your system. Then, install the necessary libraries using the following commands:
```bash
pip install requests
pip install beautifulsoup4 
```

## Usage
Run the script using Python. The output will be a neatly formatted JSON file containing the playlist's songs and artists. To execute the script, navigate to its directory and run:

python apple_music_scraper.py

### Example Output

Here's a sample of the output you can expect:
```
[
    {
        "Artist": "Artist Name 1",
        "Song": "Song Title 1"
    },
    {
        "Artist": "Artist Name 2",
        "Song": "Song Title 2"
    }
    // ... more songs
]
```