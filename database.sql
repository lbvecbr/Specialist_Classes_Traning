 create table t_document(
    -- TODO: 1. Сделать возможность сохранение в базе
    -- TODO:         дополнительных параметров
    i_id      integer  not null autoincrement primary key,
    f_status  integer  null
 );

 create table t_nakladnaya(
    r_id_document  integer not null primary key references t_document(i_id),
    f_itogo        numeric(22, 2) null
 );

 create table t_position(
    i_id             integer        not null autoincrement primary key,
    r_id_nakladnaya  integer        not null references t_nakladnaya(i_id),
    f_ordinal        integer        not null,
    f_title          text           null,
    f_unit           text           null,
    f_amount         integer        null,
    f_price          numeric(22, 4) null,
    f_summa          numeric(22, 4) null
 );