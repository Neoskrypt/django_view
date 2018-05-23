--select DISTINCT name,surname from django_view_artist 
--where birth < '1990-01-01';
--select name,date_released from django_view_song
--where name = "Meow";
--insert into django_view_song(author_id,date_released,name) VALUES(2,"2018-05-21","Voodoo dance");
--UPDATE django_view_song
--set author_id = 2
--where name = "Voodoo dance";
--insert into django_view_artist(name,surname,birth) values ("Vasa", "pupkin","2000-10-04");

--elect name as Full_Name
--insert into django_view_song(author_id,date_released,name) VALUES(2,"2018-05-21","Voodoo dance");
--select * from django_view_artist
SELECT a.name,a.surname,count(d.id) AS amount FROM django_view_artist a
RIGHT JOIN django_view_song d ON a.id = d.author_id
GROUP BY a.name,a.surname
ORDER BY amount DESC
SELECT a.name, count(b.id) AS amount FROM django_view_artist a
LEFT JOIN django_view_artist b ON a.id = b.id
GROUP BY a.name








