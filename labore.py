from pathlib import Path

# Assuming locale_dir is already defined as a Path object
locale_dir = Path("/path/to/locale")

# Construct the file path using the / operator
po_file_path = locale_dir / "LC_MESSAGES" / "messages.po"

# Now po_file_path contains the combined path
print(po_file_path)
