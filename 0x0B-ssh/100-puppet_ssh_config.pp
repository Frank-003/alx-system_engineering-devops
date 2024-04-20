#!/usr/bin/env bash
# using puppet to connect without password

file { '/home/www.data/.ssh/config':
    ensure => 'present',
    owner  => 'www.data',
    group  => 'www.data',
    mode   => '0744',
    content => "Host your_server_address\n\
                \tIdentityFile ~/.ssh/school\n\
                \tPasswordAuthentication no\n",
}
