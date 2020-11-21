#!/bin/bash
# Run this script to yield maximum performance from the Jetson nano.
# First we shall be mounting the 4GB swap. This substitutes disk space for RAM memory when real RAM fills up. Might make it slower, but it generally helpful when more space is required. 
sudo systemctl disable nvzramconfig.service.
sudo fallocate -l 4G /mnt/4GB.swap
sudo chmod 600 /mnt/4GB.swap
sudo /etc/fstab
# Add "/mnt/4GB. swap swap swap defaults 0 0" at the end of the file. Reboot the system.
free -m 
# Check whether 4GB of swap is alloted.
# Set Nano to use maximum power capacity.
sudo nvpmodel -m 0
$ sudo jetson_clocks
