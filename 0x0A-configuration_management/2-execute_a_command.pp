#Kill the procces killmenow
exec { 'restart_process':
    command => 'pkill killmenow',
    path    => '/usr/bin/',
}
