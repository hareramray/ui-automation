import os

class FileAgent:
    def __init__(self, filename="output.txt"):
        self.filename = filename
        self.filepath = os.path.join(os.getcwd(), self.filename)

    def write_content(self, content: str):
        try:
            with open(self.filepath, 'w') as f:
                f.write(content)
            print(f"✅ File '{self.filename}' created and content written successfully.")
        except Exception as e:
            print(f"❌ Failed to write to file: {e}")

