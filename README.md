# dynamic-update-google-domains
Quick dynamic update service for google domains 

Copy dynamic-update.py to /root
Setup dynamic dns in domains.google.com
Add credentials created to dynamic-update.py

copy dynamic-update.service to /etc/systemd/system/
copy dynamix-update.py to /root/

chmod +x dynamic-update.py

systemctl daemon-reload
systemctl start dynamic-update.service
systemctl enable dynamic-update.service
