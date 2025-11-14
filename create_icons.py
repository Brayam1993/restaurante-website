#!/usr/bin/env python3
"""
Generate PNG icons for the restaurant website
"""
try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Pillow not installed. Installing...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'Pillow'])
    from PIL import Image, ImageDraw

# Icon definitions: (filename, color, shape_type, style_details)
icons = {
    'phone.png': {
        'bg_color': (0, 0, 0),
        'size': 32,
    },
    'location.png': {
        'bg_color': (0, 0, 0),
        'size': 32,
    },
    'envelope.png': {
        'bg_color': (0, 0, 0),
        'size': 32,
    },
    'facebook.png': {
        'bg_color': (0, 0, 0),
        'size': 32,
    },
    'twitter.png': {
        'bg_color': (0, 0, 0),
        'size': 32,
    },
    'youtube.png': {
        'bg_color': (0, 0, 0),
        'size': 32,
    },
}

def create_phone_icon(size, color):
    """Create phone icon"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Phone body
    margin = size // 6
    draw.rectangle([margin, margin, size - margin, size - margin], 
                   outline=color, width=2)
    # Phone screen
    draw.rectangle([margin + 2, margin + 2, size - margin - 2, size - margin - 6], 
                   outline=color, width=1)
    
    return img

def create_location_icon(size, color):
    """Create location/map marker icon"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Marker point
    center_x, center_y = size // 2, size // 3
    radius = size // 4
    draw.ellipse([center_x - radius, center_y - radius, 
                  center_x + radius, center_y + radius], 
                 fill=color)
    
    # Marker tail
    points = [(center_x - radius // 2, center_y + radius),
              (center_x + radius // 2, center_y + radius),
              (center_x, size - 2)]
    draw.polygon(points, fill=color)
    
    return img

def create_envelope_icon(size, color):
    """Create envelope/email icon"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    margin = size // 5
    # Envelope body
    draw.rectangle([margin, margin, size - margin, size - margin], 
                   outline=color, width=2)
    # Envelope flap
    draw.line([(margin, margin), (size // 2, size // 2 + margin)], 
              fill=color, width=2)
    draw.line([(size - margin, margin), (size // 2, size // 2 + margin)], 
              fill=color, width=2)
    
    return img

def create_facebook_icon(size, color):
    """Create Facebook 'f' icon"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # F shape
    margin = size // 5
    draw.rectangle([margin, margin, margin + size // 3, size - margin], 
                   fill=color)  # Vertical bar
    draw.rectangle([margin, margin, size - margin, margin + size // 5], 
                   fill=color)  # Top horizontal
    draw.rectangle([margin, margin + size // 3, size - margin // 2, 
                   margin + size // 2], fill=color)  # Middle horizontal
    
    return img

def create_twitter_icon(size, color):
    """Create Twitter bird icon"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Simple bird shape
    center_x, center_y = size // 2, size // 2
    
    # Body
    draw.ellipse([center_x - size // 6, center_y - size // 6,
                  center_x + size // 6, center_y + size // 6], 
                 fill=color)
    # Left wing
    draw.polygon([(center_x - size // 6, center_y),
                  (center_x - size // 2, center_y - size // 8),
                  (center_x - size // 3, center_y + size // 8)], 
                 fill=color)
    # Right wing
    draw.polygon([(center_x + size // 6, center_y),
                  (center_x + size // 2, center_y - size // 8),
                  (center_x + size // 3, center_y + size // 8)], 
                 fill=color)
    
    return img

def create_youtube_icon(size, color):
    """Create YouTube play button icon"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    margin = size // 5
    # Rectangle
    draw.rectangle([margin, margin, size - margin, size - margin], 
                   outline=color, width=2)
    # Play triangle
    play_margin = size // 3
    draw.polygon([(play_margin + 2, play_margin),
                  (play_margin + 2, size - play_margin),
                  (size - play_margin, size // 2)], 
                 fill=color)
    
    return img

# Create icons
icon_creators = {
    'phone.png': create_phone_icon,
    'location.png': create_location_icon,
    'envelope.png': create_envelope_icon,
    'facebook.png': create_facebook_icon,
    'twitter.png': create_twitter_icon,
    'youtube.png': create_youtube_icon,
}

output_dir = r'img\icons'
import os
os.makedirs(output_dir, exist_ok=True)

for filename, creator in icon_creators.items():
    size = 32
    color = (0, 0, 0)  # Black
    img = creator(size, color)
    img.save(os.path.join(output_dir, filename))
    print(f"Created {filename}")

print("\nAll icons created successfully!")
