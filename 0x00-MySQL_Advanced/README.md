<h2>MySQL advanced</h2>

<p>pull and run mysql on docker with root user & password</p>
<code>docker run --name=my-image-name -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql</code>

<p>access the container</p>
<code>docker exec -it my-name bin/bash</code>

<p>Access MySQL</p>
<code>mysql</code>

<p>create user</p>

<code>CREATE USER 'user'@'localhost';
GRANT ALL PRIVILEGES ON base._ TO 'user'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, DELETE ON base._ TO 'user'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
</code>

<p>run query on mysql db on docker from localhost:</P>
<code>mysql -h localhost -P 3306 --protocol=tcp -u root -p hbtn_0d_tvshows</code>

<h2>Resources</h2>

<ul>
    <li><a href="/rltoken/8w9di_hk19DIMSBEV3EayQ" title="MySQL cheatsheet" target="_blank">MySQL cheatsheet</a></li>
    <li><a href="/rltoken/2GJbZ48zRPA70o2YhTdH7g" title="MySQL Performance: How To Leverage MySQL Database Indexing"
            target="_blank">MySQL Performance: How To Leverage MySQL Database Indexing</a>
    </li>
    <li><a href="/rltoken/K180X2OCzb6gzPngjn-EIg" title="Stored Procedure" target="_blank">Stored Procedure</a></li>
    <li><a href="/rltoken/cJ1qA4o-rRm4rWIsqYKSZg" title="Triggers" target="_blank">Triggers</a></li>
    <li><a href="/rltoken/vHg1z3UAOcWMvOt8xZHeiA" title="Views" target="_blank">Views</a>
    </li>
    <li><a href="/rltoken/g-c1m6iljScpi4LeqxBRqQ" title="Functions and Operators" target="_blank">Functions and
            Operators</a></li>
    <li><a href="/rltoken/gLVwKjQfRL0Jr_nWqAS7VQ" title="Trigger Syntax and Examples" target="_blank">Trigger Syntax and
            Examples</a></li>
    <li><a href="/rltoken/X789nJ22H6HVh1uCQPl0lg" title="CREATE TABLE Statement" target="_blank">CREATE TABLE
            Statement</a></li>
    <li><a href="/rltoken/mfrWMt1KL3NHXblJykMgZg" title="CREATE PROCEDURE and CREATE FUNCTION Statements"
            target="_blank">CREATE
            PROCEDURE and CREATE FUNCTION Statements</a></li>
    <li><a href="/rltoken/oCu8Rg9WfKyF4BhTt8dZGQ" title="CREATE INDEX Statement" target="_blank">CREATE INDEX
            Statement</a></li>
    <li><a href="/rltoken/FEZNlZFKZmD1ISnLINkCwQ" title="CREATE VIEW Statement" target="_blank">CREATE VIEW
            Statement</a></li>
</ul>

<h2>Learning Objectives</h2>

<h3>General</h3>

<ul>
    <li>How to create tables with constraints</li>
    <li>How to optimize queries by adding indexes</li>
    <li>What is and how to implement stored procedures and functions in MySQL</li>
    <li>What is and how to implement views in MySQL</li>
    <li>What is and how to implement triggers in MySQL</li>
</ul>

<pre><code>$ service mysql start

- MySQL Community Server 5.7.30 is started
  $
$ cat 0-list_databases.sql | mysql -uroot -p my_database
  Enter password:
  Database
  information_schema
  mysql
  performance_schema
  sys
  $
  </code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<h3>How to import a SQL dump</h3>

<pre><code>$ echo &quot;CREATE DATABASE hbtn_0d_tvshows;&quot; | mysql -uroot -p

  Enter password:
  $ curl &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql&quot; -s | mysql -uroot -p hbtn_0d_tvshows
  Enter password:
  $ echo &quot;SELECT \* FROM tv_genres&quot; | mysql -uroot -p hbtn_0d_tvshows
  Enter password:
  id name
  1 Drama
  2 Mystery
  3 Adventure
  4 Fantasy
  5 Comedy
  6 Crime
  7 Suspense
  8 Thriller
  $
  </code></pre>

<h2 class="gap">Tasks</h2>

<h3 class="panel-title">
    0. We are all unique!
</h3>
<p>Write a SQL script that creates a table <code>users</code> following these
    requirements:</p>

<ul>
    <li>With these attributes:

        <ul>
            <li><code>id</code>, integer, never null, auto increment and primary key
            </li>
            <li><code>email</code>, string (255 characters), never null and unique</li>
            <li><code>name</code>, string (255 characters)</li>
        </ul>
    </li>
    <li>If the table already exists, your script should not fail</li>
    <li>Your script can be executed on any database</li>
</ul>

<p><strong>Context:</strong>
    <em>Make an attribute unique directly in the table schema will enforced your
        business rules and avoid bugs in your application</em>
</p>

<pre><code>bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton

  Enter password:
  ERROR 1146 (42S02) at line 1: Table &#39;holberton.users&#39; doesn&#39;t exist
  bob@dylan:~$
  bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
  Enter password:
  bob@dylan:~$
  bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;);&#39; | mysql -uroot -p holberton
  Enter password:
  bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;);&#39; | mysql -uroot -p holberton
  Enter password:
  bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Jean&quot;);&#39; | mysql -uroot -p holberton
  Enter password:
  ERROR 1062 (23000) at line 1: Duplicate entry &#39;bob@dylan.com&#39; for key &#39;email&#39;
  bob@dylan:~$
  bob@dylan:~$ echo &quot;SELECT \* FROM users;&quot; | mysql -uroot -p holberton
  Enter password:
  id email name
  1 bob@dylan.com Bob
  2 sylvie@dylan.com Sylvie
  bob@dylan:~$
  </code></pre>

<h3 class="panel-title">
    1. In and not out
</h3>

<p>Write a SQL script that creates a table <code>users</code> following these
    requirements:</p>

<ul>
    <li>With these attributes:

        <ul>
            <li><code>id</code>, integer, never null, auto increment and primary key
            </li>
            <li><code>email</code>, string (255 characters), never null and unique</li>
            <li><code>name</code>, string (255 characters)</li>
            <li><code>country</code>, enumeration of countries: <code>US</code>,
                <code>CO</code> and <code>TN</code>, never null (= default will be the
                first element of the enumeration, here <code>US</code>)
            </li>
        </ul>
    </li>
    <li>If the table already exists, your script should not fail</li>
    <li>Your script can be executed on any database</li>
</ul>

<pre><code>bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton

  Enter password:
  ERROR 1146 (42S02) at line 1: Table &#39;holberton.users&#39; doesn&#39;t exist
  bob@dylan:~$
  bob@dylan:~$ cat 1-country_users.sql | mysql -uroot -p holberton
  Enter password:
  bob@dylan:~$
  bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;, &quot;US&quot;);&#39; | mysql -uroot -p holberton
  Enter password:
  bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;, &quot;CO&quot;);&#39; | mysql -uroot -p holberton
  Enter password:
  bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;jean@dylan.com&quot;, &quot;Jean&quot;, &quot;FR&quot;);&#39; | mysql -uroot -p holberton
  Enter password:
  ERROR 1265 (01000) at line 1: Data truncated for column &#39;country&#39; at row 1
  bob@dylan:~$
  bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;john@dylan.com&quot;, &quot;John&quot;);&#39; | mysql -uroot -p holberton
  Enter password:
  bob@dylan:~$
  bob@dylan:~$ echo &quot;SELECT \* FROM users;&quot; | mysql -uroot -p holberton
  Enter password:
  id email name country
  1 bob@dylan.com Bob US
  2 sylvie@dylan.com Sylvie CO
  3 john@dylan.com John US
  bob@dylan:~$
  </code></pre>

<h3 class="panel-title">
    2. Best band ever!
</h3>

<span id="user_id" data-id="343517"></span>

<p>Write a SQL script that ranks country origins of bands, ordered by the number of
    (non-unique) fans</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>Import this table dump: <a href="/rltoken/uPn947gnZLaa0FJrrAFTGQ" title="metal_bands.sql.zip"
            target="_blank">metal_bands.sql.zip</a></li>
    <li>Column names must be: <code>origin</code> and <code>nb_fans</code></li>
    <li>Your script can be executed on any database</li>
</ul>

<p><strong>Context:</strong>
    <em>Calculate/compute something is always power intensive&hellip; better to
        distribute the load!</em>
</p>

<pre><code>bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton

  Enter password:
  bob@dylan:~$
  bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton &gt; tmp_res ; head tmp_res
  Enter password:
  origin nb_fans
  USA 99349
  Sweden 47169
  Finland 32878
  United Kingdom 32518
  Germany 29486
  Norway 22405
  Canada 8874
  The Netherlands 8819
  Italy 7178
  bob@dylan:~$
  </code></pre>


<p>Write a SQL script that lists all bands with <code>Glam rock</code> as their main
    style, ranked by their longevity</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>Import this table dump: <a href="/rltoken/uPn947gnZLaa0FJrrAFTGQ" title="metal_bands.sql.zip"
            target="_blank">metal_bands.sql.zip</a></li>
    <li>Column names must be: <code>band_name</code> and <code>lifespan</code> (in years
        <strong>until 2022</strong> - please use <code>2022</code> instead of
        <code>YEAR(CURDATE())</code>)
    </li>
    <li>You should use attributes <code>formed</code> and <code>split</code> for
        computing the <code>lifespan</code></li>
    <li>Your script can be executed on any database</li>
</ul>

<pre><code>bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton

  Enter password:
  bob@dylan:~$
  bob@dylan:~$ cat 3-glam_rock.sql | mysql -uroot -p holberton
  Enter password:
  band_name lifespan
  Alice Cooper 56
  Mötley Crüe 34
  Marilyn Manson 31
  The 69 Eyes 30
  Hardcore Superstar 23
  Nasty Idols 0
  Hanoi Rocks 0
  bob@dylan:~$
  </code></pre>

<p>Write a SQL script that creates a trigger that decreases the quantity of an item
    after adding a new order.</p>

<p>Quantity in the table <code>items</code> can be negative.</p>

<p><strong>Context:</strong>
    <em>Updating multiple tables for one action from your application can generate
        issue: network disconnection, crash, etc&hellip; to keep your data in a good
        shape, let MySQL do it for you!</em>
</p>

<pre><code>bob@dylan:~$ cat 4-init.sql

  -- Initial
  DROP TABLE IF EXISTS items;
  DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
name VARCHAR(255) NOT NULL,
quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
item_name VARCHAR(255) NOT NULL,
number int NOT NULL
);

INSERT INTO items (name) VALUES (&quot;apple&quot;), (&quot;pineapple&quot;), (&quot;pear&quot;);

bob@dylan:~$
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-main.sql
Enter password:
-- Show and add orders
SELECT _ FROM items;
SELECT _ FROM orders;

INSERT INTO orders (item_name, number) VALUES (&#39;apple&#39;, 1);
INSERT INTO orders (item_name, number) VALUES (&#39;apple&#39;, 3);
INSERT INTO orders (item_name, number) VALUES (&#39;pear&#39;, 2);

SELECT &quot;--&quot;;

SELECT _ FROM items;
SELECT _ FROM orders;

bob@dylan:~$
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton
Enter password:
name quantity
apple 10
pineapple 10
pear 10
--
--
name quantity
apple 6
pineapple 10
pear 8
item_name number
apple 1
apple 3
pear 2
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    5. Email validation to sent
</h3>

<p>Write a SQL script that creates a trigger that resets the attribute
    <code>valid_email</code> only when the <code>email</code> has been changed.
</p>

<p><strong>Context:</strong>
    <em>Nothing related to MySQL, but perfect for user email validation - distribute the
        logic to the database itself!</em>
</p>

<pre><code>bob@dylan:~$ cat 5-init.sql

-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
id int not null AUTO_INCREMENT,
email varchar(255) not null,
name varchar(255),
valid_email boolean not null default 0,
PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;);
INSERT INTO users (email, name, valid_email) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;, 1);
INSERT INTO users (email, name, valid_email) VALUES (&quot;jeanne@dylan.com&quot;, &quot;Jeanne&quot;, 1);

bob@dylan:~$
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-valid_email.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-main.sql
Enter password:
-- Show users and update (or not) email
SELECT \* FROM users;

UPDATE users SET valid_email = 1 WHERE email = &quot;bob@dylan.com&quot;;
UPDATE users SET email = &quot;sylvie+new@dylan.com&quot; WHERE email = &quot;sylvie@dylan.com&quot;;
UPDATE users SET name = &quot;Jannis&quot; WHERE email = &quot;jeanne@dylan.com&quot;;

SELECT &quot;--&quot;;
SELECT \* FROM users;

UPDATE users SET email = &quot;bob@dylan.com&quot; WHERE email = &quot;bob@dylan.com&quot;;

SELECT &quot;--&quot;;
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton
Enter password:
id email name valid_email
1 bob@dylan.com Bob 0
2 sylvie@dylan.com Sylvie 1
3 jeanne@dylan.com Jeanne 1
--
--
id email name valid_email
1 bob@dylan.com Bob 1
2 sylvie+new@dylan.com Sylvie 0
3 jeanne@dylan.com Jannis 1
--
--
id email name valid_email
1 bob@dylan.com Bob 1
2 sylvie+new@dylan.com Sylvie 0
3 jeanne@dylan.com Jannis 1
bob@dylan:~$
</code></pre>

<p>Write a SQL script that creates a stored procedure <code>AddBonus</code> that adds a
    new correction for a student.</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>Procedure <code>AddBonus</code> is taking 3 inputs (in this order):

        <ul>
            <li><code>user_id</code>, a <code>users.id</code> value (you can assume
                <code>user_id</code> is linked to an existing <code>users</code>)
            </li>
            <li><code>project_name</code>, a new or already exists <code>projects</code>
                - if no <code>projects.name</code> found in the table, you should create
                it</li>
            <li><code>score</code>, the score value for the correction</li>
        </ul>
    </li>
</ul>

<p><strong>Context:</strong>
    <em>Write code in SQL is a nice level up!</em>
</p>

<pre><code>bob@dylan:~$ cat 6-init.sql

-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
id int not null AUTO_INCREMENT,
name varchar(255) not null,
average_score float default 0,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
id int not null AUTO_INCREMENT,
name varchar(255) not null,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
user_id int not null,
project_id int not null,
score int default 0,
KEY `user_id` (`user_id`),
KEY `project_id` (`project_id`),
CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;C is fun&quot;);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;Python is cool&quot;);
SET @project_py = LAST_INSERT_ID();

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-main.sql
Enter password:
-- Show and add bonus correction
SELECT _ FROM projects;
SELECT _ FROM corrections;

SELECT &quot;--&quot;;

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;Python is cool&quot;, 100);

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;Bonus project&quot;, 100);
CALL AddBonus((SELECT id FROM users WHERE name = &quot;Bob&quot;), &quot;Bonus project&quot;, 10);

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;New bonus&quot;, 90);

SELECT &quot;--&quot;;

SELECT _ FROM projects;
SELECT _ FROM corrections;

bob@dylan:~$
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton
Enter password:
id name
1 C is fun
2 Python is cool
user_id project_id score
1 1 80
1 2 96
2 1 91
2 2 73
--
--
--
--
id name
1 C is fun
2 Python is cool
3 Bonus project
4 New bonus
user_id project_id score
1 1 80
1 2 96
2 1 91
2 2 73
2 2 100
2 3 100
1 3 10
2 4 90
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    7. Average score
</h3>

<p>Write a SQL script that creates a stored procedure
    <code>ComputeAverageScoreForUser</code> that computes and store the average score
    for a student.

    Note: An average score can be a decimal
</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>Procedure <code>ComputeAverageScoreForUser</code> is taking 1 input:

        <ul>
            <li><code>user_id</code>, a <code>users.id</code> value (you can assume
                <code>user_id</code> is linked to an existing <code>users</code>)
            </li>
        </ul>
    </li>
</ul>

<pre><code>bob@dylan:~$ cat 7-init.sql

-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
id int not null AUTO_INCREMENT,
name varchar(255) not null,
average_score float default 0,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
id int not null AUTO_INCREMENT,
name varchar(255) not null,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
user_id int not null,
project_id int not null,
score int default 0,
KEY `user_id` (`user_id`),
KEY `project_id` (`project_id`),
CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;C is fun&quot;);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;Python is cool&quot;);
SET @project_py = LAST_INSERT_ID();

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-average_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-main.sql
-- Show and compute average score
SELECT _ FROM users;
SELECT _ FROM corrections;

SELECT &quot;--&quot;;
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = &quot;Jeanne&quot;));

SELECT &quot;--&quot;;
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton
Enter password:
id name average_score
1 Bob 0
2 Jeanne 0
user_id project_id score
1 1 80
1 2 96
2 1 91
2 2 73
--
--
--
--
id name average_score
1 Bob 0
2 Jeanne 82
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    8. Optimize simple search
</h3>

<p>Write a SQL script that creates an index <code>idx_name_first</code> on the table
    <code>names</code> and the first letter of <code>name</code>.
</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>Import this table dump: <a href="/rltoken/BluyCCIIfw0NqcjqUiUdEw" title="names.sql.zip"
            target="_blank">names.sql.zip</a></li>
    <li>Only the first letter of <code>name</code> must be indexed</li>
</ul>

<p><strong>Context:</strong>
    <em>Index is not the solution for any performance issue, but well used, it&rsquo;s
        really powerful!</em>
</p>

<pre><code>bob@dylan:~$ cat names.sql | mysql -uroot -p holberton

Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39;;
+-------------+
| COUNT(name) |
+-------------+
| 302936 |
+-------------+
1 row in set (2.19 sec)
mysql&gt;
mysql&gt; exit
bye
bob@dylan:~$
bob@dylan:~$ cat 8-index_my_names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql&gt; SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names | 1 | idx_name_first | 1 | name | A | 25 | 1 | NULL | YES | BTREE | | |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql&gt;
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39;;
+-------------+
| COUNT(name) |
+-------------+
| 302936 |
+-------------+
1 row in set (0.82 sec)
mysql&gt;
mysql&gt; exit
bye
bob@dylan:~$
</code></pre>

<p>Write a SQL script that creates an index <code>idx_name_first_score</code> on the
    table <code>names</code> and the first letter of <code>name</code> and the
    <code>score</code>.
</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>Import this table dump: <a href="/rltoken/BluyCCIIfw0NqcjqUiUdEw" title="names.sql.zip"
            target="_blank">names.sql.zip</a></li>
    <li>Only the first letter of <code>name</code> AND <code>score</code> must be
        indexed</li>
</ul>

<pre><code>bob@dylan:~$ cat names.sql | mysql -uroot -p holberton

Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39; AND score &lt; 80;
+-------------+
| count(name) |
+-------------+
| 60717 |
+-------------+
1 row in set (2.40 sec)
mysql&gt;
mysql&gt; exit
bye
bob@dylan:~$
bob@dylan:~$ cat 9-index_name_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql&gt; SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names | 1 | idx_name_first_score | 1 | name | A | 25 | 1 | NULL | YES | BTREE | | |
| names | 1 | idx_name_first_score | 2 | score | A | 3901 | NULL | NULL | YES | BTREE | | |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql&gt;
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39; AND score &lt; 80;
+-------------+
| COUNT(name) |
+-------------+
| 60717 |
+-------------+
1 row in set (0.48 sec)
mysql&gt;
mysql&gt; exit
bye
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    10. Safe divide
</h3>

<p>Write a SQL script that creates a function <code>SafeDiv</code> that divides (and
    returns) the first by the second number or returns 0 if the second number is equal
    to 0.</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>You must create a function</li>
    <li>The function <code>SafeDiv</code> takes 2 arguments:

        <ul>
            <li><code>a</code>, INT</li>
            <li><code>b</code>, INT</li>
        </ul>
    </li>
    <li>And returns <code>a / b</code> or 0 if <code>b == 0</code></li>
</ul>

<pre><code>bob@dylan:~$ cat 10-init.sql

-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
a int default 0,
b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo &quot;SELECT (a / b) FROM numbers;&quot; | mysql -uroot -p holberton
Enter password:
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$
bob@dylan:~$ echo &quot;SELECT SafeDiv(a, b) FROM numbers;&quot; | mysql -uroot -p holberton
Enter password:
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    11. No table for a meeting
</h3>
<p>Write a SQL script that creates a view <code>need_meeting</code> that lists all
    students that have a score under 80 (strict) and no <code>last_meeting</code> or
    more than 1 month.</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>The view <code>need_meeting</code> should return all students name when:

        <ul>
            <li>They score are under (strict) to 80</li>
            <li><strong>AND</strong> no <code>last_meeting</code> date
                <strong>OR</strong> more than a month
            </li>
        </ul>
    </li>
</ul>

<pre><code>bob@dylan:~$ cat 11-init.sql

-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
name VARCHAR(255) NOT NULL,
score INT default 0,
last_meeting DATE NULL
);

INSERT INTO students (name, score) VALUES (&quot;Bob&quot;, 80);
INSERT INTO students (name, score) VALUES (&quot;Sylvia&quot;, 120);
INSERT INTO students (name, score) VALUES (&quot;Jean&quot;, 60);
INSERT INTO students (name, score) VALUES (&quot;Steeve&quot;, 50);
INSERT INTO students (name, score) VALUES (&quot;Camilia&quot;, 80);
INSERT INTO students (name, score) VALUES (&quot;Alexa&quot;, 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-need_meeting.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-main.sql
-- Test view
SELECT \* FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET score = 40 WHERE name = &#39;Bob&#39;;
SELECT \* FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET score = 80 WHERE name = &#39;Steeve&#39;;
SELECT \* FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET last_meeting = CURDATE() WHERE name = &#39;Jean&#39;;
SELECT \* FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET last_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = &#39;Jean&#39;;
SELECT \* FROM need_meeting;

SELECT &quot;--&quot;;

SHOW CREATE TABLE need_meeting;

SELECT &quot;--&quot;;

SHOW CREATE TABLE students;

bob@dylan:~$
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password:
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View Create View character_set_client collation_connection
XXXXXX&lt;yes, here it will display the View SQL statement :-) &gt;XXXXXX
--
--
Table Create Table
students CREATE TABLE `students` (\n `name` varchar(255) NOT NULL,\n `score` int(11) DEFAULT &#39;0&#39;,\n `last_meeting` date DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    12. Average weighted score
</h3>

<p>Write a SQL script that creates a stored procedure
    <code>ComputeAverageWeightedScoreForUser</code> that computes and store the average
    weighted score for a student.
</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>Procedure <code>ComputeAverageScoreForUser</code> is taking 1 input:

        <ul>
            <li><code>user_id</code>, a <code>users.id</code> value (you can assume
                <code>user_id</code> is linked to an existing <code>users</code>)
            </li>
        </ul>
    </li>
</ul>

<p><strong>Tips</strong>:</p>

<ul>
    <li><a href="/rltoken/QHx92mlF43zF6GTEil-Cyw" title="Calculate-Weighted-Average"
            target="_blank">Calculate-Weighted-Average</a></li>
</ul>

<pre><code>bob@dylan:~$ cat 100-init.sql

-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
id int not null AUTO_INCREMENT,
name varchar(255) not null,
average_score float default 0,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
id int not null AUTO_INCREMENT,
name varchar(255) not null,
weight int default 1,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
user_id int not null,
project_id int not null,
score float default 0,
KEY `user_id` (`user_id`),
KEY `project_id` (`project_id`),
CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES (&quot;C is fun&quot;, 1);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES (&quot;Python is cool&quot;, 2);
SET @project_py = LAST_INSERT_ID();

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 100-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 100-average_weighted_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 100-main.sql
-- Show and compute average weighted score
SELECT _ FROM users;
SELECT _ FROM projects;
SELECT \* FROM corrections;

CALL ComputeAverageWeightedScoreForUser((SELECT id FROM users WHERE name = &quot;Jeanne&quot;));

SELECT &quot;--&quot;;
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 100-main.sql | mysql -uroot -p holberton
Enter password:
id name average_score
1 Bob 0
2 Jeanne 82
id name weight
1 C is fun 1
2 Python is cool 2
user_id project_id score
1 1 80
1 2 96
2 1 91
2 2 73
--
--
id name average_score
1 Bob 0
2 Jeanne 79
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    13. Average weighted score for all!
</h3>

<p>Write a SQL script that creates a stored procedure
    <code>ComputeAverageWeightedScoreForUsers</code> that computes and store the average
    weighted score for all students.
</p>

<p><strong>Requirements:</strong></p>

<ul>
    <li>Procedure <code>ComputeAverageWeightedScoreForUsers</code> is not taking any
        input.</li>
</ul>

<p><strong>Tips</strong>:</p>

<ul>
    <li><a href="/rltoken/QHx92mlF43zF6GTEil-Cyw" title="Calculate-Weighted-Average"
            target="_blank">Calculate-Weighted-Average</a></li>
</ul>

<pre><code>bob@dylan:~$ cat 101-init.sql

-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
id int not null AUTO_INCREMENT,
name varchar(255) not null,
average_score float default 0,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
id int not null AUTO_INCREMENT,
name varchar(255) not null,
weight int default 1,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
user_id int not null,
project_id int not null,
score float default 0,
KEY `user_id` (`user_id`),
KEY `project_id` (`project_id`),
CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES (&quot;C is fun&quot;, 1);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES (&quot;Python is cool&quot;, 2);
SET @project_py = LAST_INSERT_ID();

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 101-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 101-average_weighted_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 101-main.sql
-- Show and compute average weighted score
SELECT _ FROM users;
SELECT _ FROM projects;
SELECT \* FROM corrections;

CALL ComputeAverageWeightedScoreForUsers();

SELECT &quot;--&quot;;
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 101-main.sql | mysql -uroot -p holberton
Enter password:
id name average_score
1 Bob 0
2 Jeanne 0
id name weight
1 C is fun 1
2 Python is cool 2
user_id project_id score
1 1 80
1 2 96
2 1 91
2 2 73
--
--
id name average_score
1 Bob 90.6667
2 Jeanne 79
bob@dylan:~$
</code></pre>