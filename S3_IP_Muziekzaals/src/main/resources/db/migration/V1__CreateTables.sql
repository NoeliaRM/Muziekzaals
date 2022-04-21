CREATE TABLE user_
                    (
                     user_id INT NOT NULL AUTO_INCREMENT,
                     user_username VARCHAR(100) NOT NULL,
                     user_password VARCHAR(100) NOT NULL,
                     user_type_fk INT NOT NULL,

                     PRIMARY KEY ( user_id )
                    );

CREATE TABLE user_type
                    (
                     user_type_id INT NOT NULL AUTO_INCREMENT,
                     user_type_description VARCHAR(100) NOT NULL,
                     permission_fk INT NOT NULL,

                     PRIMARY KEY ( user_type_id )
                    );

CREATE TABLE permission
                    (
                    permission_id INT NOT NULL AUTO_INCREMENT,
                    permission_description VARCHAR(100) NOT NULL,

                    PRIMARY KEY ( permission_id )
                    );

CREATE TABLE user_relationship
                    (
                     user_relationship_first_id INT NOT NULL,
                     user_relationship_second_id INT NOT NULL,
                     relationship_fk INT NOT NULL,

                     PRIMARY KEY ( user_relationship_first_id, user_relationship_second_id )
                    );

CREATE TABLE relationship
                    (
                     relationship_id INT NOT NULL AUTO_INCREMENT,
                     relationship_description VARCHAR(100) NOT NULL,

                     PRIMARY KEY (relationship_id)
                    );






