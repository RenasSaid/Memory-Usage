To install and run this service, follow these steps:

Files/Directories:
1. Put memory_usage.service in /etc/systemd/system/
2. Change values in .memory_usage.conf as you want them(currently values are set to 1 Megabyte and 5 minutes).
3. Put .memory_usage.conf in /etc/systemd/system/
4. Put memory_usage.py in /usr/bin/
5. Run: sudo chmod 664 /etc/systemd/system/memory_usage.service
6. Run: sudo systemctl enable memory_usage
7. Run: sudo systemctl daemon-reload

	* If prior steps has been followed, the service should start at next system reboot.
	* The log file will automatically created in /var/log/memory_usage.log
	* Values for memory limit and time can be changed in /etc/systemd/system/.memory_usage.conf

----------------

	For manual testing:

	* Run: sudo systemctl start memory_usage to start service manually

	* Run: python3 /usr/bin/memory_usage.py <memory_limit> <minutes> to test different values
	* Run: sudo rm /var/log/memory_usage.log to empty log file
