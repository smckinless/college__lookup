drop table if exists college_holder;
    create table college_holder (
    id integer primary key autoincrement,
    name text not null,
    acceptance_rate text not null,
    location text not null,
    sat_score text not null,
    act_score text not null
);