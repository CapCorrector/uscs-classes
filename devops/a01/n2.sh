#!/bin/bash
echo "Memory Statistics" > /vagrant/n2-results.txt
sudo free >> /vagrant/n2-results.txt
echo "HDD Statistics" >> /vagrant/n2-results.txt
df -h >> /vagrant/n2-results.txt
echo "CPU Statistics" >> /vagrant/n2-results.txt
top -bn 1 | grep Cpu 2>&1 1>> /vagrant/n2-results.txt
