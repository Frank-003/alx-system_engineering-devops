#!/usr/bin/env bash
# using puppet to connect without password

file { '/etc/ssh/.ssh/config':
    ensure => present
}

file_line {'Turn off password auth':
    path    => '/etc/ssh/.ssh/config',
    line    => 'PasswordAuthentication no',
    match   => '^#PasswordAuthecation',
}

file_line {'Declare identity file',
    path    => '/etc/ssh/.ssh/config',
    line    => 'IdentityFile ~/.ssh/school',
    match   => '^#Identityfile',

