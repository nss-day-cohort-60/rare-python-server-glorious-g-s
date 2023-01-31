CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

INSERT INTO `Users` VALUES (null, "Pat", "Mahomes", "pat@pat.com", "Football player", "pat", "pat", "https://www.history.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTU3ODc4NjAwMDI2ODkxNTkz/the-nfl-begins-football-grass-2014-hero-2.jpg", 01312023, 1);
INSERT INTO `Users` VALUES (null, "Jalen", "Hurts", "hurts@hurts.com", "Football player", "jalen", "jalen", "https://assets3.cbsnewsstatic.com/hub/i/r/2022/03/14/08c8764e-029d-4bf2-8319-db05c67a20d3/thumbnail/640x392/be38c4b9e67216d7a78628552724738c/tom-brady-football.jpg", 01312023, 1);

INSERT INTO `Subscriptions` VALUES (null, 1, 2, 01312023);

INSERT INTO `Posts` VALUES (NULL, 2, "How to win a superbowl", 02072023, "https://www.si.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTc0NDU1OTQyMjAzNjQ3NjIy/college-football-covid-symptoms-cases-players.jpg", "You can win a superbowl by outscoring your opponent.", 1);
INSERT INTO `Comments` VALUES (NULL, 1, 2, "That is not how you win a superbowl.");

DELETE FROM Users 
WHERE id >= 3