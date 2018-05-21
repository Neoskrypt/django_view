--select DISTINCT name,surname from django_view_artist 
--where birth < '1990-01-01';
--select name,date_released from django_view_song
--where name = "Meow";
--insert into django_view_song(author_id,date_released,name) VALUES(2,"2018-05-21","Voodoo dance");
--UPDATE django_view_song
--set author_id = 1
--where name = "Voodoo dance";
--select name as Full_Name from django_view_artist
--UNION
--select surname as Full_Name from django_view_artist
SELECT id,name,surname,birth FROM django_view_artist
--SELECT id,birth,CONCAT(name,"",surname) as Full_Name from django_view_artist;






