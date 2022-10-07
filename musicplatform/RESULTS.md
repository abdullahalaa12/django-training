## 1- create  some  artists

 `
 In [3]: artist1, artist2 =
 Artist(stage_name="Michael Jackson", social_link="https://www.instagram.com/michaeljackson/?hl=en"),
 Artist(stage_name="Coldplay", social_link="https://www.instagram.com/coldplay/?hl=en")
`

`In [5]: artist1.save()`

`In [6]: artist2.save()`

## 2- list  down  all  artists

`In [2]: Artist.objects.all()`

`Out[2]: <QuerySet [<Artist: Coldplay>, <Artist: Michael Jackson>]>`

## 3- list  down  all  artists  sorted  by  name

`In [5]: Artist.objects.all().order_by("stage_name")`

`Out[5]: <QuerySet [<Artist: Coldplay>, <Artist: Michael Jackson>]>`

## 4- list  down  all  artists  whose  name  starts  with  `a`

`In [3]: Artist.objects.filter(stage_name__startswith="a")`

`Out[3]: <QuerySet []>`

## 5- in  2  different  ways,  create  some  albums  and  assign  them  to  any  artists  (hint:  use  `objects`  manager  and  use  the  related  object  reference)
 
### 1:
`In [11]: artist1.album_set.create(name="Got to Be There", release_date=datetime.datetime(1972, 1, 24, 10, 0), cost = 999.99)`

### 2:
`In [19]: album2 = Album(name="Parachutes", release_date=datetime.datetime(2022, 10, 7, 10, 0), cost=499.99)`

`In [21]: album2.artist=artist2`

`In [22]: album2.save()`

## 6- get  the  latest  released  album

`In [36]: Album.objects.all().order_by("release_date").reverse()[0]`

`Out[36]: <Album: Parachutes>`

## 7- get  all  albums  released  before  today

`In [26]: Album.objects.exclude(release_date__gte=timezone.now().date())`

`Out[20]: <QuerySet [<Album: Got to Be There>, <Album: New Album>]>`

## 8- get all  albums  released  today  or  before  but  not  after  today

`In [27]: Album.objects.filter(release_date__date__lte=timezone.now().date())`

`Out[27]: <QuerySet [<Album: Got to Be There>, <Album: Parachutes>, <Album: New Album>]>`

## 9- count  the  total  number  of  albums  (hint:  count  in  an  optimized  manner)

`In [31]: Album.objects.count()`

`Out[31]: 3`

## 10- in  2  different  ways,  for  each  artist,  list  down  all  of  his/her  albums  (hint:  use  `objects`  manager  and  use  the  related  object  reference)

### 1:
`In [55]: for artist in Artist.objects.all():
    ...:     print(artist, artist.album_set.all())
`

`Coldplay <QuerySet [<Album: Parachutes>]>`

`Michael Jackson <QuerySet [<Album: Got to Be There>, <Album: New Album>]>`

### 2:
`In [58]: for artist in Artist.objects.all():
    ...:     print(artist, Album.objects.filter(artist=artist.id))
`

`Coldplay <QuerySet [<Album: Parachutes>]>`

`Michael Jackson <QuerySet [<Album: Got to Be There>, <Album: New Album>]>`

## 11- list  down  all  albums  ordered  by  cost  then  by  name  (cost  has  the  higher  priority)

`In [79]: Album.objects.all().order_by("cost", "name")`

`Out[79]: <QuerySet [<Album: Parachutes>, <Album: A>, <Album: Got to Be There>, <Album: New Album>]>`