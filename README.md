Built an end-to-end data engineering project that extracts video statistics from the YouTube Data API, orchestrates the ETL pipeline with Dagster, and serves the processed data through a Django web application. The stack is deployed on Microsoft Azure with a Neon serverless PostgreSQL database, demonstrating skills in data engineering, backend web development, and cloud deployment.

**STEPS TO CREATE A REACHABLE URL**
Using Azure VM

**Set up the server:**

	sudo apt update && sudo apt upgrade -y
	sudo apt install -y python3-pip python3-venv nginx git curl
  

**Clone your projects**

	cd ~
	https://github.com/ofaronbi/Youtube-API-ETL_Front_End


**Create virtual environments**

	cd ~/Youtube-API-ETL_Front_End
	python3 -m venv .venv
	source venv/bin/activate
	pip install -r requirements.txt gunicorn
	pip install gunicorn
	deactivate


**Configure systemd services**

	sudo nano /etc/systemd/system/django.service
	
	[Unit]
	Description=Django Gunicorn
	After=network.target
	
	[Service]
	User=ofaronbi
	WorkingDirectory=/home/ofaronbi/Youtube-API-ETL_Front_End
	ExecStart=/home/ofaronbi/Youtube-API-ETL_Front_End/.venv/bin/gunicorn config.wsgi:application --bind 127.0.0.1:8000 --workers 2
	Restart=on-failure
	Environment=DATABASE_URL=postgresql://neondb_owner:pass@ep-xxx.neon.tech/YouTube_video_statistic?sslmode=require&channel_binding=require
	Environment=DJANGO_SETTINGS_MODULE=config.settings
	
	[Install]
	WantedBy=multi-user.target



**Enable service**

	sudo systemctl daemon-reload
	sudo systemctl enable django
	sudo systemctl start django
	
	# Check they're running
	sudo systemctl status django


**Configure Nginx**

	sudo nano /etc/nginx/sites-available/django
	
	#Django — your main domain
	server {
    listen 80;
    server_name vm ip address;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /home/ofaronbi/Youtube-API-ETL_Front_End/staticfiles/;
    }
		}


**Enable the config & restart Nginx**

	sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/
	sudo nginx -t
	sudo systemctl restart nginx


**Verify everything is working**

	# Check all services
	sudo systemctl status django nginx
	
	# Watch Dagster logs live
	sudo journalctl -u django -f
