cat << 'EOF' > ~/setup.sh
#!/usr/bin/env bash

# Install essentials
sudo yum install -y git vim python3 jq docker docker-compose

# Start docker service
sudo service docker start
EOF

chmod +x ~/setup.sh
