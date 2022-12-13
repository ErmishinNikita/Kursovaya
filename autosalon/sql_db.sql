create table if not  exists admin (
id integer primary key autoincrement,
login text not null,
password text not null
);

create table if not  exists users (
id integer primary key autoincrement,
login text not null,
password text not null
);


create table if not  exists uslugi (
id integer primary key autoincrement,
fio text not null,
contact text not null,
auto text not null
);

create table if not exists model2 (
    id integer primary key autoincrement,
    name text not null,
    foto text not null,
    price text not null,
    max_speed text not null,
    loshad text not null,
    razgon text not null,
    rashod text not null
);