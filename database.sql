CREATE TABLE domocontrolsm.tempsensors (
	id int(10) NOT NULL auto_increment,
	date varchar(25) NOT NULL,
	topic varchar(60),
	temp decimal(5,2),
	humidity decimal(5,2),
	PRIMARY KEY (date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE UNIQUE INDEX id ON domocontrolsm.tempsensors (id);