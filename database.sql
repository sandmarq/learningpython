CREATE TABLE domocontrolsm.tempsensors (
	id int(10) NOT NULL auto_increment,
	date varchar(25) NOT NULL,
	topic varchar(60) NOT NULL,
	temp decimal(5,2) NOT NULL,
	humidity decimal(5,2) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
