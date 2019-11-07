Encurtador de URL's 


CREATE TABLE users(
id serial primary key,
nome varchar(200) not null,
email varchar(200) not null unique,
username varchar(100) not null unique,
password varchar(100) not null
);

CREATE TABLE links(
id serial primary key,
hits integer not null,
urloriginal varchar(200) not null,
shorturl varchar(200) not null unique,
FOREIGN KEY (id) REFERENCES users(id)
);

