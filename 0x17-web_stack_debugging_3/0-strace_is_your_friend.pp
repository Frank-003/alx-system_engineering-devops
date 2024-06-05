# 0-strace_is_your_friend.pp

file { '/var/log/apache2':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

service { 'apache2':
  ensure => 'running',
  enable => true,
  subscribe => File['/var/log/apache2'],
}

