CREATE TABLE `user` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`f_name` varchar(255),
	`l_name` varchar(255),
	`dob` varchar(255),
	`role` varchar(10),
	`username` varchar(255),
	`password` varchar(255),
	`profile_pic` varchar(200),
	`updated_at` DATETIME,
	`created_at` DATETIME,
	PRIMARY KEY (`id`)
);

CREATE TABLE `case_details` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`username` varchar(255),
	`case_name` varchar(255),
	`ref_no` varchar(255),
	`case_details` varchar(500),
	`updated_at` DATETIME,
	`created_at` DATETIME,
	PRIMARY KEY (`id`)
);

CREATE TABLE `mob_osint` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`name_truecaller` varchar(200),
	`name_eyecon` varchar(200),
	`name_fb` varchar(200),
	`mail_id` varchar(255),
	`fb_url` varchar(255),
	`city` varchar(200),
	`state` varchar(200),
	`msp` varchar(200),
	`upi_id` varchar(200),
	`updated_at` DATETIME,
	`created_at` DATETIME,
	PRIMARY KEY (`id`)
);

CREATE TABLE `email_osint` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`fb_url` varchar(255),
	`twitter_url` varchar(200),
	`instagram_url` varchar(200),
	`other_url` varchar(200),
	`updated_at` TIMESTAMP,
	`created_at` TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `gmail_details` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`owner_name` varchar(200),
	`goolge_id` varchar(200),
	`google_services` varchar(200),
	`youtube_channel` varchar(200),
	`map_contributions` varchar(200),
	`calendar_events` varchar(200),
	`updated_at` DATETIME,
	`created_at` DATETIME,
	PRIMARY KEY (`id`)
);

CREATE TABLE `truecaller_details` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`owner_name` varchar(200),
	`gender` varchar(200),
	`about` varchar(500),
	`job_title` varchar(200),
	`company_name` varchar(200),
	`e164_format` varchar(200),
	`national_format` varchar(200),
	`dialing_code` varchar(200),
	`country_code` varchar(200),
	`carrier_name` varchar(200),
	`address` varchar(200),
	`street` varchar(200),
	`zip_code` varchar(200),
	`city` varchar(200),
	`country_code` varchar(200),
	`time_zone` varchar(200) NOT NULL,
	`internet_addresses_id` varchar(200),
	`internet_addresses_service` varchar(200) NOT NULL,
	`internet_addresses_caption` varchar(200),
	`is_user` varchar(200),
	`updated_at` TIMESTAMP,
	`created_at` TIMESTAMP,
	PRIMARY KEY (`id`)
);

ALTER TABLE `case_details` ADD CONSTRAINT `case_details_fk0` FOREIGN KEY (`id`) REFERENCES `user`(`username`);

ALTER TABLE `mob_osint` ADD CONSTRAINT `mob_osint_fk0` FOREIGN KEY (`id`) REFERENCES `case_details`(`id`);

ALTER TABLE `email_osint` ADD CONSTRAINT `email_osint_fk0` FOREIGN KEY (`id`) REFERENCES `case_details`(`id`);

ALTER TABLE `gmail_details` ADD CONSTRAINT `gmail_details_fk0` FOREIGN KEY (`id`) REFERENCES `case_details`(`id`);

ALTER TABLE `truecaller_details` ADD CONSTRAINT `truecaller_details_fk0` FOREIGN KEY (`id`) REFERENCES `case_details`(`id`);

