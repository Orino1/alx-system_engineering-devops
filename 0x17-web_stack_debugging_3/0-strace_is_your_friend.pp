# this manifests will fix the wrong extention in the file wp-settings.php to fix our webstack

exec { 'execute_commands':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php ; service apache2 reload',
  path    => 'usr/local/bin:/bin/'
}

