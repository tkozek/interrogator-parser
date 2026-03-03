from pathlib import Path



for file in Path.cwd().glob("*.txt"):
    print("Deleting: ", file)
    file.unlink()