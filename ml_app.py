import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from app import create_app


if __name__ == "__main__":
    app = create_app()
    app.run()
