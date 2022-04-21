INSERT INTO permission
(permission_description)
VALUES ("premium");
INSERT INTO permission
(permission_description)
VALUES ("basic");


INSERT INTO user_type
(user_type_description, permission_fk)
VALUES ("administrator", 1);
INSERT INTO user_type
(user_type_description, permission_fk)
VALUES ("customer", 2);


INSERT INTO user_
(user_username, user_password, user_type_fk)
VALUES ("a", "a", 1);
INSERT INTO user_
(user_username, user_password, user_type_fk)
VALUES ("c1", "c1", 2);
INSERT INTO user_
(user_username, user_password, user_type_fk)
VALUES ("c2", "c2", 2);
INSERT INTO user_
(user_username, user_password, user_type_fk)
VALUES ("c3", "c3", 2);