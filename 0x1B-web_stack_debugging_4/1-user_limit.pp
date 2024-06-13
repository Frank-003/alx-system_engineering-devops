http {
    ...
    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m use_temp_path=off;

    server {
        ...
        location / {
            proxy_cache my_cache;
            proxy_pass http://holberton hard:your_app_port;
            proxy_cache_valid 200 302 10m;
            proxy_cache_valid 404 1m;
            proxy_cache_bypass $http_cache_control;
        }
    }
}

