#!/bin/bash
sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd
sed -ri 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

/usr/sbin/sshd
while true; do
    echo "sleeping 60"
    sleep 60
done
