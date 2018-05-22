--select DISTINCT name,surname from django_view_artist 
--where birth < '1990-01-01';
--select name,date_released from django_view_song
--where name LIKE("Meow%");
--insert into django_view_song(author_id,date_released,name) VALUES(2,"2018-05-21","Voodoo dance");
--UPDATE django_view_song
--set author_id = 1
--where name = "Voodoo dance";

select id,name || ' ' || surname  as full_name, birth as Birth
from django_view_artist






