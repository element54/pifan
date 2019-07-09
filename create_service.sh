#!/bin/sh

HERE=$( cd  $(dirname "${BASH_SOURCE:=$0}") && pwd)
cp -f "$HERE/pifan.service" "/lib/systemd/system"
chown "root:root /lib/systemd/system/pifan.service"
systemctl daemon-reload
systemctl enable pifan.service
systemctl start pifan.service
