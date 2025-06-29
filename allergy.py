import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# --- CONFIGURATION ---
INPUT_FILE       = 'Option_1__Comma-Delimited_Allergies.csv'
NAME_COL         = 'Name'
ALLERGY_COL      = 'Allergy'
OUTPUT_DIR       = 'stickers'

# 4" × 3" at 300 DPI → 1200×900 px
IMG_WIDTH        = 1200
IMG_HEIGHT       = 900

BORDER_WIDTH     = 6
BG_COLOR         = 'white'
BORDER_COLOR     = 'black'

# The desired font sizes you declared
NAME_FONT_SZ     = 150
ALLERGY_FONT_SZ  = 80

# --- SCRIPT ---

def find_font():
    """Tries to find a common system font, returns None if not found."""
    # List of common fonts to search for on any system
    font_paths = [
        'arial.ttf',                # Windows
        'DejaVuSans.ttf',           # Linux
        'Helvetica.ttf',            # macOS (often available)
        'Arial.ttf',                # macOS / Windows (alternative case)
        'Verdana.ttf',
    ]
    for font_name in font_paths:
        try:
            # The 'ImageFont.truetype' function will search default system font paths
            ImageFont.truetype(font_name, size=10)
            return font_name
        except IOError:
            continue
    return None

# --- PREP ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data & fill missing allergies
df = pd.read_csv(INPUT_FILE)
df[ALLERGY_COL] = df[ALLERGY_COL].fillna('No allergy')

# Automatically find a font and load it with the desired sizes
found_font_path = find_font()
if found_font_path:
    print(f"✓ Automatically found and using font: {found_font_path}")
    name_font    = ImageFont.truetype(found_font_path, NAME_FONT_SZ)
    allergy_font = ImageFont.truetype(found_font_path, ALLERGY_FONT_SZ)
else:
    print("⚠ Warning: No common system fonts found. Falling back to the small default font.")
    name_font    = ImageFont.load_default()
    allergy_font = ImageFont.load_default()

def text_size(draw, text, font):
    """Calculates the width and height of a string of text."""
    bbox = draw.textbbox((0, 0), text, font=font)
    return (bbox[2] - bbox[0], bbox[3] - bbox[1])

# --- GENERATE STICKERS ---
for idx, row in df.iterrows():
    name = str(row[NAME_COL]).strip()
    raw_allergies  = str(row[ALLERGY_COL]).strip()

    if not name:
        continue

    # Build bullet list
    if raw_allergies.lower() in ('none', 'no allergy', ''):
        bullets = ["• No allergy"]
    else:
        items = [a.strip() for a in raw_allergies.split(',') if a.strip()]
        bullets = [f"• {a}" for a in items]

    # Create canvas
    img  = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Draw border
    for off in range(BORDER_WIDTH):
        draw.rectangle(
            [off, off, IMG_WIDTH - 1 - off, IMG_HEIGHT - 1 - off],
            outline=BORDER_COLOR
        )

    # Draw name (centered in top portion)
    w_name, h_name = text_size(draw, name, name_font)
    x_name = (IMG_WIDTH - w_name) / 2
    y_name = (IMG_HEIGHT * 0.25) - (h_name / 2)
    draw.text((x_name, y_name), name, fill='black', font=name_font)

    # Draw "Allergy:" label
    label = "Allergy:"
    w_lab, h_lab = text_size(draw, label, allergy_font)
    x_lab = (IMG_WIDTH - w_lab) / 2
    y_lab = IMG_HEIGHT * 0.48
    draw.text((x_lab, y_lab), label, fill='black', font=allergy_font)

    # Draw bullet points
    y_start = y_lab + h_lab + 20
    for line in bullets:
        w_ln, h_ln = text_size(draw, line, allergy_font)
        x_ln = (IMG_WIDTH - w_ln) / 2
        draw.text((x_ln, y_start), line, fill='black', font=allergy_font)
        y_start += h_ln + 15

    # Save out
    safe_name = "".join(c for c in name if c.isalnum()).rstrip()
    output_path  = os.path.join(OUTPUT_DIR, f"sticker_{idx+1}_{safe_name}.png")
    img.save(output_path)
    print(f"→ Saved: {output_path}")

print("\nAll stickers generated.")