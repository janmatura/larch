CREATE TABLE ticker_ohlc (

record_id   int generated always as identity,
ticker		varchar(20),
date		date,
open		numeric(10,2) not null,
close		numeric(10,2) not null,
low			numeric(10,2) not null,
high		numeric(10,2) not null,
peRatio		numeric(10,2) not null,
pbRatio		numeric(10,2) not null


);

create index recId_p on ticker_ohlc 
(
	ticker,
	date 
);

CREATE TABLE ticker_funda (

record_id   int generated always as identity,
ticker		varchar(20),
date		date,
quarter		numeric(1,0) not null,
roa				numeric(30,2) not null,
piotroskiFScore	numeric(1,0) not null,
eps				numeric(30,2) not null,
revenue			numeric(30,2) not null,
grossProfit		numeric(30,2) not null,
ebt				numeric(30,2) not null,
ebitda			numeric(30,2) not null,
totalAssets		numeric(30,2) not null,
sharesBasic		numeric(30,2) not null,
debtCurrent		numeric(30,2) not null


);

create index recId_f on ticker_ohlc 
(
	ticker,
	date 
);


