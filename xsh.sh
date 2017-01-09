#!/usr/bin/expect
puts $argc
set host_name [lindex $argv 0]
puts $host_name
set user root
set host_ip 192.168.107.52
spawn ssh $user@$host_ip
expect {
    "password:" {send "aaaaaa\r"}
    }
expect "*#"
interact
