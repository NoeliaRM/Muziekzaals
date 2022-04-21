ALTER TABLE `user_`
ADD CONSTRAINT `user_type_fk`
FOREIGN KEY (`user_type_fk`) REFERENCES `user_type`(`user_type_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `user_type`
ADD CONSTRAINT `permission_fk`
FOREIGN KEY (`permission_fk`) REFERENCES `permission`(`permission_id`) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE `user_relationship`
ADD CONSTRAINT `relationship_fk`
FOREIGN KEY (`relationship_fk`) REFERENCES `relationship`(`relationship_id`) ON DELETE NO ACTION ON UPDATE CASCADE;
