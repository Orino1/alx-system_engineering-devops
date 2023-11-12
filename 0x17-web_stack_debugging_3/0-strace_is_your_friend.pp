# this manifests will create the file index.html to fix our webstack

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'hello',
  mode    => '0644',
}

