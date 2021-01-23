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



do $$
declare lm int = 0;
declare datem date = '2020-01-15';

begin
for i in 1..10000 loop
datem = datem + 1;
INSERT INTO ticker_ohlc (ticker, date, open, close, low, high) 
VALUES ('JNJ', datem, lm, 322.01, 112, 325.1);
lm = lm + 1;
end loop;
end; $$

delete from ticker_ohlc where record_id not in (select distinct on (ticker, date) record_id from ticker_ohlc);

