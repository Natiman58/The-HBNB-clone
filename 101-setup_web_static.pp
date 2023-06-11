# Automated deployment using puppet
# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create directories
file { ['/data/', '/data/web_static/', '/data/web_static/releases/', '/data/web_static/shared/', '/data/web_static/releases/test/']:
  ensure => directory,
}

# Create fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'This is a fake HTML file',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

# Set ownership recursively
file { '/data/':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80;
                server_name mydomainname.tech;

                location /hbnb_static/ {
                  alias /data/web_static/current/;
                }
              }",
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

# Clean up old archives
define clean_archives($number) {
  exec { "clean_archives_${number}":
    command => "ls -t /data/web_static/releases/ | tail -n +$(( ${number} + 1 )) | xargs rm -rf",
  }
}

# Call the clean_archives defined type with the desired number of archives to keep
clean_archives { '2':
  number => 2,
}

https://www.hackerrank.com/tests/djh857dk29p/