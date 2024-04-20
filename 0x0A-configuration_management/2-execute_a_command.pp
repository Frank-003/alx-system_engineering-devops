#This code kills a process && works together with the killnow file which has already been prvided
exec { 'killmenow':
  command  =>  '/usr/bin/pkill killmenow',
  provider =>  'shell',
  returns  =>  [0, 1],
}
