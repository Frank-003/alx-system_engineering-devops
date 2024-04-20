#!/usr/bin/env bash
# using puppet to connect without password

file { '/home/your_username/.ssh/config':
    ensure => file,
    owner  => 'your_username',
    group  => 'your_group',
    mode   => '0600',
    content => "Host your_server_address\n\
                \tIdentityFile ~/.ssh/school\n\
                \tPasswordAuthentication no\n",
}
