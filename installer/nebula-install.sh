#!/bin/bash
# NebulaOS Installer (Debian-based)
# This is a starter stub for installing the supervisor and web dashboard

set -e

echo "Starting NebulaOS installation..."

# Update and install Python
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git curl

# Create virtual environment
python3 -m venv /opt/nebulaos/venv
source /opt/nebulaos/venv/bin/activate

# Install backend dependencies
pip install --upgrade pip
pip install -r /opt/nebulaos/supervisor/requirements.txt

echo "NebulaOS Supervisor installed."

# TODO: Install web dashboard, optional GUI, systemd service
echo "Installer stub complete. Implement full install steps in the future."
