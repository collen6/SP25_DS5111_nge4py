#!/bin/bash

#!/bin/bash

echo "🔄 Updating package lists..."
sudo apt update -y

echo "🛠 Installing required packages..."
sudo apt install -y make python3.12-venv tree

echo "✅ Setup complete!"
