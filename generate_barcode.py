import barcode
from barcode.writer import ImageWriter
import sys

# Get URL from command line argument or prompt user
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("Enter your bit.ly URL (or any URL): ").strip()

# Validate URL
if not url:
    print("Error: URL cannot be empty!")
    sys.exit(1)

# Generate a filename from the URL (replace special characters)
safe_filename = "".join(c if c.isalnum() or c in ('-', '_') else '_' for c in url)
safe_filename = safe_filename[:50]  # Limit filename length

# Create a Code128 barcode for the URL
barcode_class = barcode.get_barcode_class('code128')
my_barcode = barcode_class(url, writer=ImageWriter())

# Save the barcode
output_filename = f"{safe_filename}_barcode"
my_barcode.save(output_filename)

print(f"Barcode generated successfully as: {output_filename}.png")
print(f"Barcode contains: {url}")

