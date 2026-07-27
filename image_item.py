from pathlib import Path
import shutil

class ImageItem:

    def __init__(self, title, filepath):
        self.title = title
        self.filepath = Path(filepath)

    def duplicate(self):
        """Create a duplicate of the image."""

        new_name = self.filepath.stem + "_copy" + self.filepath.suffix
        new_path = self.filepath.parent / new_name

        shutil.copy2(self.filepath, new_path)

        return ImageItem(self.title + " Copy", new_path)

    def delete(self):
        """Delete image from disk."""

        if self.filepath.exists():
            self.filepath.unlink()

    def save_as(self, destination):
        """Save a copy somewhere else."""

        shutil.copy2(self.filepath, destination)