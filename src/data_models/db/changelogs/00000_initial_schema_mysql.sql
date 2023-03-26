-- liquibase formatted sql
-- changeset dom:636e9da8-cdd4-4079-b7c7-f47e1516e609 splitStatements:true endDelimiter:;

SET timezone = 'UTC';

DROP TABLE IF EXISTS stock_data CASCADE;
CREATE TABLE stock_data (
    stock_data_id       INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    created             TIMESTAMP not null default now(),
    stock_id            VARCHAR(400) null,
    stock_value         INTEGER NOT NULL,
    currency            CHAR(3) not null default 'GBP'
);