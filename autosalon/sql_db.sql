create table if not  exists admin (
id integer primary key autoincrement,
login text not null,
password text not null
);