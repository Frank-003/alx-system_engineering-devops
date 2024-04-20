#The code that will create a file name called school inside /tmp directory
file { '/tmp/school':
ensure => file,
content => 'I love Puppet',
Permission mode => '0744',
owner => 'www-data',
group => 'www-data',
}
