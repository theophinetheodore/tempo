#!/bin/bash

current_dir=$(pwd)

cp -ar "$current_dir" /usr/lib/

echo -e '#!/bin/bash\npython /usr/lib/tempo/main.py' > /usr/bin/tempo
chmod +x /usr/bin/tempo

cp /usr/lib/tempo/tempo.desktop /usr/share/applications
chmod +x /usr/share/applications/tempo.desktop

echo "Installation complete."
