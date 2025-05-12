from django.db import models


class Films(models.Model):
    GENRE = (
        ('Боевик', 'Боевик'),
        ('Приключения', 'Приключения'),
        ('Постапокалипсис', 'Постапокалипсис'),
        ('Утопия', 'Утопия'),
        ('Дистопия', 'Дистопия'),
        ('Фантастика', 'Фантастика'),
        ('Драма', 'Драма'),
        ('Приключения', 'Приключения'),
        ('Триллер', 'Триллер'),
        ('Мистика', 'Мистика'),
        ('Экшен', 'Экшен'),
        ('Молодежный', 'Молодежный'),
        ('Комедия', 'Комедия'),
        ('Драма', 'Драма'),
        ('Фэнтези', 'Фэнтези'),
        ('Ужасы', 'Ужасы'),
        ('Мистика', 'Мистика'),
        ('Романтика', 'Романтика'),
        ('Фантастика', 'Фантастика'),
        ('Триллер', 'Триллер'),
        ('Документальный', 'Документальный'),
        ('Биография', 'Биография'),
        ('Криминал', 'Криминал'),
        ('Исторический', 'Исторический'),
        ('Военный', 'Военный'),
        ('Спорт', 'Спорт'),
        ('Психологический', 'Психологический'),
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=100, verbose_name='Укажите название фильма')
    create_at = models.DateField(verbose_name='Дата выхода')
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр', default='Фантастика')
    director = models.CharField(max_length=100, default='Неизвестен', verbose_name='Режиссёр')
    description = models.TextField(verbose_name='Укажите описание фильма')
    trailer_url  = models.URLField(verbose_name='Ссылка на трейлер фильма', default='https://example.com')
    duration = models.PositiveIntegerField(verbose_name='Продолжительность', default=90, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

class Reviews(models.Model):
    films_choice = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100, verbose_name='Как вас зовут?')
    text = models.TextField(verbose_name='Как вам фильм?')

    def __str__(self):
        return f'{self.films_choice}-{self.user_name}'
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'