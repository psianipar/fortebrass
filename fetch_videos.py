import urllib.request
import xml.etree.ElementTree as ET
import json
import os

# Paste your copied YouTube Channel ID here
CHANNEL_ID = "UClKoxdZNJA7MvjbUui5XXaA"
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

try:
    # Fetch the RSS feed
    response = urllib.request.urlopen(RSS_URL)
    xml_data = response.read()
    
    root = ET.fromstring(xml_data)
    
    # Namespaces used by YouTube RSS format
    ns = {
        'atom': 'http://www.w3.org/2005/Atom',
        'yt': 'http://www.youtube.com/xml/schemas/2015'
    }
    
    videos = []
    
    # Extract the 6 most recent videos
    for entry in root.findall('atom:entry', ns)[:6]:
        video_id = entry.find('yt:videoId', ns).text
        title = entry.find('atom:title', ns).text
        link = entry.find('atom:link', ns).attrib['href']
        thumbnail = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        
        videos.append({
            "id": video_id,
            "title": title,
            "link": link,
            "thumbnail": thumbnail
        })
        
    # Write to a local JSON file
    with open('videos.json', 'w', encoding='utf-8') as f:
        json.dump(videos, f, indent=2, ensure_ascii=False)
        
    print("Successfully compiled latest videos to videos.json")
except Exception as e:
    print(f"Error executing feed automation: {e}")
