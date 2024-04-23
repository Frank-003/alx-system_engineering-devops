# File: nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80;
        server_name _;
        root /var/www/html;

        location / {
            return 200 'Hello World!';
        }

        location /redirect_me {
            return 301 /;
        }
    }
  ",
  require => Package['nginx'],
}

# Enable Nginx site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx service if configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}

