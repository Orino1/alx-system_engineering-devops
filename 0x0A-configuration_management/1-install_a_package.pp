# Define a package resource for Flask
package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify a command to print Flask version
exec { 'print_flask_version':
  command     => '/usr/bin/pip3 show Flask | grep Version',
  path        => ['/usr/bin', '/usr/local/bin'],
  refreshonly => true,
  notify      => Exec['print_flask_version'],
}

