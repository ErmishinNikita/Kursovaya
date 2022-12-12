-- create table if not  exists auto (
-- id integer primary key autoincrement,
-- login text not null,
-- password text not null
-- );

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