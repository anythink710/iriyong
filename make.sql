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

create table iriyong_movie(
	id int primary key auto_increment,
    movie_name varchar(100),
    movie_subject varchar(100),
    movie_makedate varchar(100),
    movie_runtime varchar(100),
    movie_contry varchar(100),
    movie_url varchar(100),
    movie_sumnail varchar(100),
    delete_yn varchar(10) default 'N',
    regist_date datetime default now()
);

create table iriyong_file_store(
	id int primary key auto_increment,
    file_origin_name varchar(300),
    file_encode_name varchar(300),
    file_ext varchar(100),
    file_path varchar(300),
    file_size varchar(300),
    delete_yn varchar(10) default 'N',
    regist_date datetime default now()
);

ALTER TABLE iriyong_secretkey convert to charset utf8;
ALTER TABLE iriyong_todo convert to charset utf8;
ALTER TABLE iriyong_movie convert to charset utf8;
ALTER TABLE iriyong_file_store convert to charset utf8;
