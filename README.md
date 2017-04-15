Namecheap Dynamic DNS updater
-----------------------------

Python 3 script for checking if the hosts public IP has changed (using ifconfig.io) and updates dynamic DNS on Namecheap if necessary.

Add your domains settings to `config.ini` according to the provided example.

| Key           | Value                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------|
| host          | `@` for base domain<br> `subdomain` for subdomain (e.g. `test` if full domain is `test.example.com`) |
| domain        | Domain name (e.g. `example.com`)                                                                   |
| ddns_password | Dynamic DNS Password, **NOT** your Namecheap account password                                          |

The program checks the hosts public IP every 10 minutes (configurable in `ddns.py`). Start the program by executing

    python ddns.py
