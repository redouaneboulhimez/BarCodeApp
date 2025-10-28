import barcode
from barcode.writer import ImageWriter
import sys


def validate_url(url):
    """Validate that the URL is not empty and has a basic format."""
    if not url:
        return False
    # Basic validation - check if it starts with http or https
    if not (url.startswith('http://') or url.startswith('https://')):
        return False
    return True


def sanitize_filename(url):
    """Generate a safe filename from the URL."""
    # Replace special characters with underscores
    safe_filename = "".join(c if c.isalnum() or c in ('-', '_', '.') else '_' for c in url)
    safe_filename = safe_filename[:50]  # Limit filename length
    return safe_filename


def generate_barcode(url):
    """Generate a Code-128 barcode from the given URL."""
    try:
        # Validate URL
        if not validate_url(url):
            print("Error: Invalid URL format. URL must start with http:// or https://")
            return None
        
        # Generate filename
        safe_filename = sanitize_filename(url)
        output_filename = f"{safe_filename}_barcode"
        
        # Create barcode
        barcode_class = barcode.get_barcode_class('code128')
        my_barcode = barcode_class(url, writer=ImageWriter())
        
        # Save the barcode
        my_barcode.save(output_filename)
        
        print(f"Barcode generated successfully as: {output_filename}.png")
        print(f"Barcode contains: {url}")
        return output_filename
        
    except Exception as e:
        print(f"Error generating barcode: {str(e)}")
        return None


def main():
    """Main function to handle command-line arguments and user input."""
    # Get URL from command line argument or prompt user
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter your bit.ly URL (or any URL): ").strip()
    
    # Generate barcode
    result = generate_barcode(url)
    
    # Exit with error code if generation failed
    if result is None:
        sys.exit(1)


if __name__ == "__main__":
    main()

