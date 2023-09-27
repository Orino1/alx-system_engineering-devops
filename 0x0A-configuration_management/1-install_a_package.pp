# Define a package resource for Flask
package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

