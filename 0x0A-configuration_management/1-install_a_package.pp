# Installs flask from pip3

exec { "pip3":
  command => "sudo apt-get install pip3"
}

package { "flask":
  ensure => "2.1.0",
  require => Exec["pip3"]
}
