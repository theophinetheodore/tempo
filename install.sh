#!/bin/bash

current_dir=$(pwd)

sudo cp -ar "$current_dir" /usr/lib/

echo -e '#!/bin/bash\npython /usr/lib/tempo/main.py' | sudo tee -a /usr/bin/tempo> /dev/null
sudo chmod +x /usr/bin/tempo

sudo cp /usr/lib/tempo/tempo.desktop /usr/share/applications
sudo chmod +x /usr/share/applications/tempo.desktop

echo "Installation complete."
