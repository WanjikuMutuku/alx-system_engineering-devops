
# Fix file permissions for Apache
file { '/var/www/html':
  ensure => directory,
  owner => 'www-data',
  group => 'www-data',
  mode => '0755',
}

# Restart Apache after fixing permissions
exec { 'restart_apache':
  command => '/etc/init.d/apache2 restart',
  refreshonly => true,
}
