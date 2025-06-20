import zipfile
from pathlib import Path

# 📁 Path to your zip files
zip_dir = Path(r"you path")  # <- Update as needed
output_dir = zip_dir / "unzipped_all"
output_dir.mkdir(exist_ok=True)

# 🔁 Extract all ZIPs, preserving full structure
for zip_path in sorted(zip_dir.glob("*.zip")):
    print(f"📦 Processing: {zip_path.name}")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for member in zip_ref.namelist():
                output_path = output_dir / member

                if member.endswith('/'):
                    output_path.mkdir(parents=True, exist_ok=True)
                else:
                    if not output_path.exists():
                        output_path.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            with zip_ref.open(member) as source, open(output_path, 'wb') as target:
                                target.write(source.read())
                        except Exception as file_err:
                            print(f"❌ Error extracting file: {member} from {zip_path.name} → {file_err}")
                    else:
                        print(f"⚠️ Skipping existing file: {output_path}")
    
    except zipfile.BadZipFile:
        print(f"❌ Bad ZIP file (corrupt or incomplete): {zip_path.name}")
    except Exception as e:
        print(f"❌ Unexpected error with {zip_path.name}: {e}")

print("\n✅ Extraction complete. Folder structure preserved. Errors (if any) shown above.")
