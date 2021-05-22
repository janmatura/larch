CREATE TABLE evaluation (
record_id	int GENERATED ALWAYS AS IDENTITY,
ticker 		varchar(20),
date		date,
pe_change_130_p numeric(30,2) not null,
pe_a numeric(30,2) NOT null,

UNIQUE (ticker, date)
);


