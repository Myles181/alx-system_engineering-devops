#Using Puppet, install flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install flask':
  command => 'pip3 install flask==2.1.0',
  path    => '/usr/bin',
  unless  => 'pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}

