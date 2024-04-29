# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a custom fact to fetch the hostname
Facter.add('nginx_hostname') do
  setcode do
    Facter::Core::Execution.execute('hostname')
  end
end

# Set up Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "# Default server configuration\n\nserver {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\n\tserver_name _;\n\n\tlocation / {\n\t\ttry_files $uri $uri/ =404;\n\t}\n\n\t# Add custom HTTP header\n\tadd_header X-Served-By ${::nginx_hostname};\n}\n",
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

