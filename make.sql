create table iriyong_secretkey(
	id int primary key auto_increment,
    secret_key varchar(100) not null
);

create table iriyong_todo(
	id int primary key auto_increment,
    content varchar(300),
    complete varchar(10) default 'N',
    delete_yn varchar(10) default 'N',
    regist_date datetime default now()
);

ALTER TABLE iriyong_secretkey convert to charset utf8;
ALTER TABLE iriyong_todo convert to charset utf8;
