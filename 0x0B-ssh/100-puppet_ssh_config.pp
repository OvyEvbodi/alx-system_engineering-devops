# configure a server

file_line {'no_password_authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => '  IdentityFile ~/.ssh/school'
}

file_line { 'school_identity_file':
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => '  PasswordAuthentication no'
}
