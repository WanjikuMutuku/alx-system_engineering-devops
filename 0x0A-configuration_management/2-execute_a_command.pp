# manifest that kills a process named killmenow.

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
