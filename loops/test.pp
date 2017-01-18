cron{'check uptime':
	command	=>	'/usr/bin/w >> /tmp/load.log',
	user	=>	'test',
	hour	=>	'20',
	#minute	=>	['0-59'],
	minute  => 	'45',
	month	=>	['1-12'],
	monthday => 	['1-31'],
	weekday	 =>	'7',
}
